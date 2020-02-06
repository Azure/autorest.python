# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
import datetime
from enum import Enum
from typing import cast, Any, Dict, List, Optional, Union

from .base_schema import BaseSchema
from .imports import FileImport, ImportType


_LOGGER = logging.getLogger(__name__)


class PrimitiveSchema(BaseSchema):
    _TYPE_MAPPINGS = {
        "boolean": "bool",
    }

    def _to_python_type(self) -> str:
        return self._TYPE_MAPPINGS.get(self.yaml_data["type"], "str")

    @property
    def serialization_type(self) -> str:
        return self._to_python_type()

    @property
    def docstring_type(self) -> str:
        return self._to_python_type()

    @property
    def type_annotation(self) -> str:
        return self.docstring_type

    @property
    def docstring_text(self) -> str:
        return self.docstring_type


class AnySchema(PrimitiveSchema):
    @property
    def serialization_type(self) -> str:
        return "object"

    @property
    def docstring_type(self) -> str:
        return "object"


class NumberSchema(PrimitiveSchema):
    def __init__(self, namespace: str, yaml_data: Dict[str, Any]):
        super(NumberSchema, self).__init__(namespace=namespace, yaml_data=yaml_data)
        self.precision = cast(int, yaml_data["precision"])
        self.multiple = cast(int, yaml_data.get("multipleOf"))
        self.maximum = cast(int, yaml_data.get("maximum"))
        self.minimum = cast(int, yaml_data.get("minimum"))
        self.exclusive_maximum = cast(int, yaml_data.get("exclusiveMaximum"))
        self.exclusive_minimum = cast(int, yaml_data.get("exclusiveMinimum"))

    @property
    def serialization_constraints(self) -> List[str]:
        validation_constraints = [
            f"maximum_ex={self.maximum}" if self.maximum is not None and self.exclusive_maximum else None,
            f"maximum={self.maximum}" if self.maximum is not None and not self.exclusive_maximum else None,
            f"minimum_ex={self.minimum}" if self.minimum is not None and self.exclusive_minimum else None,
            f"minimum={self.minimum}" if self.minimum is not None and not self.exclusive_minimum else None,
            f"multiple={self.multiple}" if self.multiple else None,
        ]
        return [x for x in validation_constraints if x is not None]

    @property
    def validation_map(self) -> Optional[Dict[str, Union[bool, int, str]]]:
        validation_map: Dict[str, Union[bool, int, str]] = {}
        if self.maximum is not None:
            if self.exclusive_maximum:
                validation_map["maximum_ex"] = self.maximum
            else:
                validation_map["maximum"] = self.maximum
        if self.minimum is not None:
            if self.exclusive_minimum:
                validation_map["minimum_ex"] = self.minimum
            else:
                validation_map["minimum"] = self.minimum
        if self.multiple:
            validation_map["multiple"] = self.multiple
        return validation_map or None

    @property
    def serialization_type(self) -> str:
        if self.yaml_data["type"] == "integer":
            if self.precision == 64:
                return "long"
            return "int"
        return "float"

    @property
    def docstring_type(self) -> str:
        if self.yaml_data["type"] == "integer":
            if self.precision == 64:
                return "long"
            return "int"
        return "float"

    @property
    def type_annotation(self) -> str:
        python_type = self.docstring_type
        if python_type == "long":
            return "int"
        return python_type


class StringSchema(PrimitiveSchema):
    def __init__(self, namespace: str, yaml_data: Dict[str, Any]):
        super(StringSchema, self).__init__(namespace=namespace, yaml_data=yaml_data)
        self.max_length = cast(int, yaml_data.get("maxLength"))
        self.min_length = cast(
            int, (yaml_data.get("minLength", 0) if yaml_data.get("maxLength") else yaml_data.get("minLength"))
        )
        self.pattern = cast(int, yaml_data.get("pattern"))

    @property
    def serialization_constraints(self) -> List[str]:
        validation_constraints = [
            f"max_length={self.max_length}" if self.max_length is not None else None,
            f"min_length={self.min_length}" if self.min_length is not None else None,
            f"pattern='{self.pattern}'" if self.pattern is not None else None,
        ]
        return [x for x in validation_constraints if x is not None]

    @property
    def validation_map(self) -> Optional[Dict[str, Union[bool, int, str]]]:
        validation_map: Dict[str, Union[bool, int, str]] = {}
        if self.max_length is not None:
            validation_map["max_length"] = self.max_length
        if self.min_length is not None:
            validation_map["min_length"] = self.min_length
        if self.pattern is not None:
            validation_map["pattern"] = self.pattern
        return validation_map or None

    def get_declaration(self, value) -> str:
        return f'"{value}"'


