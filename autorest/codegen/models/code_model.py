# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from itertools import chain
import logging
from typing import List, Dict, Optional, Any, Set

from .base_schema import BaseSchema
from .enum_schema import EnumSchema
from .object_schema import ObjectSchema
from .operation_group import OperationGroup
from .operation import Operation
from .lro_operation import LROOperation
from .paging_operation import PagingOperation
from .parameter import Parameter, ParameterLocation
from .client import Client
from .property import Property
from .parameter_list import ParameterList
from .imports import FileImport, ImportType
from .schema_response import SchemaResponse


_LOGGER = logging.getLogger(__name__)


class CredentialSchema(BaseSchema):
    def __init__(self):  # pylint: disable=super-init-not-called
        self.type = "azure.core.credentials.TokenCredential"

    @property
    def serialization_type(self) -> str:
        return self.type

    @property
    def docstring_type(self) -> str:
        return self.type

    @property
    def type_annotation(self) -> str:
        return '"TokenCredential"'

    @property
    def docstring_text(self) -> str:
        return "credential"


class IOSchema(BaseSchema):
    def __init__(self):  # pylint: disable=super-init-not-called
        self.type = "IO"

    @property
    def serialization_type(self) -> str:
        return self.type

    @property
    def docstring_type(self) -> str:
        return self.type

    @property
    def type_annotation(self) -> str:
        return self.docstring_type

    @property
    def docstring_text(self) -> str:
        return "IO"

    def imports(self):
        file_import = FileImport()
        file_import.add_from_import("typing", "IO", ImportType.STDLIB)
        return file_import


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

    def __init__(self, options: Dict[str, Any]):
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

    def sort_schemas(self) -> None:
        """Sorts the final object schemas by inheritance and by alphabetical order.

        :return: None
        :rtype: None
        """
        seen_schemas: Set[str] = set()
        sorted_schemas: List[ObjectSchema] = []
        for schema in sorted(self.schemas.values(), key=lambda x: x.name.lower()):
            if schema.name in seen_schemas:
                continue
            ancestors = []
            current = schema
            ancestors.append(schema)
            while current.base_model:
                parent = current.base_model
                if parent.name in seen_schemas:
                    break
                ancestors.insert(0, parent)
                seen_schemas.add(current.name)
                current = parent
            seen_schemas.add(current.name)
            sorted_schemas += ancestors
        self.sorted_schemas = sorted_schemas

    def add_credential_global_parameter(self) -> None:
        """Adds a `credential` global parameter.

        :return: None
        :rtype: None
        """
        credential_schema = CredentialSchema()
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

    @staticmethod
    def _lro_initial_function(operation: LROOperation) -> Operation:
        return Operation(
            yaml_data={},
            name="_" + operation.name + "_initial",
            description="",
            url=operation.url,
            method=operation.method,
            parameters=operation.parameters.parameters,
            responses=operation.responses,
            exceptions=operation.exceptions,
            media_types=operation.media_types,
            want_description_docstring=False,
            want_tracing=False,
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
                    operation.set_lro_response_type()
                    operation_group.operations.insert(i, CodeModel._lro_initial_function(operation))
                    i += 1
                i += 1

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

    def _add_properties_from_inheritance(self) -> None:
        """Adds properties from base classes to schemas with parents.

        :return: None
        :rtype: None
        """
        for schema in self.schemas.values():
            if schema.base_model:
                parent = schema.base_model
                while parent:
                    schema.properties = parent.properties + schema.properties
                    seen_properties: Set[Property] = set()
                    schema.properties = [
                        p
                        for p in schema.properties
                        if p.name not in seen_properties and not seen_properties.add(p.name)  # type: ignore
                    ]
                    parent = parent.base_model

    def _add_exceptions_from_inheritance(self) -> None:
        """Sets a class as an exception if it's parent is an exception.

        :return: None
        :rtype: None
        """
        for schema in self.schemas.values():
            if schema.base_model:
                parent = schema.base_model
                while parent:
                    if parent.is_exception:
                        schema.is_exception = True
                        break
                    parent = parent.base_model

    def add_inheritance_to_models(self) -> None:
        """Adds base classes and properties from base classes to schemas with parents.

        :return: None
        :rtype: None
        """
        for schema in self.schemas.values():
            if schema.base_model:
                # right now, the base model property just holds the name of the parent class
                schema.base_model = [b for b in self.schemas.values() if b.id == schema.base_model][0]
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
            obj.schema = IOSchema()

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
                    operation.responses,
                    operation.exceptions,
                    chain.from_iterable(response.headers for response in operation.responses),
                ):
                    self._populate_schema(obj)

    def add_schema_link_to_global_parameters(self) -> None:
        for parameter in self.global_parameters:
            self._populate_schema(parameter)
