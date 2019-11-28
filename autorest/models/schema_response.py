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
from typing import Dict, Optional, List, Union, Any


class HeaderResponse:
    def __init__(self, name:str, schema):
        self.name = name
        self.schema = schema


class SchemaResponse:
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        schema: Optional[Any],
        media_types: List[str],
        status_codes: List[Union[str, int]],
        headers: List[HeaderResponse],
    ):
        self.yaml_data = yaml_data
        self.schema = schema
        self.media_types = media_types
        self.status_codes = status_codes
        self.headers = headers

    @property
    def has_body(self):
        """Tell if that response defines a body.
        """
        return bool(self.schema)

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str], **kwargs) -> "SchemaResponse":

        return cls(
            yaml_data=yaml_data,
            schema=yaml_data.get("schema", None),  # FIXME replace by operation model
            media_types=yaml_data["protocol"]["http"].get("mediaTypes", []),
            status_codes=[
                int(code) if code != "default" else "default"
                for code in yaml_data["protocol"]["http"]["statusCodes"]
            ],
            headers=[
                HeaderResponse(header_prop['header'], header_prop['schema'])
                for header_prop in yaml_data["protocol"]["http"].get("headers", [])
            ]
        )

    def __repr__(self):
        return f"<{type(self)} {self.status_codes}>"