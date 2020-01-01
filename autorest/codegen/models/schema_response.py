# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, Optional, List, Union, Any

from .base_model import BaseModel


class HeaderResponse:
    def __init__(self, name: str, schema):
        self.name = name
        self.schema = schema


class SchemaResponse(BaseModel):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        schema: Optional[Any],
        media_types: List[str],
        status_codes: List[Union[str, int]],
        headers: List[HeaderResponse],
        binary: bool,
    ):
        super().__init__(yaml_data)
        self.schema = schema
        self.media_types = media_types
        self.status_codes = status_codes
        self.headers = headers
        self.binary = binary

    @property
    def has_body(self):
        """Tell if that response defines a body.
        """
        return bool(self.schema)

    @property
    def has_headers(self):
        """Tell if that response defines headers.
        """
        return bool(self.headers)

    @property
    def is_stream_response(self):
        """Is the response expected to be streamable, like a download."""
        return self.binary

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
            ],
            binary=yaml_data.get("binary", False),
        )

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.status_codes}>"