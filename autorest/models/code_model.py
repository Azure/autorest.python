# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from itertools import chain
import logging
from typing import List, Dict, Optional, Any, cast, Set

from .base_schema import BaseSchema
from .enum_schema import EnumSchema
from .primitive_schemas import PrimitiveSchema
from .object_schema import ObjectSchema
from .operation_group import OperationGroup
from .operation import Operation
from .lro_operation import LROOperation
from .paging_operation import PagingOperation
from .parameter import Parameter, ParameterLocation
from .client import Client


_LOGGER = logging.getLogger(__name__)


class FakeSchema(BaseSchema):
    """Remove this guy eventually, just to make some fast process during dev.
    """
    def __init__(self):
        ...

    def get_serialization_type(self):
        return "FAKESERIALIZATIONTYPE"

    def get_python_type(self, namespace=None):
        return namespace+"FAKEDOCSTRING"


class CodeModel:
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
        self.module_name = None
        self.class_name = None
        self.description = None
        self.namespace = None
        self.namespace_path = None
        self.tracing = None
        self.schemas: Dict[int, ObjectSchema] = {}
        self.sorted_schemas: List[ObjectSchema] = []
        self.enums: Dict[int, EnumSchema] = {}
        self.primitives: Dict[int, BaseSchema] = {}
        self.operation_groups: List[OperationGroup] = []
        self.global_parameters: List[Parameter] = []
        self.custom_base_url: Optional[str] = None
        self.base_url: Optional[str] = None
        self.service_client = Client()

    def lookup_schema(self, schema_id: int) -> None:
        """Looks to see if the schema has already been created.

        :param int schema_id: The yaml id of the schema
        :return: If created, we return the created schema, otherwise, we throw.
        :rtype: ~autorest.models.BaseSchema
        :raises: KeyError if schema is not found
        """
        for attr in [self.schemas, self.enums, self.primitives]:
            for elt_key, elt_value in attr.items():
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
        credential_schema = PrimitiveSchema(yaml_data={"type": "credential"})
        credential_parameter = Parameter(
            yaml_data={},
            schema=credential_schema,
            serialized_name="credential",
            rest_api_name="credential",
            implementation="Client",
            description="Credential needed for the client to connect to Azure.",
            is_required=True,
            location=ParameterLocation.Other,
            skip_url_encoding=True,
            constraints=[]
        )
        self.global_parameters.insert(0, credential_parameter)

    @staticmethod
    def _lro_initial_function(operation):
        return Operation(
            yaml_data={},
            name="_" + operation.name + "_initial",
            description="",
            url=operation.url,
            method=operation.method,
            parameters=operation.parameters,
            responses=operation.responses,
            exceptions=operation.exceptions,
            media_types=operation.media_types,
            want_description_docstring=False,
            want_tracing=False
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

        Could disapear if https://github.com/Azure/autorest.modelerfour/issues/85 done
        """
        for operation_group in self.operation_groups:
            # Build an index to be faster
            op_index = {
                operation.yaml_data.get('language', {}).get('default', {}).get('name'): operation
                for operation
                in operation_group.operations
            }

            next_operations = []
            for operation in operation_group.operations:
                if isinstance(operation, PagingOperation) and operation.operation_name:
                    short_op_name = operation.operation_name.split('_')[-1]
                    if short_op_name not in op_index:
                        raise ValueError(f"Could not find {operation.operation_name} in op group {operation_group.name} I have {op_index.keys()}")

                    next_operation = op_index[short_op_name]
                    operation.next_operation = next_operation
                    next_operations.append(next_operation)

            operation_group.operations = [
                operation
                for operation
                in operation_group.operations
                if operation not in next_operations
            ]

    def enable_parameter_flattening(self):
        for op_group in self.operation_groups:
            for operation in op_group.operations:
                self._enable_parameter_flattening_for_operation(operation)

    def _enable_parameter_flattening_for_operation(self, operation):
        if not (operation.has_request_body and isinstance(operation.body_parameter.schema, ObjectSchema)):
            return

        body_schema = cast(ObjectSchema, operation.body_parameter.schema)
        properties = [prop for prop in body_schema.properties if not (prop.constant or prop.readonly)]

        if len(properties) > self.options.get("payload-flattening-threshold", 0):
            return

        # Create fake parameters, so we can use the template as usual
        fake_parameters = []
        for prop in properties:
            fake_parameters.append(
                Parameter(
                    yaml_data=None,
                    schema=prop.schema,
                    rest_api_name=prop.original_swagger_name,
                    serialized_name=prop.name,
                    description=prop.description,
                    implementation="Method",
                    is_required=prop.required,
                    location=ParameterLocation.Other,
                    skip_url_encoding=False, # Doesn't matter here
                    constraints=[], # FIXME inject validation map
                )
            )

        # Insert after the body parameter these fake parameters
        body_parameter_index = operation.parameters.index(operation.body_parameter)
        operation.parameters[body_parameter_index:body_parameter_index] = fake_parameters

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
                    seen_properties: Set["BaseSchema"] = set()
                    schema.properties = [p for p in schema.properties if p.name not in seen_properties and not seen_properties.add(p.name)]
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

    def _populate_schema(self, obj):
        schema_obj = obj.schema
        if schema_obj:
            schema_obj_id = id(obj.schema)
            _LOGGER.debug("Looking for id %s for member %s", schema_obj_id, obj)
            try:
                obj.schema = self.lookup_schema(schema_obj_id)
            except KeyError:
                _LOGGER.critical("Unable to ref the object")
                obj.schema = FakeSchema()

    def add_schema_link_to_operation(self) -> None:
        """Puts created schemas into operation classes `schema` property

        :return: None
        :rtype: None
        """
        # Index schemas
        for operation_group in self.operation_groups:
            for operation in operation_group.operations:
                for obj in chain(operation.parameters, operation.responses, operation.exceptions, chain.from_iterable(response.headers for response in operation.responses)):
                    self._populate_schema(obj)

    def add_schema_link_to_global_parameters(self) -> None:
        for parameter in self.global_parameters:
            self._populate_schema(parameter)
