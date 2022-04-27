# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List, Dict, Optional, Any, Set, Union

from autorest.codegen.models.parameter import Parameter

from .base_type import BaseType
from .enum_type import EnumType
from .model_type import ModelType
from .operation_group import OperationGroup
from .client import Client, Config
from .request_builder import OverloadedRequestBuilder, RequestBuilder

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
     id to our created ModelType.
    :type schemas: dict[int, ~autorest.models.ModelType]
    :param sorted_schemas: Our schemas in order by inheritance and alphabet
    :type sorted_schemas: list[~autorest.models.ModelType]
    :param enums: The enums, if any, we are going to serialize. Maps their yaml id to our created EnumType.
    :type enums: Dict[int, ~autorest.models.EnumType]
    :param primitives: List of schemas we've created that are not EnumSchemas or ObjectSchemas. Maps their
     yaml id to our created schemas.
    :type primitives: Dict[int, ~autorest.models.BaseType]
    :param operation_groups: The operation groups we are going to serialize
    :type operation_groups: list[~autorest.models.OperationGroup]
    :param package_dependency: All the dependencies needed in setup.py
    :type package_dependency: Dict[str, str]
    """

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        options: Dict[str, Any],
    ) -> None:
        self.yaml_data = yaml_data
        self.options = options
        self.types_map: Dict[int, BaseType] = {} # map yaml id to schema
        self.operation_groups: List[OperationGroup] = []
        self._object_types: List[ModelType] = []
        self._client: Optional[Client] = None
        self._config: Optional[Config] = None
        self.request_builders: List[Union[RequestBuilder, OverloadedRequestBuilder]] = []
        self.package_dependency: Dict[str, str] = {}
        self.namespace: str = yaml_data["client"]["namespace"].lower()
        self.module_name: str = self.yaml_data["client"]["name"].replace(" ", "_").lower()

    def lookup_type(self, schema_id: int) -> BaseType:
        """Looks to see if the schema has already been created.

        :param int schema_id: The yaml id of the schema
        :return: If created, we return the created schema, otherwise, we throw.
        :rtype: ~autorest.models.BaseType
        :raises: KeyError if schema is not found
        """
        try:
            return next(
                type
                for id, type in self.types_map.items()
                if id == schema_id
            )
        except StopIteration:
            raise KeyError(f"Couldn't find schema with id {schema_id}")

    @property
    def credential(self) -> Optional[Parameter]:
        return self.client.parameters.credential

    @property
    def client(self) -> Client:
        if not self._client:
            raise ValueError("You haven't linked the client yet")
        return self._client

    @client.setter
    def client(self, val: Client) -> None:
        self._client = val

    @property
    def config(self) -> Config:
        if not self._config:
            raise ValueError("You haven't linked the config yet")
        return self._config

    @config.setter
    def config(self, val: Config) -> None:
        self._config = val

    def lookup_request_builder(self, request_builder_id: int) -> Union[RequestBuilder, OverloadedRequestBuilder]:
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
    def object_types(self) -> List[ModelType]:
        if not self._object_types:
            self._object_types = [t for t in self.types_map.values() if isinstance(t, ModelType)]
        return self._object_types

    @object_types.setter
    def object_types(self, val: List[ModelType]) -> None:
        self._object_types = val

    @property
    def enums(self) -> List[EnumType]:
        return [t for t in self.types_map.values() if isinstance(t, EnumType)]

    @staticmethod
    def _sort_schemas_helper(current: ModelType, seen_schema_names: Set[str], seen_schema_yaml_ids: Set[int]):
        if current.id in seen_schema_yaml_ids:
            return []
        if current.name in seen_schema_names:
            raise ValueError(
                f"We have already generated a schema with name {current.name}"
            )
        ancestors = [current]
        if current.parents:
            for parent in current.parents:
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
        sorted_object_schemas: List[ModelType] = []
        for schema in sorted(self.object_types, key=lambda x: x.name.lower()):
            sorted_object_schemas.extend(
                CodeModel._sort_schemas_helper(
                    schema, seen_schema_names, seen_schema_yaml_ids
                )
            )
        self.object_types = sorted_object_schemas

    def format_lro_operations(self) -> None:
        """Adds operations and attributes needed for LROs.
        If there are LRO functions in here, will add initial LRO function. Will also set the return
        type of the LRO operation
        """
        for operation_group in self.operation_groups:
            i = 0
            while i < len(operation_group.operations):
                operation = operation_group.operations[i]
                if operation.operation_type in ("lro", "lropaging"):
                    operation_group.operations.insert(i, operation.initial_operation)
                    i += 1
                i += 1

    @property
    def operations_folder_name(self) -> str:
        name = "operations"
        if self.options["version_tolerant"] and not any(
            og for og in self.operation_groups if not og.is_mixin
        ):
            name = f"_{name}"
        return name

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
            if o.is_mixin and self.options["python3_only"]
        )

    @property
    def has_lro_operations(self) -> bool:
        return any(
            [
                operation.operation_type in ("lro", "lropaging")
                for operation_group in self.operation_groups
                for operation in operation_group.operations
            ]
        )

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
    def rest_layer_name(self) -> str:
        return "rest" if self.options["builders_visibility"] == "public" else "_rest"
