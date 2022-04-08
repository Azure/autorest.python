# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
import datetime
from enum import Enum
from typing import cast, Any, Dict, List, Optional, Union, TYPE_CHECKING

from .base_schema import BaseSchema
from .imports import FileImport, ImportType, TypingSection

if TYPE_CHECKING:
    from .code_model import CodeModel


_LOGGER = logging.getLogger(__name__)

class RawString(object):
    def __init__(self, string: str) -> None:
        self.string = string

    def __repr__(self) -> str:
        return "r'{}'".format(self.string.replace('\'', '\\\''))



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

    def type_annotation(self, *, is_operation_file: bool = False) -> str:  # pylint: disable=unused-argument
        return self.docstring_type

    @property
    def docstring_text(self) -> str:
        return self.docstring_type

    def _add_optional_and_default_value_template_representation(
        self,
        *,
        optional: bool = True,
        default_value_declaration: Optional[str] = None,
        description: Optional[str] = None,
    ):
        comment = ""
        if optional:
            comment += " Optional."
        if default_value_declaration:
            comment += f" Default value is {default_value_declaration}."
        else:
            default_value_declaration = self.default_template_representation_declaration
        if description:
            comment += f" {description}"
        if comment:
            comment = f"#{comment}"
        return f"{default_value_declaration}{comment}"

    def get_json_template_representation(self, **kwargs: Any) -> Any:
        if self.default_value:
            kwargs["default_value_declaration"] = kwargs.get(
                "default_value_declaration",
                self.get_declaration(self.default_value)
            )
        return self._add_optional_and_default_value_template_representation(
            **kwargs
        )

    @property
    def default_template_representation_declaration(self) -> str:
        return self.get_declaration(self.docstring_type)

class IOSchema(PrimitiveSchema):

    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel") -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.type = "IO"

    @property
    def serialization_type(self) -> str:
        return self.type

    @property
    def docstring_type(self) -> str:
        return self.type

    def type_annotation(self, *, is_operation_file: bool = False) -> str:  # pylint: disable=unused-argument
        return self.docstring_type

    @property
    def docstring_text(self) -> str:
        return "IO"

    @property
    def default_template_representation_declaration(self) -> str:
        return self.get_declaration(b"bytes")

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.add_submodule_import("typing", "IO", ImportType.STDLIB, TypingSection.CONDITIONAL)
        return file_import

