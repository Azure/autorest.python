# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union, TYPE_CHECKING

from .base import BaseType
from .imports import FileImport, ImportType, TypingSection
from .utils import add_to_description

if TYPE_CHECKING:
    from .code_model import CodeModel


class RawString(object):
    def __init__(self, string: str) -> None:
        self.string = string

    def __repr__(self) -> str:
        return "r'{}'".format(self.string.replace("'", "\\'"))


class PrimitiveType(BaseType):  # pylint: disable=abstract-method
    def description(
        self, *, is_operation_file: bool  # pylint: disable=unused-argument
    ) -> str:
        return ""

    def type_annotation(self, **kwargs: Any) -> str:
        return self.docstring_type(**kwargs)

    def docstring_text(self, **kwargs: Any) -> str:
        return self.docstring_type()

    def get_json_template_representation(
        self,
        *,
        optional: bool = True,
        client_default_value_declaration: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Any:
        comment = ""
        if optional:
            comment = add_to_description(comment, "Optional.")
        if self.client_default_value is not None:
            client_default_value_declaration = (
                client_default_value_declaration
                or self.get_declaration(self.client_default_value)
            )
        if client_default_value_declaration:
            comment = add_to_description(
                comment, f"Default value is {client_default_value_declaration}."
            )
        else:
            client_default_value_declaration = (
                self.default_template_representation_declaration
            )
        if description:
            comment = add_to_description(comment, description)
        if comment:
            comment = f"# {comment}"
        return f"{client_default_value_declaration}{comment}"

    @property
    def default_template_representation_declaration(self) -> str:
        return self.get_declaration(self.docstring_type())


class BooleanType(PrimitiveType):
    @property
    def serialization_type(self) -> str:
        return "bool"

    def docstring_type(self, **kwargs: Any) -> str:
        return "bool"

    @property
    def instance_check_template(self) -> str:
        return "isinstance({}, bool)"


class BinaryType(PrimitiveType):
    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel") -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.type = "IO"

    @property
    def serialization_type(self) -> str:
        return self.type

    def docstring_type(self, **kwargs: Any) -> str:
        return self.type

    def type_annotation(self, **kwargs: Any) -> str:
        return self.docstring_type(**kwargs)

    def docstring_text(self, **kwargs: Any) -> str:
        return "IO"

    @property
    def default_template_representation_declaration(self) -> str:
        return self.get_declaration(b"bytes")

    def imports(self, **kwargs: Any) -> FileImport:
        file_import = FileImport()
        file_import.add_submodule_import("typing", "IO", ImportType.STDLIB)
        return file_import

    @property
    def instance_check_template(self) -> str:
        return "isinstance({}, (IO, bytes))"


class BinaryIteratorType(PrimitiveType):
    """Type returned by response if response is a streamed response"""

    @property
    def serialization_type(self) -> str:
        return "IO"

    def docstring_type(self, **kwargs: Any) -> str:
        return "AsyncIterator[bytes]" if kwargs.get("async_mode") else "Iterator[bytes]"

    def type_annotation(self, **kwargs: Any) -> str:
        return self.docstring_type(**kwargs)

    def docstring_text(self, **kwargs: Any) -> str:
        iterator = "Async iterator" if kwargs.get("async_mode") else "Iterator"
        return f"{iterator} of the response bytes"

    @property
    def default_template_representation_declaration(self) -> str:
        return self.get_declaration(f"Iterator[bytes]")

    def imports(self, **kwargs: Any) -> FileImport:
        file_import = FileImport()
        iterator = "AsyncIterator" if kwargs.get("async_mode") else "Iterator"
        file_import.add_submodule_import("typing", iterator, ImportType.STDLIB)
        return file_import

    @property
    def instance_check_template(self) -> str:
        return "isinstance({}, Iterator)"


class AnyType(PrimitiveType):
    @property
    def serialization_type(self) -> str:
        return "object"

    def docstring_type(self, **kwargs: Any) -> str:
        return "any"

    def type_annotation(self, **kwargs: Any) -> str:
        return "Any"

    @property
    def default_template_representation_declaration(self) -> str:
        return self.get_declaration({})

    def imports(self, **kwargs: Any) -> FileImport:
        file_import = FileImport()
        file_import.add_submodule_import(
            "typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        return file_import

    @property
    def instance_check_template(self) -> str:
        raise ValueError(
            "Shouldn't do instance check on an anytype, it can be anything"
        )


class AnyObjectType(PrimitiveType):
    @property
    def serialization_type(self) -> str:
        return "object"

    def docstring_type(self, **kwargs: Any) -> str:
        return "JSON"

    def type_annotation(self, **kwargs: Any) -> str:
        return "JSON"

    @property
    def default_template_representation_declaration(self) -> str:
        return self.get_declaration({})

    @property
    def instance_check_template(self) -> str:
        return "isinstance({}, MutableMapping)"

    def imports(self, **kwargs: Any) -> FileImport:
        file_import = FileImport()
        file_import.define_mutable_mapping_type()
        return file_import


class NumberType(PrimitiveType):  # pylint: disable=abstract-method
    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel") -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.precision: Optional[int] = yaml_data.get("precision")
        self.multiple: Optional[int] = yaml_data.get("multipleOf")
        self.maximum: Optional[int] = yaml_data.get("maximum")
        self.minimum: Optional[int] = yaml_data.get("minimum")
        self.exclusive_maximum: Optional[int] = yaml_data.get("exclusiveMaximum")
        self.exclusive_minimum: Optional[int] = yaml_data.get("exclusiveMinimum")

    @property
    def serialization_constraints(self) -> List[str]:
        validation_constraints = [
            f"maximum_ex={self.maximum}"
            if self.maximum is not None and self.exclusive_maximum
            else None,
            f"maximum={self.maximum}"
            if self.maximum is not None and not self.exclusive_maximum
            else None,
            f"minimum_ex={self.minimum}"
            if self.minimum is not None and self.exclusive_minimum
            else None,
            f"minimum={self.minimum}"
            if self.minimum is not None and not self.exclusive_minimum
            else None,
            f"multiple={self.multiple}" if self.multiple else None,
        ]
        return [x for x in validation_constraints if x is not None]

    @property
    def validation(self) -> Optional[Dict[str, Union[bool, int, str]]]:
        validation: Dict[str, Union[bool, int, str]] = {}
        if self.maximum is not None:
            if self.exclusive_maximum:
                validation["maximum_ex"] = self.maximum
            else:
                validation["maximum"] = self.maximum
        if self.minimum is not None:
            if self.exclusive_minimum:
                validation["minimum_ex"] = self.minimum
            else:
                validation["minimum"] = self.minimum
        if self.multiple:
            validation["multiple"] = self.multiple
        return validation or None

    @property
    def default_template_representation_declaration(self) -> str:
        default_value = 0 if self.docstring_type() == "int" else 0.0
        return self.get_declaration(default_value)


class IntegerType(NumberType):
    @property
    def serialization_type(self) -> str:
        return "int"

    def docstring_type(self, **kwargs: Any) -> str:
        return "int"

    def type_annotation(self, **kwargs: Any) -> str:
        return "int"

    @property
    def default_template_representation_declaration(self) -> str:
        return self.get_declaration(0)

    @property
    def instance_check_template(self) -> str:
        return "isinstance({}, int)"


class FloatType(NumberType):
    @property
    def serialization_type(self) -> str:
        return "float"

    def docstring_type(self, **kwargs: Any) -> str:
        return "float"

    def type_annotation(self, **kwargs: Any) -> str:
        return "float"

    @property
    def default_template_representation_declaration(self) -> str:
        return self.get_declaration(0.0)

    @property
    def instance_check_template(self) -> str:
        return "isinstance({}, float)"


class StringType(PrimitiveType):
    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel") -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.max_length: Optional[int] = yaml_data.get("maxLength")
        self.min_length: Optional[int] = (
            yaml_data.get("minLength", 0)
            if yaml_data.get("maxLength")
            else yaml_data.get("minLength")
        )
        self.pattern: Optional[str] = yaml_data.get("pattern")

    @property
    def serialization_constraints(self) -> List[str]:
        validation_constraints = [
            f"max_length={self.max_length}" if self.max_length is not None else None,
            f"min_length={self.min_length}" if self.min_length is not None else None,
            f"pattern={RawString(self.pattern)}" if self.pattern else None,
        ]
        return [x for x in validation_constraints if x is not None]

    @property
    def validation(self) -> Optional[Dict[str, Union[bool, int, str]]]:
        validation: Dict[str, Union[bool, int, str]] = {}
        if self.max_length is not None:
            validation["max_length"] = self.max_length
        if self.min_length is not None:
            validation["min_length"] = self.min_length
        if self.pattern:
            # https://github.com/Azure/autorest.python/issues/407
            validation["pattern"] = RawString(self.pattern)  # type: ignore
        return validation or None

    def get_declaration(self, value) -> str:
        return f'"{value}"'

    @property
    def serialization_type(self) -> str:
        return "str"

    def docstring_type(self, **kwargs: Any) -> str:
        return "str"

    @property
    def instance_check_template(self) -> str:
        return "isinstance({}, str)"


class DatetimeType(PrimitiveType):
    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel") -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.format = self.Formats(yaml_data["format"])

    class Formats(str, Enum):
        datetime = "date-time"
        rfc1123 = "date-time-rfc1123"

    @property
    def serialization_type(self) -> str:
        formats_to_attribute_type = {
            self.Formats.datetime: "iso-8601",
            self.Formats.rfc1123: "rfc-1123",
        }
        return formats_to_attribute_type[self.format]

    def docstring_type(self, **kwargs: Any) -> str:
        return "~" + self.type_annotation()

    def type_annotation(self, **kwargs: Any) -> str:
        return "datetime.datetime"

    def docstring_text(self, **kwargs: Any) -> str:
        return "datetime"

    def get_declaration(self, value: datetime.datetime) -> str:
        """Could be discussed, since technically I should return a datetime object,
        but msrest will do fine.
        """
        return f'"{value}"'

    def imports(self, **kwargs: Any) -> FileImport:
        file_import = FileImport()
        file_import.add_import("datetime", ImportType.STDLIB)
        return file_import

    @property
    def default_template_representation_declaration(self):
        return self.get_declaration(datetime.datetime(2020, 2, 20))

    @property
    def instance_check_template(self) -> str:
        return "isinstance({}, datetime.datetime)"


class TimeType(PrimitiveType):
    @property
    def serialization_type(self) -> str:
        return "time"

    def docstring_type(self, **kwargs: Any) -> str:
        return "~" + self.type_annotation()

    def type_annotation(self, **kwargs: Any) -> str:
        return "datetime.time"

    def docstring_text(self, **kwargs: Any) -> str:
        return "time"

    def get_declaration(self, value: datetime.time) -> str:
        """Could be discussed, since technically I should return a time object,
        but msrest will do fine.
        """
        return f'"{value}"'

    def imports(self, **kwargs: Any) -> FileImport:
        file_import = FileImport()
        file_import.add_import("datetime", ImportType.STDLIB)
        return file_import

    @property
    def default_template_representation_declaration(self) -> str:
        return self.get_declaration(datetime.time(12, 30, 0))

    @property
    def instance_check_template(self) -> str:
        return "isinstance({}, datetime.time)"


class UnixTimeType(PrimitiveType):
    @property
    def serialization_type(self) -> str:
        return "unix-time"

    def docstring_type(self, **kwargs: Any) -> str:
        return "~" + self.type_annotation()

    def type_annotation(self, **kwargs: Any) -> str:
        return "datetime.datetime"

    def docstring_text(self, **kwargs: Any) -> str:
        return "datetime"

    def get_declaration(self, value: datetime.datetime) -> str:
        """Could be discussed, since technically I should return a datetime object,
        but msrest will do fine.
        """
        return f'"{value}"'

    def imports(self, **kwargs: Any) -> FileImport:
        file_import = FileImport()
        file_import.add_import("datetime", ImportType.STDLIB)
        return file_import

    @property
    def default_template_representation_declaration(self) -> str:
        return self.get_declaration(datetime.datetime(2020, 2, 20))

    @property
    def instance_check_template(self) -> str:
        return "isinstance({}, datetime.time)"


class DateType(PrimitiveType):
    @property
    def serialization_type(self) -> str:
        return "date"

    def docstring_type(self, **kwargs: Any) -> str:
        return "~" + self.type_annotation()

    def type_annotation(self, **kwargs: Any) -> str:
        return "datetime.date"

    def docstring_text(self, **kwargs: Any) -> str:
        return "date"

    def get_declaration(self, value: datetime.date) -> str:
        """Could be discussed, since technically I should return a datetime object,
        but msrest will do fine.
        """
        return f'"{value}"'

    def imports(self, **kwargs: Any) -> FileImport:
        file_import = FileImport()
        file_import.add_import("datetime", ImportType.STDLIB)
        return file_import

    @property
    def default_template_representation_declaration(self) -> str:
        return self.get_declaration(datetime.date(2020, 2, 20))

    @property
    def instance_check_template(self) -> str:
        return "isinstance({}, datetime.date)"


class DurationType(PrimitiveType):
    @property
    def serialization_type(self) -> str:
        return "duration"

    def docstring_type(self, **kwargs: Any) -> str:
        return "~" + self.type_annotation()

    def type_annotation(self, **kwargs: Any) -> str:
        return "datetime.timedelta"

    def docstring_text(self, **kwargs: Any) -> str:
        return "timedelta"

    def get_declaration(self, value: datetime.timedelta) -> str:
        """Could be discussed, since technically I should return a datetime object,
        but msrest will do fine.
        """
        return f'"{value}"'

    def imports(self, **kwargs: Any) -> FileImport:
        file_import = FileImport()
        file_import.add_import("datetime", ImportType.STDLIB)
        return file_import

    @property
    def default_template_representation_declaration(self) -> str:
        return self.get_declaration(datetime.timedelta(1))

    @property
    def instance_check_template(self) -> str:
        return "isinstance({}, datetime.timedelta)"


class ByteArraySchema(PrimitiveType):
    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel") -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.format = yaml_data["format"]

    @property
    def serialization_type(self) -> str:
        if self.format == "base64url":
            return "base64"
        return "bytearray"

    def docstring_type(self, **kwargs: Any) -> str:
        return "bytes"

    def get_declaration(self, value: str) -> str:
        return f'bytes("{value}", encoding="utf-8")'

    @property
    def instance_check_template(self) -> str:
        return "isinstance({}, bytes)"
