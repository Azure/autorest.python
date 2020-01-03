# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from enum import Enum
from typing import Dict, Optional, Union

from .base_schema import BaseSchema


_LOGGER = logging.getLogger(__name__)


class PrimitiveSchema(BaseSchema):
    _TYPE_MAPPINGS = {
        "boolean": "bool",
    }

    def _to_python_type(self):
        return self._TYPE_MAPPINGS.get(self.yaml_data['type'], "str")

    def get_serialization_type(self):
        return self._to_python_type()

    def get_python_type(self, namespace=None):
        return self._to_python_type()


class AnySchema(PrimitiveSchema):
    def get_serialization_type(self):
        return 'object'

    def get_python_type(self, namespace=None):
        return 'object'


class NumberSchema(PrimitiveSchema):
    def __init__(self, yaml_data):
        super(NumberSchema, self).__init__(yaml_data)
        self.precision = yaml_data['precision']
        self.multiple = yaml_data.get('multipleOf')
        self.maximum = yaml_data.get('maximum')
        self.minimum = yaml_data.get('minimum')
        self.exclusive_maximum = yaml_data.get('exclusiveMaximum')
        self.exclusive_minimum = yaml_data.get('exclusiveMinimum')

    def get_serialization_constraints(self):
        validation_constraints = [
            f"maximum_ex={self.maximum}" if self.maximum is not None and self.exclusive_maximum else None,
            f"maximum={self.maximum}" if self.maximum is not None and not self.exclusive_maximum else None,
            f"minimum_ex={self.minimum}" if self.minimum is not None and self.exclusive_minimum else None,
            f"minimum={self.minimum}" if self.minimum is not None and not self.exclusive_minimum else None,
            f"multiple={self.multiple}" if self.multiple else None
        ]
        return [x for x in validation_constraints if x is not None]

    def get_validation_map(self) -> Optional[Dict[str, Union[int, bool]]]:
        validation_map = {}
        if self.maximum is not None:
            if self.exclusive_maximum:
                validation_map['maximum_ex'] = self.maximum
            else:
                validation_map['maximum'] = self.maximum
        if self.minimum is not None:
            if self.exclusive_minimum:
                validation_map['minimum_ex'] = self.minimum
            else:
                validation_map['minimum'] = self.minimum
        if self.multiple:
            validation_map['multiple'] = self.multiple
        return validation_map or None


    def get_serialization_type(self):
        if self.yaml_data['type'] == "integer":
            if self.precision == 64:
                return "long"
            return "int"
        return "float"

    def get_python_type(self, namespace=None):
        if self.yaml_data['type'] == "integer":
            if self.precision == 64:
                return "long"
            return "int"
        return "float"

    def get_python_type_annotation(self):
        python_type = self.get_python_type()
        if python_type == "long":
            return "int"
        return python_type


class StringSchema(PrimitiveSchema):
    def __init__(self, yaml_data):
        super(StringSchema, self).__init__(yaml_data)
        self.max_length = yaml_data.get('maxLength')
        self.min_length = yaml_data.get('minLength', 0) if yaml_data.get('maxLength') else yaml_data.get('minLength')
        self.pattern = yaml_data.get('pattern')

    def get_serialization_constraints(self):
        validation_constraints = [
            f"max_length={self.max_length}" if self.max_length is not None else None,
            f"min_length={self.min_length}" if self.min_length is not None else None,
            f"pattern=\'{self.pattern}\'" if self.pattern is not None else None
        ]
        return [x for x in validation_constraints if x is not None]

    def get_validation_map(self) -> Optional[Dict[str, Union[int, bool]]]:
        validation_map = {}
        if self.max_length is not None:
            validation_map['max_length'] = self.max_length
        if self.min_length is not None:
            validation_map['min_length'] = self.min_length
        if self.pattern is not None:
            validation_map['pattern'] = self.pattern
        return validation_map or None

    def get_declaration(self, value) -> str:
        return f'"{value}"'


class DatetimeSchema(PrimitiveSchema):
    def __init__(self, yaml_data):
        super(DatetimeSchema, self).__init__(yaml_data)
        self.format = self.Formats(yaml_data['format'])

    class Formats(str, Enum):
        datetime = "date-time"
        rfc1123 = "date-time-rfc1123"

    def get_serialization_type(self):
        formats_to_attribute_type = {
            self.Formats.datetime: "iso-8601",
            self.Formats.rfc1123: "rfc-1123"
        }
        return formats_to_attribute_type[self.format]

    def get_python_type(self, namespace=None):
        return "~"+self.get_python_type_annotation()

    def get_python_type_annotation(self):
        return "datetime.datetime"

    def get_declaration(self, value) -> str:
        """Could be discussed, since technically I should return a datetime object,
        but msrest will do fine.
        """
        return f'"{value}"'


class UnixTimeSchema(PrimitiveSchema):

    def get_serialization_type(self):
        return "unix-time"

    def get_python_type(self, namespace=None):
        return "~"+self.get_python_type_annotation()

    def get_python_type_annotation(self):
        return "datetime.datetime"

    def get_declaration(self, value) -> str:
        """Could be discussed, since technically I should return a datetime object,
        but msrest will do fine.
        """
        return f'"{value}"'


class DateSchema(PrimitiveSchema):

    def get_serialization_type(self):
        return "date"

    def get_python_type(self, namespace=None):
        return "~"+self.get_python_type_annotation()

    def get_python_type_annotation(self):
        return "datetime.date"

    def get_declaration(self, value) -> str:
        """Could be discussed, since technically I should return a datetime object,
        but msrest will do fine.
        """
        return f'"{value}"'


class DurationSchema(PrimitiveSchema):

    def get_serialization_type(self):
        return "duration"

    def get_python_type(self, namespace=None):
        return "~"+self.get_python_type_annotation()

    def get_python_type_annotation(self):
        return "datetime.timedelta"

    def get_declaration(self, value) -> str:
        """Could be discussed, since technically I should return a datetime object,
        but msrest will do fine.
        """
        return f'"{value}"'


class ByteArraySchema(PrimitiveSchema):
    def __init__(self, yaml_data):
        super(ByteArraySchema, self).__init__(yaml_data)
        self.format = self.Formats(yaml_data['format'])

    class Formats(str, Enum):
        base64url = "base64url"
        byte = "byte"

    def get_serialization_type(self):
        if self.format == ByteArraySchema.Formats.base64url:
            return "base64"
        return "bytearray"

    def get_python_type(self, namespace=None):
        return "bytearray"

    def get_declaration(self, value) -> str:
        return f'bytearray("{value}", encoding="utf-8")'


def get_primitive_schema(yaml_data):
    mapping = {
        'integer': NumberSchema,
        'number': NumberSchema,
        'string': StringSchema,
        'date-time': DatetimeSchema,
        'unixtime': UnixTimeSchema,
        'date': DateSchema,
        'duration': DurationSchema,
        'byte-array': ByteArraySchema,
        'any': AnySchema
    }
    schema_type = yaml_data['type']
    return mapping.get(schema_type, PrimitiveSchema).from_yaml(yaml_data=yaml_data)
