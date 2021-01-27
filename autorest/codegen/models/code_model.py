# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from itertools import chain
import logging
from typing import cast, List, Dict, Optional, Any, Set, Union

from .base_schema import BaseSchema
from .credential_schema import AzureKeyCredentialSchema, TokenCredentialSchema
from .enum_schema import EnumSchema
from .object_schema import ObjectSchema
from .operation_group import OperationGroup
from .operation import Operation
from .lro_operation import LROOperation
from .paging_operation import PagingOperation
from .parameter import Parameter, ParameterLocation
from .client import Client
from .parameter_list import ParameterList
from .schema_response import SchemaResponse
from .property import Property
from .primitive_schemas import IOSchema


_LOGGER = logging.getLogger(__name__)


class CodeModel:  # pylint: disable=too-many-instance-attributes
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
    :param str custom_base_url: Optional. If user specifies a custom base url, this will override the default
    :param str base_url: Optional. The default base_url. Will include the host from yaml
    """

    def __init__(self, options: Dict[str, Any]) -> None:
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
        self.global_parameters: ParameterList = ParameterList()
        self.custom_base_url: Optional[str] = None
        self.base_url: Optional[str] = None
        self.service_client: Client = Client()

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
                ancestors = CodeModel._sort_schemas_helper(parent, seen_schema_names, seen_schema_yaml_ids) + ancestors
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
            sorted_schemas.extend(CodeModel._sort_schemas_helper(schema, seen_schema_names, seen_schema_yaml_ids))
        self.sorted_schemas = sorted_schemas

    def add_credential_global_parameter(self) -> None:
        """Adds a `credential` global parameter.

        :return: None
        :rtype: None
        """
        credential_schema: Union[AzureKeyCredentialSchema, TokenCredentialSchema]
        if self.options["credential_default_policy_type"] == "BearerTokenCredentialPolicy":
            credential_schema = TokenCredentialSchema(async_mode=False)
        else:
            credential_schema = AzureKeyCredentialSchema()
        credential_parameter = Parameter(
            yaml_data={},
            schema=credential_schema,
            serialized_name="credential",
            rest_api_name="credential",
            implementation="Client",
            description="Credential needed for the client to connect to Azure.",
            required=True,
            location=ParameterLocation.Other,
            skip_url_encoding=True,
            constraints=[],
        )
        self.global_parameters.insert(0, credential_parameter)

    def remove_next_operation(self) -> None:
        """Linking paging operations together.
        """
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
                if operation.yaml_data and operation.yaml_data['language']['python'].get('paging'):
                    next_link_yaml = operation.yaml_data['language']['python']['paging'].get('nextLinkOperation')
                if isinstance(operation, PagingOperation) and next_link_yaml:
                    next_operation = _lookup_operation(id(next_link_yaml))
                    operation.next_operation = next_operation
                    next_operations.append(next_operation)

            operation_group.operations = [
                operation for operation in operation_group.operations if operation not in next_operations
            ]

    @staticmethod
    def _add_properties_from_inheritance_helper(schema, properties) -> List[Property]:
        if not schema.base_models:
            return properties
        if schema.base_models:
            for base_model in schema.base_models:
                parent = cast(ObjectSchema, base_model)
                # need to make sure that the properties we choose from our parent also don't contain
                # any of our own properties
                schema_property_names = set([p.name for p in properties] + [p.name for p in schema.properties])
                chosen_parent_properties = [
                    p for p in parent.properties
                    if p.name not in schema_property_names
                ]
                properties = (
                    CodeModel._add_properties_from_inheritance_helper(parent, chosen_parent_properties) +
                    properties
                )

        return properties

    def _add_properties_from_inheritance(self) -> None:
        """Adds properties from base classes to schemas with parents.

        :return: None
        :rtype: None
        """
        for schema in self.schemas.values():
            schema.properties = CodeModel._add_properties_from_inheritance_helper(schema, schema.properties)

    @staticmethod
    def _add_exceptions_from_inheritance_helper(schema) -> bool:
        if schema.is_exception:
            return True
        parent_is_exception: List[bool] = []
        for base_model in schema.base_models:
            parent = cast(ObjectSchema, base_model)
            parent_is_exception.append(CodeModel._add_exceptions_from_inheritance_helper(parent))
        return any(parent_is_exception)

    def _add_exceptions_from_inheritance(self) -> None:
        """Sets a class as an exception if it's parent is an exception.

        :return: None
        :rtype: None
        """
        for schema in self.schemas.values():
            schema.is_exception = CodeModel._add_exceptions_from_inheritance_helper(schema)

    def add_inheritance_to_models(self) -> None:
        """Adds base classes and properties from base classes to schemas with parents.

        :return: None
        :rtype: None
        """
        for schema in self.schemas.values():
            if schema.base_models:
                # right now, the base model property just holds the name of the parent class
                schema.base_models = [b for b in self.schemas.values() if b.id in schema.base_models]
        self._add_properties_from_inheritance()
        self._add_exceptions_from_inheritance()

    def _populate_target_property(self, parameter: Parameter) -> None:
        for obj in self.sorted_schemas:
            for prop in obj.properties:
                if prop.id == parameter.target_property_name:
                    parameter.target_property_name = prop.name
                    return
        raise KeyError("Didn't find the target property")

    def _populate_schema(self, obj: Any) -> None:
        schema_obj = obj.schema
        if schema_obj and not isinstance(schema_obj, dict):
            return

        if schema_obj:
            schema_obj_id = id(obj.schema)
            _LOGGER.debug("Looking for id %s for member %s", schema_obj_id, obj)
            try:
                obj.schema = self.lookup_schema(schema_obj_id)
            except KeyError:
                _LOGGER.critical("Unable to ref the object")
                raise
        if isinstance(obj, Parameter) and obj.target_property_name:
            self._populate_target_property(obj)
        if isinstance(obj, SchemaResponse) and obj.is_stream_response:
            obj.schema = IOSchema(namespace=None, yaml_data={})

    def add_schema_link_to_operation(self) -> None:
        """Puts created schemas into operation classes `schema` property

        :return: None
        :rtype: None
        """
        # Index schemas
        for operation_group in self.operation_groups:
            for operation in operation_group.operations:
                for obj in chain(
                    operation.parameters,
                    operation.request.parameters,
                    operation.request.multiple_media_type_parameters or [],
                    operation.responses,
                    operation.exceptions,
                    chain.from_iterable(response.headers for response in operation.responses),
                    chain.from_iterable(request.parameters for request in operation.request.schema_requests)
                ):
                    self._populate_schema(obj)

    def add_schema_link_to_global_parameters(self) -> None:
        for parameter in self.global_parameters:
            self._populate_schema(parameter)

    def generate_single_parameter_from_multiple_media_types(self) -> None:
        for operation_group in self.operation_groups:
            for operation in operation_group.operations:
                if operation.request.multiple_media_type_parameters:
                    type_annot = ", ".join([
                        param.schema.operation_type_annotation
                        for param in operation.request.multiple_media_type_parameters
                    ])
                    docstring_type = " or ".join([
                        param.schema.docstring_type for param in operation.request.multiple_media_type_parameters
                    ])
                    chosen_parameter = next(
                        iter(filter(lambda x: x.has_multiple_media_types, operation.request.parameters)), None
                    )
                    if not chosen_parameter:
                        raise ValueError("You are missing a parameter that has multiple media types")
                    chosen_parameter.multiple_media_types_type_annot = f"Union[{type_annot}]"
                    chosen_parameter.multiple_media_types_docstring_type = docstring_type

    @property
    def has_lro_operations(self) -> bool:
        return any([
            isinstance(operation, LROOperation)
            for operation_group in self.operation_groups
            for operation in operation_group.operations
        ])

    @staticmethod
    def base_url_method_signature(async_mode: bool) -> str:
        if async_mode:
            return "base_url: Optional[str] = None,"
        return "base_url=None,  # type: Optional[str]"
