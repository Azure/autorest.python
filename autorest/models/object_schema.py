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
from .base_schema import BaseSchema
from typing import Any, Dict, List
from ..common.utils import to_python_type


class ObjectSchema(BaseSchema):
    """Represents a class ready to be serialized in Python.

    :param str name: The name of the class.
    :param str description: The description of the class.
    :param properties: the optional properties of the class.
    :type properties: dict(str, str)
    """
    def __init__(self, name: str, description: str, schema_type: str, **kwargs: "**Any") -> "ObjectSchema":
        super(ObjectSchema, self).__init__(name, description, **kwargs)
        self.schema_type = schema_type
        self.max_properties = kwargs.pop('max_properties', None)
        self.min_properties = kwargs.pop('min_properties', None)
        self.properties = kwargs.pop('properties', None)
        self.base_model = kwargs.pop('base_model', None)
        self.property_documentation_string = None
        self.init_line = None
        self.init_args = None

    def get_attribute_map_type(self) -> str:
        return self.schema_type

    """Returns the properties of a ClassType if they exist.

    :param yaml_data: a dictionary object representative of the yaml schema
    for the class type.
    :type yaml_data: dict(str, str)
    :returns: a list of the properties of the class type
    :rtype: list[~autorest.models.Property or
     ~autorest.models.DictionaryType or
     ~autorest.models.SequenceType or
     ~autorest.models.EnumType]
    """
    @classmethod
    def _create_properties(cls, yaml_data: Dict[str, str]) -> List["Property"]:
        properties = []
        for prop in yaml_data:
            from . import build_schema
            properties.append(build_schema(
                name=prop['serializedName'],
                yaml_data=prop
            ))
        return properties

    """Returns a ClassType from the dict object constructed from a yaml file.

    :param str name: The name of the class type.
    :param yaml_data: A representation of the schema of a class type from a yaml file.
    :type yaml_data: dict(str, str)
    :returns: A ClassType.
    :rtype: ~autorest.models.schema.ClassType
    """
    @classmethod
    def from_yaml(cls, name: str, yaml_data: Dict[str, str], **kwargs) -> "ClassType":
        # Returns a ClassType from a yaml file
        common_parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data
        )
        schema_type = yaml_data['schema']['type'] if yaml_data.get('schema') else yaml_data['type']
        if yaml_data.get('properties'):
            # A class with properties to be serialized
            properties = cls._create_properties(yaml_data=yaml_data['properties'])
        else:
            properties = []
        return cls(
            name=name,
            description=common_parameters_dict['description'],
            schema_type=schema_type,
            properties=properties,
            base_model=yaml_data['allOf'][0] if yaml_data.get('allOf') else None,
            required=common_parameters_dict['required'],
            readonly=common_parameters_dict['readonly'],
            constant=common_parameters_dict['constant']
        )
