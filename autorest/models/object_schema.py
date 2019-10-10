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
from ..common.utils import to_python_type, get_property_name


class ObjectSchema(BaseSchema):
    """Represents a class ready to be serialized in Python.

    :param str name: The name of the class.
    :param str description: The description of the class.
    :param properties: the optional properties of the class.
    :type properties: dict(str, str)
    """
    def __init__(self, name: str, description: str, schema_type: str, id, **kwargs: "**Any") -> "ObjectSchema":
        super(ObjectSchema, self).__init__(name, description, id, **kwargs)
        self.schema_type = schema_type
        self.max_properties = kwargs.pop('max_properties', None)
        self.min_properties = kwargs.pop('min_properties', None)
        self.properties = kwargs.pop('properties', None)
        self.is_exception = kwargs.pop('is_exception', False)
        self.has_additional_properties = kwargs.pop('has_additional_properties', False)
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
                name=get_property_name(prop['serializedName']),
                yaml_data=prop,
                serialize_name=prop['serializedName']
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
        base_model = None
        has_additional_properties = False

        # this is then a top level schema from the and list in yaml_data
        if yaml_data.get('allOf'):
            # this is the object we want to generate as itself
            if yaml_data['$key'] == yaml_data['allOf'][0]['$key']:
                if len(yaml_data['allOf']) > 1:
                    # object has additional properties defined on it
                    if yaml_data['allOf'][1]['type'] == 'dictionary':
                        has_additional_properties = True

                    # object has a parent then
                    else:
                        base_model = yaml_data['allOf'][1]['$key']

                        # if there is another entry in the allOf, then this objects
                        # has both a parent and additional_properties defined on it
                        if len(yaml_data['allOf']) > 2:
                            has_additional_properties = True

                yaml_data = yaml_data['allOf'][0]

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
        is_exception = None
        exceptions_set = kwargs.pop('exceptions_set', None)
        if exceptions_set:
            if yaml_data['$key'] in exceptions_set:
                is_exception = True
        return cls(
            name=name,
            description=common_parameters_dict['description'],
            id=common_parameters_dict['id'],
            schema_type=schema_type,
            properties=properties,
            base_model=base_model,
            required=common_parameters_dict['required'],
            readonly=common_parameters_dict['readonly'],
            constant=common_parameters_dict['constant'],
            default_value=yaml_data['schema'].get('defaultValue') if yaml_data.get('schema') else None,
            serialize_name=kwargs.pop('serialize_name', None),
            is_exception=is_exception,
            has_additional_properties=has_additional_properties
        )
