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
import re
from .base_schema import BaseSchema
from .dictionary_schema import DictionarySchema
from typing import Any, Dict, List
from ..common.utils import to_python_type, get_property_name


class ObjectSchema(BaseSchema):
    """Represents a class ready to be serialized in Python.

    :param str name: The name of the class.
    :param str description: The description of the class.
    :param properties: the optional properties of the class.
    :type properties: dict(str, str)
    """
    def __init__(self, yaml_data, name: str, description: str, schema_type: str, **kwargs: "**Any") -> "ObjectSchema":
        super(ObjectSchema, self).__init__(yaml_data, name, description, **kwargs)
        self.schema_type = schema_type
        self.max_properties = kwargs.pop('max_properties', None)
        self.min_properties = kwargs.pop('min_properties', None)
        self.properties = kwargs.pop('properties', None)
        self.is_exception = kwargs.pop('is_exception', False)
        self.base_model = kwargs.pop('base_model', None)
        self.has_subclasses = kwargs.pop('has_subclasses', False)
        self.discriminator = kwargs.pop('discriminator', None)
        self.subtype_map = kwargs.pop('subtype_map', None)
        self.property_documentation_string = None
        self.init_line = None
        self.init_args = None

    def get_attribute_map_type(self) -> str:
        return self.schema_type

    def get_doc_string_type(self, namespace):
        if self.schema_type == 'object':
            return self.schema_type
        return '~{}.models.{}'.format(namespace, self.schema_type)

    @classmethod
    def _convert_to_class_name(cls, name):
        name_list = re.split('[^a-zA-Z\\d]', name)
        name_list = [s[0].upper() + s[1:] if len(s) > 1 else s.upper()
                            for s in name_list]
        return ''.join(name_list)

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
    def _create_properties(cls, yaml_data: Dict[str, str], has_additional_properties) -> List["Property"]:
        properties = []
        for prop in yaml_data:
            from . import build_schema
            name = get_property_name(prop['serializedName'])
            if name == 'additional_properties' and has_additional_properties:
                name = 'additional_properties1'
            properties.append(build_schema(
                name=name,
                yaml_data=prop,
                original_swagger_name=prop['serializedName']
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
        for_additional_properties = kwargs.pop("for_additional_properties", False)
        top_level = kwargs.pop("top_level", False)
        properties = []
        base_model = None

        # checking to see if there is a parent class and / or additional properties
        if yaml_data.get('parents'):
            immediate_parents = yaml_data['parents']['immediate']
        # checking if object has a parent
            if immediate_parents and immediate_parents[0]['language']['default']['name'] != yaml_data['language']['default']['name']:
                base_model = immediate_parents[0]['language']['default']['name']

            # this means that this class has additional properties defined on it
            if immediate_parents[0]['language']['default']['name'] == yaml_data['language']['default']['name'] and immediate_parents[0]['type'] == 'dictionary':
                properties.append(DictionarySchema.from_yaml(name="additional_properties", yaml_data=immediate_parents[0], for_additional_properties=True))

        # checking to see if this is a polymorphic class
        discriminator = None
        subtype_map = {}
        if yaml_data.get('discriminator'):
            discriminator = yaml_data['discriminator']['property']['language']['default']['name']

            # map of discriminator value to child's name
            for children_name, children_yaml in yaml_data['discriminator']['immediate'].items():
                subtype_map[children_yaml['discriminatorValue']] = cls._convert_to_class_name(children_name)

        schema_type = None
        if top_level and yaml_data.get('properties'):
            properties += cls._create_properties(yaml_data=yaml_data.get('properties', []), has_additional_properties=len(properties) > 0)

        # this is to ensure that the attribute map type and property type are generated correctly
        elif for_additional_properties:
            schema_type = yaml_data['type']
        else:
            schema_data = yaml_data['schema'] if yaml_data.get('schema') else yaml_data
            schema_type = schema_data['type']
            if schema_type == 'object':
                schema_type = cls._convert_to_class_name(schema_data['language']['default']['name'])

        if top_level:
            name = cls._convert_to_class_name(name)
        common_parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data
        )
        is_exception = None
        exceptions_set = kwargs.pop('exceptions_set', None)
        if exceptions_set:
            if yaml_data['language']['default']['name'] in exceptions_set:
                is_exception = True
        return cls(
            yaml_data=yaml_data,
            name=name,
            description=common_parameters_dict['description'],
            schema_type=schema_type,
            properties=properties,
            base_model=base_model,
            required=common_parameters_dict['required'],
            readonly=common_parameters_dict['readonly'],
            constant=common_parameters_dict['constant'],
            is_discriminator=common_parameters_dict['is_discriminator'],
            discriminator_value = common_parameters_dict['discriminator_value'],
            default_value=yaml_data['schema'].get('defaultValue') if yaml_data.get('schema') else None,
            original_swagger_name=kwargs.pop('original_swagger_name', yaml_data['language']['default']['name']),
            is_exception=is_exception,
            discriminator=discriminator,
            subtype_map=subtype_map if subtype_map else None
        )
