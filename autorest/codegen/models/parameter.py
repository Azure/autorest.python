# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from enum import Enum
import logging
from typing import Dict, Optional, List, Any, Union

from .imports import FileImport, ImportType
from .base_model import BaseModel
from .base_schema import BaseSchema


_LOGGER = logging.getLogger(__name__)


class ParameterLocation(Enum):
    Path = "path"
    Body = "body"
    Query = "query"
    Header = "header"
    Uri = "uri"
    Other = "other"


class ParameterStyle(Enum):
    simple = "simple"
    label = "label"
    matrix = "matrix"
    form = "form"
    spaceDelimited = "spaceDelimited"
    pipeDelimited = "pipeDelimited"
    deepObject = "deepObject"
    tabDelimited = "tabDelimited"
    json = "json"
    binary = "binary"
    xml = "xml"


class Parameter(BaseModel):  # pylint: disable=too-many-instance-attributes
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        schema: BaseSchema,
        rest_api_name: str,
        serialized_name: str,
        description: str,
        implementation: str,
        required: bool,
        location: ParameterLocation,
        skip_url_encoding: bool,
        constraints: List[Any],
        target_property_name: Optional[Union[int, str]] = None,  # first uses id as placeholder
        style: Optional[ParameterStyle] = None,
        *,
        flattened: bool = False,
        grouped_by: Optional["Parameter"] = None,
        original_parameter: Optional["Parameter"] = None,
        client_default_value: Optional[Any] = None,
    ):
        super().__init__(yaml_data)
        self.schema = schema
        self.rest_api_name = rest_api_name
        self.serialized_name = serialized_name
        self.description = description
        self._implementation = implementation
        self.required = required
        self.location = location
        self.skip_url_encoding = skip_url_encoding
        self.constraints = constraints
        self.target_property_name = target_property_name
        self.style = style
        self.flattened = flattened
        self.grouped_by = grouped_by
        self.original_parameter = original_parameter
        self.client_default_value = client_default_value

    @property
    def implementation(self) -> str:
        # https://github.com/Azure/autorest.modelerfour/issues/81
        if self.serialized_name == "api_version":
            return "Method"
        return self._implementation

    def _default_value(self):
        type_annot = self.schema.operation_type_annotation
        if not self.required:
            type_annot = f"Optional[{type_annot}]"

        if self.client_default_value is not None:
            return self.client_default_value, self.schema.get_declaration(self.client_default_value), type_annot

        default_value = self.schema.default_value
        default_value_declaration = self.schema.default_value_declaration
        if default_value is not None and self.required:
            _LOGGER.warning(
                "Parameter '%s' is required and has a default value, this combination is not recommended",
                self.rest_api_name
            )

        return default_value, default_value_declaration, type_annot

    @property
    def sync_method_signature(self) -> str:
        default_value, default_value_declaration, type_annot = self._default_value()
        if default_value is not None or not self.required:
            return f"{self.serialized_name}={default_value_declaration},  # type: {type_annot}"
        return f"{self.serialized_name},  # type: {type_annot}"

    @property
    def async_method_signature(self) -> str:
        default_value, default_value_declaration, type_annot = self._default_value()
        if default_value is not None or not self.required:
            return f"{self.serialized_name}: {type_annot} = {default_value_declaration}"
        return f"{self.serialized_name}: {type_annot}"

    @property
    def full_serialized_name(self) -> str:
        origin_name = self.serialized_name
        if self.implementation == "Client":
            origin_name = f"self._config.{self.serialized_name}"
        return origin_name

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any]) -> "Parameter":
        http_protocol = yaml_data["protocol"].get("http", {"in": ParameterLocation.Other})
        return cls(
            yaml_data=yaml_data,
            schema=yaml_data.get("schema", None),  # FIXME replace by operation model
            # See also https://github.com/Azure/autorest.modelerfour/issues/80
            rest_api_name=yaml_data["language"]["default"].get(
                "serializedName", yaml_data["language"]["default"]["name"]
            ),
            serialized_name=yaml_data["language"]["python"]["name"],
            description=yaml_data["language"]["python"]["description"],
            implementation=yaml_data["implementation"],
            required=yaml_data.get("required", False),
            location=ParameterLocation(http_protocol["in"]),
            skip_url_encoding=yaml_data.get("extensions", {}).get("x-ms-skip-url-encoding", False),
            constraints=[],  # FIXME constraints
            target_property_name=id(yaml_data["targetProperty"]) if yaml_data.get("targetProperty") else None,
            style=ParameterStyle(http_protocol["style"]) if "style" in http_protocol else None,
            grouped_by=yaml_data.get("groupedBy", None),
            original_parameter=yaml_data.get("originalParameter", None),
            flattened=yaml_data.get("flattened", False),
            client_default_value=yaml_data.get("clientDefaultValue"),
        )

    def imports(self) -> FileImport:
        file_import = self.schema.imports()
        if not self.required:
            file_import.add_from_import("typing", "Optional", ImportType.STDLIB)
        return file_import