class AnySchema(PrimitiveSchema):
    @property
    def serialization_type(self) -> str:
        return "object"

    @property
    def docstring_type(self) -> str:
        return "any"

    def type_annotation(self, *, is_operation_file: bool = False) -> str:  # pylint: disable=unused-argument
        return "Any"

    @property
    def default_template_representation_declaration(self) -> str:
        return self.get_declaration({})

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.add_submodule_import("typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL)
        return file_import

class NumberSchema(PrimitiveSchema):
    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel") -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
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

    def type_annotation(self, *, is_operation_file: bool = False) -> str:  # pylint: disable=unused-argument
        python_type = self.docstring_type
        if python_type == "long":
            return "int"
        return python_type

    @property
    def default_template_representation_declaration(self) -> str:
        default_value = 0 if self.docstring_type == "int" else 0.0
        return self.get_declaration(default_value)

class StringSchema(PrimitiveSchema):

    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel") -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.max_length = cast(int, yaml_data.get("maxLength"))
        self.min_length = cast(
            int, (yaml_data.get("minLength", 0) if yaml_data.get("maxLength") else yaml_data.get("minLength"))
        )
        self.pattern = cast(str, yaml_data.get("pattern"))

    @property
    def serialization_constraints(self) -> List[str]:
        validation_constraints = [
            f"max_length={self.max_length}" if self.max_length is not None else None,
            f"min_length={self.min_length}" if self.min_length is not None else None,
            f"pattern={RawString(self.pattern)}" if self.pattern else None,
        ]
        return [x for x in validation_constraints if x is not None]

    @property
    def validation_map(self) -> Optional[Dict[str, Union[bool, int, str]]]:
        validation_map: Dict[str, Union[bool, int, str]] = {}
        if self.max_length is not None:
            validation_map["max_length"] = self.max_length
        if self.min_length is not None:
            validation_map["min_length"] = self.min_length
        if self.pattern:
            # https://github.com/Azure/autorest.python/issues/407
            validation_map["pattern"] = RawString(self.pattern)  # type: ignore
        return validation_map or None

    def get_declaration(self, value) -> str:
        return f'"{value}"'


class DatetimeSchema(PrimitiveSchema):
    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel") -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
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
        return "~" + self.type_annotation()

    def type_annotation(self, *, is_operation_file: bool = False) -> str:  # pylint: disable=unused-argument
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

    @property
    def default_template_representation_declaration(self):
        return self.get_declaration(datetime.datetime(2020, 2, 20))

class TimeSchema(PrimitiveSchema):
    @property
    def serialization_type(self) -> str:
        return "time"

    @property
    def docstring_type(self) -> str:
        return "~" + self.type_annotation()

    def type_annotation(self, *, is_operation_file: bool = False) -> str:  # pylint: disable=unused-argument
        return "datetime.time"

    @property
    def docstring_text(self) -> str:
        return "time"

    def get_declaration(self, value: datetime.time) -> str:
        """Could be discussed, since technically I should return a time object,
        but msrest will do fine.
        """
        return f'"{value}"'

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.add_import("datetime", ImportType.STDLIB)
        return file_import

    @property
    def default_template_representation_declaration(self) -> str:
        return self.get_declaration(datetime.time(12, 30, 0))


class UnixTimeSchema(PrimitiveSchema):
    @property
    def serialization_type(self) -> str:
        return "unix-time"

    @property
    def docstring_type(self) -> str:
        return "~" + self.type_annotation()

    def type_annotation(self, *, is_operation_file: bool = False) -> str:  # pylint: disable=unused-argument
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

    @property
    def default_template_representation_declaration(self) -> str:
        return self.get_declaration(datetime.datetime(2020, 2, 20))


class DateSchema(PrimitiveSchema):
    @property
    def serialization_type(self) -> str:
        return "date"

    @property
    def docstring_type(self) -> str:
        return "~" + self.type_annotation()

    def type_annotation(self, *, is_operation_file: bool = False) -> str:  # pylint: disable=unused-argument
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

    @property
    def default_template_representation_declaration(self) -> str:
        return self.get_declaration(datetime.date(2020, 2, 20))


class DurationSchema(PrimitiveSchema):
    @property
    def serialization_type(self) -> str:
        return "duration"

    @property
    def docstring_type(self) -> str:
        return "~" + self.type_annotation()

    def type_annotation(self, *, is_operation_file: bool = False) -> str:  # pylint: disable=unused-argument
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

    @property
    def default_template_representation_declaration(self) -> str:
        return self.get_declaration(datetime.timedelta(1))


class ByteArraySchema(PrimitiveSchema):
    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel") -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
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


def get_primitive_schema(yaml_data: Dict[str, Any], code_model: "CodeModel") -> "PrimitiveSchema":
    mapping = {
        "integer": NumberSchema,
        "number": NumberSchema,
        "string": StringSchema,
        "char": StringSchema,
        "date-time": DatetimeSchema,
        "time": TimeSchema,
        "unixtime": UnixTimeSchema,
        "date": DateSchema,
        "duration": DurationSchema,
        "byte-array": ByteArraySchema,
        "any": AnySchema,
        "any-object": AnySchema,
        "binary": IOSchema
    }
    schema_type = yaml_data["type"]
    primitive_schema = cast(
        PrimitiveSchema, mapping.get(schema_type, PrimitiveSchema).from_yaml(yaml_data=yaml_data, code_model=code_model)
    )
    return primitive_schema
