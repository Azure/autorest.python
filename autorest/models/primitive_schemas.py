from enum import Enum
from .base_schema import BaseSchema
from ..common.utils import to_python_type

class PrimitiveSchema(BaseSchema):
    def __init__(self, yaml_data, name, schema_type, **kwargs):
        super(PrimitiveSchema, self).__init__(yaml_data, name,**kwargs)
        self.schema_type = to_python_type(schema_type)

    @classmethod
    def from_yaml(cls, name, yaml_data, schema_type, original_swagger_name):
        return cls(
            yaml_data=yaml_data,
            name=name,
            schema_type=schema_type,
            original_swagger_name=original_swagger_name,
        )

    def get_serialization_type(self):
        return self.schema_type

    def get_doc_string_type(self, namespace=None):
        return self.schema_type


class NumberSchema(PrimitiveSchema):
    def __init__(self, yaml_data, name, schema_type, precision, **kwargs):
        super(NumberSchema, self).__init__(yaml_data, name, schema_type, **kwargs)
        self.precision = precision
        self.multiple_of = kwargs.pop('multiple_of', None)
        self.maximum = kwargs.pop('maximum', None)
        self.minimum = kwargs.pop('minimum', None)
        self.exclusive_maximum = kwargs.pop('exclusive_maximum', None)
        self.exclusive_minimum = kwargs.pop('exclusive_minimum', None)

    @classmethod
    def from_yaml(cls, name, yaml_data, schema_type, original_swagger_name):
        return cls(
            yaml_data=yaml_data,
            name=name,
            schema_type=schema_type,
            precision=yaml_data['precision'],
            original_swagger_name=original_swagger_name,
            multiple_of = yaml_data.get('multipleOf'),
            maximum=yaml_data.get('maximum'),
            minimum=yaml_data.get('minimum'),
            exclusive_maximum=yaml_data.get('exclusiveMaximum'),
            exclusive_minimum=yaml_data.get('exclusiveMinimum'),
        )

class StringSchema(PrimitiveSchema):
    def __init__(self, yaml_data, name, schema_type, **kwargs):
        super(StringSchema, self).__init__(yaml_data, name, schema_type, **kwargs)
        self.max_length = kwargs.pop('max_length', None)
        self.min_length = kwargs.pop('min_length', None)
        self.pattern = kwargs.pop('pattern', None)

    @classmethod
    def from_yaml(cls, name, yaml_data, original_swagger_name):
        return cls(
            yaml_data=yaml_data,
            name=name,
            schema_type='string',
            max_length=yaml_data.get('maxLength'),
            min_length=yaml_data.get('minLength'),
            pattern=yaml_data.get('pattern'),
            original_swagger_name=original_swagger_name
        )


class DatetimeSchema(PrimitiveSchema):
    def __init__(self, yaml_data, name, schema_type, format, **kwargs):
        super(DatetimeSchema, self).__init__(yaml_data, name, schema_type, **kwargs)
        self.format = format

    class Formats(str, Enum):
        datetime = "date-time"
        rfc1123 = "date-time-rfc1123"

    def get_serialization_type(self):
        formats_to_attribute_type = {
            self.Formats.datetime: "iso-8601",
            self.Formats.rfc1123: "rfc-1123"
        }
        return formats_to_attribute_type[self.format]

    @classmethod
    def from_yaml(cls, name, yaml_data, schema_type, original_swagger_name):
        return cls(
            yaml_data=yaml_data,
            name=name,
            schema_type=schema_type,
            format=cls.Formats(yaml_data['format']),
            original_swagger_name=original_swagger_name
        )


class ByteArraySchema(PrimitiveSchema):
    def __init__(self, yaml_data, name, schema_type, format, **kwargs):
        super(ByteArraySchema, self).__init__(yaml_data, name, schema_type, **kwargs)
        self.format = format

    class Formats(str, Enum):
        base64url = "base64url"
        byte = "byte"

    @classmethod
    def from_yaml(cls, name, yaml_data, original_swagger_name):
        return cls(
            yaml_data=yaml_data,
            name=name,
            schema_type='byte-array',
            format=cls.Formats(yaml_data['format']),
            original_swagger_name=original_swagger_name
        )

def get_primitive_schema(name, yaml_data, original_swagger_name):
    schema_type = yaml_data['type']
    if schema_type in ('integer', 'number'):
        return NumberSchema.from_yaml(
            name=name,
            yaml_data=yaml_data,
            schema_type=schema_type,
            original_swagger_name=original_swagger_name
        )
    if schema_type == 'string':
        return StringSchema.from_yaml(
            name=name,
            yaml_data=yaml_data,
            original_swagger_name=original_swagger_name
        )
    if schema_type == 'date-time':
        return DatetimeSchema.from_yaml(
            name=name,
            yaml_data=yaml_data,
            schema_type=schema_type,
            original_swagger_name=original_swagger_name
        )
    if schema_type  == 'byte-array':
        return ByteArraySchema.from_yaml(
            name=name,
            yaml_data=yaml_data,
            original_swagger_name=original_swagger_name
        )
    return PrimitiveSchema.from_yaml(
        name=name,
        yaml_data=yaml_data,
        schema_type=schema_type,
        original_swagger_name=original_swagger_name
    )