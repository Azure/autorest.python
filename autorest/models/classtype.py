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
from .basetype import BaseType
from typing import Any, Dict, List
from ..common.utils import to_python_type


class ClassType(BaseType):
    """Represents a class ready to be serialized in Python.

    :param str name: The name of the class.
    :param str description: The description of the class.
    :param properties: the optional properties of the class.
    :type properties: dict(str, str)
    """
    def __init__(self, name: str, description: str, **kwargs: "**Any") -> "ClassType":
        super(ClassType, self).__init__(name, description, **kwargs)
        self.properties = kwargs.pop('properties', None)
        self.base_model = kwargs.pop('base_model', None)
        self.property_type = kwargs.pop('property_type', None)
        self.property_documentation_string = None
        self.init_line = None
        self.init_args = None

    def get_attribute_map_type(self) -> str:
        return self.property_type

    def _get_property_type_from_yaml(yaml_data):
        property_type = yaml_data['type']
        if property_type == 'object':
            # TODO: make sure pure objects don't have $key entry
            if yaml_data.get('$ref'):
                # property is of a class in our yaml file
                return yaml_data['$ref']
            # if not, the property's type is just object
        return to_python_type(property_type)

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
    def _create_properties(cls, yaml_data: Dict[str, str], required_list: List[str]) -> List["Property"]:
        properties = []
        for name in yaml_data['properties']:
            from . import build_property
            properties.append(build_property(
                name=name,
                prop=yaml_data['properties'][name],
                required_list=required_list
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
        required_list = kwargs.pop('required_list', None)
        parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data,
            required_list=required_list
        )
        if yaml_data.get('properties'):
            # A class to be serialized
            properties = cls._create_properties(yaml_data=yaml_data, required_list=required_list)
            property_type = None
        else:
            # A property to be serialized
            properties = None
            property_type = cls._get_property_type_from_yaml(yaml_data=yaml_data)
        return cls(
            name=name,
            description=parameters_dict['description'],
            properties=properties,
            base_model=yaml_data['allOf'][0] if yaml_data.get('allOf') else None,
            property_type=property_type,
            required=parameters_dict['required'],
            readonly=parameters_dict['readonly'],
            constant=parameters_dict['constant']
        )