class DatetimeSchema(PrimitiveSchema):
    def __init__(self, namespace: str, yaml_data: Dict[str, Any]):
        super(DatetimeSchema, self).__init__(namespace=namespace, yaml_data=yaml_data)
        self.format = self.Formats(yaml_data["format"])

    class Formats(str, Enum):
        datetime = "date-time"
        rfc1123 = "date-time-rfc1123"

    @property
    def serialization_type(self) -> str:
        formats_to_attribute_type = {self.Formats.datetime: "iso-8601", self.Formats.rfc1123: "rfc-1123"}
        return formats_to_attribute_type[self.format]

    @property
    def docstring_type(self) -> str:
        return "~" + self.type_annotation

    @property
    def type_annotation(self) -> str:
        return "datetime.datetime"

    @property
    def docstring_text(self) -> str:
        return "datetime"

    def get_declaration(self, value: datetime.datetime) -> str:
        """Could be discussed, since technically I should return a datetime object,
        but msrest will do fine.
        """
        return f'"{value}"'

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.add_import("datetime", ImportType.STDLIB)
        return file_import


class UnixTimeSchema(PrimitiveSchema):
    @property
    def serialization_type(self) -> str:
        return "unix-time"

    @property
    def docstring_type(self) -> str:
        return "~" + self.type_annotation

    @property
    def type_annotation(self) -> str:
        return "datetime.datetime"

    @property
    def docstring_text(self) -> str:
        return "datetime"

    def get_declaration(self, value: datetime.datetime) -> str:
        """Could be discussed, since technically I should return a datetime object,
        but msrest will do fine.
        """
        return f'"{value}"'

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.add_import("datetime", ImportType.STDLIB)
        return file_import


class DateSchema(PrimitiveSchema):
    @property
    def serialization_type(self) -> str:
        return "date"

    @property
    def docstring_type(self) -> str:
        return "~" + self.type_annotation

    @property
    def type_annotation(self) -> str:
        return "datetime.date"

    @property
    def docstring_text(self) -> str:
        return "date"

    def get_declaration(self, value: datetime.date) -> str:
        """Could be discussed, since technically I should return a datetime object,
        but msrest will do fine.
        """
        return f'"{value}"'

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.add_import("datetime", ImportType.STDLIB)
        return file_import


class DurationSchema(PrimitiveSchema):
    @property
    def serialization_type(self) -> str:
        return "duration"

    @property
    def docstring_type(self) -> str:
        return "~" + self.type_annotation

    @property
    def type_annotation(self) -> str:
        return "datetime.timedelta"

    @property
    def docstring_text(self) -> str:
        return "timedelta"

    def get_declaration(self, value: datetime.timedelta) -> str:
        """Could be discussed, since technically I should return a datetime object,
        but msrest will do fine.
        """
        return f'"{value}"'

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.add_import("datetime", ImportType.STDLIB)
        return file_import


class ByteArraySchema(PrimitiveSchema):
    def __init__(self, namespace: str, yaml_data: Dict[str, Any]):
        super(ByteArraySchema, self).__init__(namespace=namespace, yaml_data=yaml_data)
        self.format = self.Formats(yaml_data["format"])

    class Formats(str, Enum):
        base64url = "base64url"
        byte = "byte"

    @property
    def serialization_type(self) -> str:
        if self.format == ByteArraySchema.Formats.base64url:
            return "base64"
        return "bytearray"

    @property
    def docstring_type(self) -> str:
        if self.format == ByteArraySchema.Formats.base64url:
            return "bytes"
        return "bytearray"

    def get_declaration(self, value: str) -> str:
        if self.format == ByteArraySchema.Formats.base64url:
            return f'bytes("{value}", encoding="utf-8")'
        return f'bytearray("{value}", encoding="utf-8")'


def get_primitive_schema(namespace: str, yaml_data: Dict[str, Any]) -> "PrimitiveSchema":
    mapping = {
        "integer": NumberSchema,
        "number": NumberSchema,
        "string": StringSchema,
        "char": StringSchema,
        "date-time": DatetimeSchema,
        "unixtime": UnixTimeSchema,
        "date": DateSchema,
        "duration": DurationSchema,
        "byte-array": ByteArraySchema,
        "any": AnySchema,
    }
    schema_type = yaml_data["type"]
    primitive_schema = cast(
        PrimitiveSchema, mapping.get(schema_type, PrimitiveSchema).from_yaml(namespace=namespace, yaml_data=yaml_data)
    )
    return primitive_schema
