# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
from enum import Enum
from typing import Dict, Optional, List, Union, Any


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


class Parameter:
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        schema: Optional[Any],
        rest_api_name: str,
        serialized_name: str,
        description: str,
        implementation: str,
        is_required: bool,
        location: ParameterLocation,
        skip_url_encoding: bool,
        constraints: List[Any],
        style: Optional[ParameterStyle] = None,
    ):
        self.yaml_data = yaml_data
        self.schema = schema
        self.rest_api_name = rest_api_name
        self.serialized_name = serialized_name
        self.description = description
        self._implementation = implementation
        self.is_required = is_required
        self.location = location
        self.skip_url_encoding = skip_url_encoding
        self.constraints = constraints
        self.style = style

    @property
    def implementation(self):
        # https://github.com/Azure/autorest.modelerfour/issues/81
        if self.serialized_name == "api_version":
            return "Method"
        return self._implementation

    @property
    def for_method_signature(self):
        if self.is_required:
            return self.serialized_name
        else:
            return f"{self.serialized_name}=None"

    @property
    def full_serialized_name(self):
        origin_name = self.serialized_name
        if self.implementation == "Client":
            origin_name = f"self._config.{self.serialized_name}"
        return origin_name

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str], **kwargs) -> "SchemaResponse":

        http_protocol = yaml_data["protocol"]["http"]
        return cls(
            yaml_data=yaml_data,
            schema=yaml_data.get("schema", None),  # FIXME replace by operation model
            # See also https://github.com/Azure/autorest.modelerfour/issues/80
            rest_api_name=yaml_data["language"]["default"].get("serializedName", yaml_data["language"]["default"]["name"]),
            serialized_name=yaml_data['language']['python']['name'],
            description=yaml_data["language"]["python"]["description"],
            implementation=yaml_data["implementation"],
            is_required=yaml_data.get("required", False),
            location=ParameterLocation(http_protocol["in"]),
            skip_url_encoding=yaml_data.get("extensions", {}).get("x-ms-skip-url-encoding", False),
            constraints=[], # FIXME constraints
            style=ParameterStyle(http_protocol["style"]) if "style" in http_protocol else None,
        )
