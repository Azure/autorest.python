# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, Optional, TYPE_CHECKING
from .parameter import (
    ParameterMethodLocation,
    ParameterOnlyPathAndBodyPositional,
    ParameterLocation,
    ParameterStyle,
    get_target_property_name,
)
from .utils import get_schema

if TYPE_CHECKING:
    from .code_model import CodeModel


def _make_public(name):
    if name[0] == "_":
        return name[1:]
    return name


class RequestBuilderParameter(ParameterOnlyPathAndBodyPositional):
    @property
    def in_method_signature(self) -> bool:
        return not (
            # if not inputtable, don't put in signature
            not self.inputtable_by_user
            # If i'm not in the method code, no point in being in signature
            or not self.in_method_code
            # If I'm a flattened property of a body, don't want me, want the body param
            or self.target_property_name
            or not self.in_method_code
        )

    @property
    def name_in_high_level_operation(self) -> str:
        if self.is_body and not self.constant:
            return f"_{self.serialized_name}"
        name = self.yaml_data["language"]["python"]["name"]
        if self.implementation == "Client" and self.in_method_code:
            # for these, we're passing the client params to the request builder.
            # Need the self._config prefix
            name = f"self._config.{name}"
        return name

    @property
    def in_method_code(self) -> bool:
        if self.location == ParameterLocation.Uri:
            # don't want any base url path formatting arguments
            return False
        return super(RequestBuilderParameter, self).in_method_code

    @property
    def default_value_declaration(self) -> Optional[str]:
        if self.serialized_name == "content_type":
            # in request builders we're in a weird scenario
            # we need to know what the types of content_type are
            # but we want to serialize content_type with no default.
            # So, we just return None in default_value_declaration for now
            return "None"
        return super().default_value_declaration

    @property
    def method_location(self) -> ParameterMethodLocation:
        super_method_location = super().method_location
        if super_method_location in (
            ParameterMethodLocation.KWARG,
            ParameterMethodLocation.HIDDEN_KWARG,
        ):
            return super_method_location
        if self.location != ParameterLocation.Path:
            return ParameterMethodLocation.KEYWORD_ONLY
        return super_method_location

    @method_location.setter
    def method_location(self, val: ParameterMethodLocation) -> None:
        self._method_location = val

    @property
    def full_serialized_name(self) -> str:
        return self.serialized_name

    @classmethod
    def from_yaml(
        cls,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        *,
        content_types: Optional[List[str]] = None,
    ) -> "RequestBuilderParameter":
        http_protocol = yaml_data["protocol"].get(
            "http", {"in": ParameterLocation.Other}
        )
        name = yaml_data["language"]["python"]["name"]
        location = ParameterLocation(http_protocol["in"])
        serialized_name = yaml_data["language"]["python"]["name"]
        schema = get_schema(code_model, yaml_data.get("schema"), serialized_name)
        target_property = yaml_data.get("targetProperty")
        target_property_name = (
            get_target_property_name(code_model, id(target_property))
            if target_property
            else None
        )
        return cls(
            code_model=code_model,
            yaml_data=yaml_data,
            schema=schema,
            # See also https://github.com/Azure/autorest.modelerfour/issues/80
            rest_api_name=yaml_data["language"]["default"].get(
                "serializedName", yaml_data["language"]["default"]["name"]
            ),
            serialized_name=_make_public(name),
            description=yaml_data["language"]["python"]["description"],
            implementation=yaml_data["implementation"],
            required=yaml_data.get("required", False),
            location=location,
            skip_url_encoding=yaml_data.get("extensions", {}).get(
                "x-ms-skip-url-encoding", False
            ),
            constraints=[],  # FIXME constraints
            target_property_name=target_property_name,
            style=ParameterStyle(http_protocol["style"])
            if "style" in http_protocol
            else None,
            explode=http_protocol.get("explode", False),
            grouped_by=yaml_data.get("groupedBy", None),
            original_parameter=yaml_data.get("originalParameter", None),
            flattened=yaml_data.get("flattened", False),
            client_default_value=yaml_data.get("clientDefaultValue"),
            content_types=content_types,
        )
