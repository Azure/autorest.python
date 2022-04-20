# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import cast, List, Dict, Optional, Any, Set

from .base_schema import BaseSchema
from .enum_schema import EnumSchema
from .object_schema import ObjectSchema
from .operation_group import OperationGroup
from .operation import Operation
from .lro_operation import LROOperation
from .paging_operation import PagingOperation
from .parameter import Parameter
from .client import Client
from .parameter_list import GlobalParameterList
from .property import Property
from .request_builder import RequestBuilder
from .credential_model import CredentialModel

_LOGGER = logging.getLogger(__name__)


class CodeModel:  # pylint: disable=too-many-instance-attributes, too-many-public-methods
    """Holds all of the information we have parsed out of the yaml file. The CodeModel is what gets
    serialized by the serializers.

    :param options: Options of the code model. I.e., whether this is for management generation
    :type options: dict[str, bool]
    :param str module_name: The module name for the client. Is in snake case.
    :param str class_name: The class name for the client. Is in pascal case.
    :param str description: The description of the client
    :param str namespace: The namespace of our module
    :param schemas: The list of schemas we are going to serialize in the models files. Maps their yaml
     id to our created ObjectSchema.
    :type schemas: dict[int, ~autorest.models.ObjectSchema]
    :param sorted_schemas: Our schemas in order by inheritance and alphabet
    :type sorted_schemas: list[~autorest.models.ObjectSchema]
    :param enums: The enums, if any, we are going to serialize. Maps their yaml id to our created EnumSchema.
    :type enums: Dict[int, ~autorest.models.EnumSchema]
    :param primitives: List of schemas we've created that are not EnumSchemas or ObjectSchemas. Maps their
     yaml id to our created schemas.
    :type primitives: Dict[int, ~autorest.models.BaseSchema]
    :param operation_groups: The operation groups we are going to serialize
    :type operation_groups: list[~autorest.models.OperationGroup]
    :param package_dependency: All the dependencies needed in setup.py
    :type package_dependency: Dict[str, str]
    :param credential_model: The class contains all the credential info
    :type credential_model: CredentialMode
    """

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        options: Dict[str, Any],
    ) -> None:
        self.yaml_data = yaml_data
        self.send_request_name = (
            "send_request" if options["show_send_request"] else "_send_request"
        )
        self.rest_layer_name = (
            "rest" if options["builders_visibility"] == "public" else "_rest"
        )
        self.options = options
        self.module_name: str = ""
        self.class_name: str = ""
        self.description: str = ""
        self.namespace: str = ""
        self.namespace_path: str = ""
        self.schemas: Dict[int, ObjectSchema] = {}
        self.sorted_schemas: List[ObjectSchema] = []
        self.enums: Dict[int, EnumSchema] = {}
        self.primitives: Dict[int, BaseSchema] = {}
        self.operation_groups: List[OperationGroup] = []
        params = GlobalParameterList(self)
        params.code_model = self
        self.service_client: Client = Client(self, params)
        self.request_builders: List[RequestBuilder] = []
        self.package_dependency: Dict[str, str] = {}
        self._credential_model: Optional[CredentialModel] = None

    @property
    def global_parameters(self) -> GlobalParameterList:
        return self.service_client.parameters

    @global_parameters.setter
    def global_parameters(self, val: GlobalParameterList) -> None:
        self.service_client.parameters = val

    def lookup_schema(self, schema_id: int) -> BaseSchema:
        """Looks to see if the schema has already been created.

        :param int schema_id: The yaml id of the schema
        :return: If created, we return the created schema, otherwise, we throw.
        :rtype: ~autorest.models.BaseSchema
        :raises: KeyError if schema is not found
        """
        for attr in [self.schemas, self.enums, self.primitives]:
            for elt_key, elt_value in attr.items():  # type: ignore
                if schema_id == elt_key:
                    return elt_value
        raise KeyError("Didn't find it!!!!!")

    def lookup_request_builder(self, request_builder_id: int) -> RequestBuilder:
        """Find the request builder based off of id"""
        try:
            return next(
                rb
                for rb in self.request_builders
                if id(rb.yaml_data) == request_builder_id
            )
        except StopIteration:
            raise KeyError(f"No request builder with id {request_builder_id} found.")

    @property
    def exception_ids(self) -> Set[int]:
        exceptions_set = set()
        for group in self.yaml_data["operationGroups"]:
            for operation in group["operations"]:
                if not operation.get("exceptions"):
                    continue
                for exception in operation["exceptions"]:
                    if not exception.get("schema"):
                        continue
                    exceptions_set.add(id(exception["schema"]))
        return exceptions_set

    @staticmethod
    def _sort_schemas_helper(current, seen_schema_names, seen_schema_yaml_ids):
        if current.id in seen_schema_yaml_ids:
            return []
        if current.name in seen_schema_names:
            raise ValueError(
                f"We have already generated a schema with name {current.name}"
            )
        ancestors = [current]
        if current.base_models:
            for base_model in current.base_models:
                parent = cast(ObjectSchema, base_model)
                if parent.id in seen_schema_yaml_ids:
                    continue
                seen_schema_names.add(current.name)
                seen_schema_yaml_ids.add(current.id)
                ancestors = (
                    CodeModel._sort_schemas_helper(
                        parent, seen_schema_names, seen_schema_yaml_ids
                    )
                    + ancestors
                )
        seen_schema_names.add(current.name)
        seen_schema_yaml_ids.add(current.id)
        return ancestors

    def sort_schemas(self) -> None:
        """Sorts the final object schemas by inheritance and by alphabetical order.

        :return: None
        :rtype: None
        """
        seen_schema_names: Set[str] = set()
        seen_schema_yaml_ids: Set[int] = set()
        sorted_schemas: List[ObjectSchema] = []
        for schema in sorted(self.schemas.values(), key=lambda x: x.name.lower()):
            sorted_schemas.extend(
                CodeModel._sort_schemas_helper(
                    schema, seen_schema_names, seen_schema_yaml_ids
                )
            )
        self.sorted_schemas = sorted_schemas

    def setup_client_input_parameters(self, yaml_data: Dict[str, Any]):
        dollar_host = [
            parameter
            for parameter in self.global_parameters
            if parameter.rest_api_name == "$host"
        ]
        if not dollar_host:
            # We don't want to support multi-api customurl YET (will see if that goes well....)
            # So far now, let's get the first one in the first operation
            # UGLY as hell.....
            if yaml_data.get("operationGroups"):
                first_req_of_first_op_of_first_grp = yaml_data["operationGroups"][0][
                    "operations"
                ][0]["requests"][0]
                self.service_client.parameterized_host_template = (
                    first_req_of_first_op_of_first_grp["protocol"]["http"]["uri"]
                )
        else:
            for host in dollar_host:
                self.global_parameters.remove(host)
            self.service_client.parameters.add_host(
                dollar_host[0].yaml_data["clientDefaultValue"]
            )

    def format_lro_operations(self) -> None:
        """Adds operations and attributes needed for LROs.
        If there are LRO functions in here, will add initial LRO function. Will also set the return
        type of the LRO operation
        """
        for operation_group in self.operation_groups:
            i = 0
            while i < len(operation_group.operations):
                operation = operation_group.operations[i]
                if isinstance(operation, LROOperation):
                    operation_group.operations.insert(i, operation.initial_operation)
                    i += 1
                i += 1

    def remove_next_operation(self) -> None:
        """Linking paging operations together."""

        def _lookup_operation(yaml_id: int) -> Operation:
            for operation_group in self.operation_groups:
                for operation in operation_group.operations:
                    if operation.id == yaml_id:
                        return operation
            raise KeyError("Didn't find it!!!!!")

        for operation_group in self.operation_groups:
            next_operations = []
            for operation in operation_group.operations:
                # when we add in "LRO" functions we don't include yaml_data, so yaml_data can be empty in these cases
                next_link_yaml = None
                if operation.yaml_data and operation.yaml_data["language"][
                    "python"
                ].get("paging"):
                    next_link_yaml = operation.yaml_data["language"]["python"][
                        "paging"
                    ].get("nextLinkOperation")
                if isinstance(operation, PagingOperation) and next_link_yaml:
                    next_operation = _lookup_operation(id(next_link_yaml))
                    operation.next_operation = next_operation
                    next_operations.append(next_operation)

            operation_group.operations = [
                operation
                for operation in operation_group.operations
                if operation not in next_operations
            ]

    @property
    def has_schemas(self):
        return self.schemas or self.enums

    @property
    def credential_model(self) -> CredentialModel:
        if not self._credential_model:
            raise ValueError(
                "You want to find the Credential Model, but have not given a value"
            )
        return self._credential_model

    @credential_model.setter
    def credential_model(self, val: CredentialModel) -> None:
        self._credential_model = val

    @staticmethod
    def _add_properties_from_inheritance_helper(schema, properties) -> List[Property]:
        if not schema.base_models:
            return properties
        if schema.base_models:
            for base_model in schema.base_models:
                parent = cast(ObjectSchema, base_model)
                # need to make sure that the properties we choose from our parent also don't contain
                # any of our own properties
                schema_property_names = set(
                    [p.name for p in properties] + [p.name for p in schema.properties]
                )
                chosen_parent_properties = [
                    p for p in parent.properties if p.name not in schema_property_names
                ]
                properties = (
                    CodeModel._add_properties_from_inheritance_helper(
                        parent, chosen_parent_properties
                    )
                    + properties
                )

        return properties

    @property
    def operations_folder_name(self) -> str:
        name = "operations"
        if self.options["version_tolerant"] and not any(
            og for og in self.operation_groups if not og.is_empty_operation_group
        ):
            name = f"_{name}"
        return name

    def _add_properties_from_inheritance(self) -> None:
        """Adds properties from base classes to schemas with parents.

        :return: None
        :rtype: None
        """
        for schema in self.schemas.values():
            schema.properties = CodeModel._add_properties_from_inheritance_helper(
                schema, schema.properties
            )

    @staticmethod
    def _add_exceptions_from_inheritance_helper(schema) -> bool:
        if schema.is_exception:
            return True
        parent_is_exception: List[bool] = []
        for base_model in schema.base_models:
            parent = cast(ObjectSchema, base_model)
            parent_is_exception.append(
                CodeModel._add_exceptions_from_inheritance_helper(parent)
            )
        return any(parent_is_exception)

    def _add_exceptions_from_inheritance(self) -> None:
        """Sets a class as an exception if it's parent is an exception.

        :return: None
        :rtype: None
        """
        for schema in self.schemas.values():
            schema.is_exception = CodeModel._add_exceptions_from_inheritance_helper(
                schema
            )

    def add_inheritance_to_models(self) -> None:
        """Adds base classes and properties from base classes to schemas with parents.

        :return: None
        :rtype: None
        """
        for schema in self.schemas.values():
            if schema.base_models:
                # right now, the base model property just holds the name of the parent class
                schema.base_models = [
                    b for b in self.schemas.values() if b.id in schema.base_models
                ]
        self._add_properties_from_inheritance()
        self._add_exceptions_from_inheritance()

    def _populate_target_property(self, parameter: Parameter) -> None:
        for obj in self.schemas.values():
            for prop in obj.properties:
                if prop.id == parameter.target_property_name:
                    parameter.target_property_name = prop.name
                    return
        raise KeyError("Didn't find the target property")

    def generate_single_parameter_from_multiple_content_types_operation(self) -> None:
        for operation_group in self.operation_groups:
            for operation in operation_group.operations:
                if operation.multiple_content_type_parameters:
                    operation.convert_multiple_content_type_parameters()

    def need_vendored_code(self, async_mode: bool) -> bool:
        if async_mode:
            return self.need_mixin_abc
        return (
            self.need_request_converter or self.need_format_url or self.need_mixin_abc
        )

    @property
    def need_request_converter(self) -> bool:
        return (
            self.options["show_operations"]
            and bool(self.request_builders)
            and not self.options["version_tolerant"]
        )

    @property
    def need_format_url(self) -> bool:
        return any(rq for rq in self.request_builders if rq.parameters.path)

    @property
    def need_mixin_abc(self) -> bool:
        return any(
            o
            for o in self.operation_groups
            if o.is_empty_operation_group and self.options["python3_only"]
        )

    @property
    def has_lro_operations(self) -> bool:
        return any(
            [
                isinstance(operation, LROOperation)
                for operation_group in self.operation_groups
                for operation in operation_group.operations
            ]
        )

    def link_operation_to_request_builder(self) -> None:
        for operation_group in self.operation_groups:
            for operation in operation_group.operations:
                request_builder = operation.request_builder
                if isinstance(operation, LROOperation):
                    request_builder.name = request_builder.name + "_initial"
                operation.request_builder = request_builder
                operation.link_body_kwargs_to_body_params()

    def get_models_filename(self, is_python3_file: bool) -> str:
        if (
            self.options["version_tolerant"] or self.options["low_level_client"]
        ) and self.options["python3_only"]:
            return "_models"
        if is_python3_file:
            return "_models_py3"
        return "_models"

    @property
    def enums_filename(self) -> str:
        if self.options["version_tolerant"] or self.options["low_level_client"]:
            return "_enums"
        return f"_{self.module_name}_enums"

    @property
    def is_legacy(self) -> bool:
        return not (self.options["version_tolerant"] or self.options["low_level_client"])
        # return not any(
        #     g
        #     for g in ["low_level_client", "version_tolerant"]
        #     if g in self.options
        # )
