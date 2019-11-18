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
from .imports import FileImport, ImportType
from .property import Property
from typing import Any, Dict, List


class ObjectSchema(BaseSchema):
    """Represents a class ready to be serialized in Python.

    :param str name: The name of the class.
    :param str description: The description of the class.
    :param properties: the optional properties of the class.
    :type properties: dict(str, str)
    """
    def __init__(self, yaml_data, name: str, description=None, **kwargs: "**Any") -> "ObjectSchema":
        super(ObjectSchema, self).__init__(yaml_data, **kwargs)
        self.name = name
        self.description = description
        self.max_properties = kwargs.pop('max_properties', None)
        self.min_properties = kwargs.pop('min_properties', None)
        self.properties = kwargs.pop('properties', None)
        self.is_exception = kwargs.pop('is_exception', False)
        self.base_model = kwargs.pop('base_model', None)
        self.subtype_map = kwargs.pop('subtype_map', None)
        self.discriminator_name = kwargs.pop('discriminator_name', None)
        self.discriminator_value = kwargs.pop('discriminator_value', None)
        self.property_documentation_string = None
        self.init_line = None
        self.init_args = None

    def imports(self):
        file_import = FileImport()
        file_import.add_from_import("msrest.serialization", "Model", ImportType.AZURECORE)
        if self.is_exception:
            file_import.add_from_import("azure.core.exceptions", "HttpResponseError", ImportType.AZURECORE)
        return file_import

    def get_serialization_type(self) -> str:
        return self.name

    def get_python_type_annotation(self) -> str:
        return f'\"{self.name}\"'

    def get_python_type(self, namespace):
        return '~{}.models.{}'.format(namespace, self.name)


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
    @staticmethod
    def _create_properties(yaml_data: Dict[str, str], has_additional_properties, **kwargs) -> List["Property"]:
        properties = []
        for p in yaml_data:
            from . import build_schema
            name = get_property_name(p['serializedName'])
            if name == 'additional_properties' and has_additional_properties:
                name = 'additional_properties1'

            schema = build_schema(
                yaml_data=p['schema'],
                **kwargs
            )
            properties.append(
                Property(
                    name=name,
                    schema=schema,
                    original_swagger_name=p['serializedName'],
                    property_data=p
                )
            )
        return properties


    """Returns a ClassType from the dict object constructed from a yaml file.

    WARNING: This guy might create an infinite loop.

    :param str name: The name of the class type.
    :param yaml_data: A representation of the schema of a class type from a yaml file.
    :type yaml_data: dict(str, str)
    :returns: A ClassType.
    :rtype: ~autorest.models.schema.ClassType
    """
    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str], **kwargs) -> "ClassType":
        obj = cls(yaml_data, None, None, None)
        return obj.fill_instance_from_yaml(yaml_data)

    def fill_instance_from_yaml(self, yaml_data: Dict[str, str], **kwargs) -> None:
        for_additional_properties = kwargs.pop("for_additional_properties", False)
        properties = []
        base_model = None

        # checking to see if there is a parent class and / or additional properties
        if yaml_data.get('parents'):
            immediate_parents = yaml_data['parents']['immediate']
        # checking if object has a parent
            if immediate_parents and immediate_parents[0]['language']['python']['name'] != yaml_data['language']['python']['name']:
                base_model = id(immediate_parents[0])

            # this means that this class has additional properties defined on it
            if immediate_parents[0]['language']['python']['name'] == yaml_data['language']['python']['name'] and immediate_parents[0]['type'] == 'dictionary':
                additional_properties_schema = DictionarySchema.from_yaml(
                        yaml_data=immediate_parents[0],
                        for_additional_properties=True,
                        **kwargs
                    )
                properties.append(
                    Property(
                        name="additional_properties",
                        schema=additional_properties_schema,
                        original_swagger_name="",
                        property_data={},
                        description='Unmatched properties from the message are deserialized to this collection.'
                    )
                )

        # checking to see if this is a polymorphic class
        subtype_map = None
        if yaml_data.get('discriminator'):
            subtype_map = {}
            # map of discriminator value to child's name
            for children_yaml in yaml_data['discriminator']['immediate'].values():
                subtype_map[children_yaml['discriminatorValue']] = children_yaml['language']['python']['name']

        if yaml_data.get('properties'):
            properties += self._create_properties(
                yaml_data=yaml_data.get('properties', []),
                has_additional_properties=len(properties) > 0,
                **kwargs
            )
        # this is to ensure that the attribute map type and property type are generated correctly

        name = yaml_data['language']['python']['name']

        description = None
        description = yaml_data['language']['python']['description'].strip()
        if description == 'MISSING-SCHEMA-DESCRIPTION-OBJECTSCHEMA':
            description = name + "."
        elif 'MISSING' in description:
            description = ""
        is_exception = None
        exceptions_set = kwargs.pop('exceptions_set', None)
        if exceptions_set:
            if yaml_data['language']['python']['name'] in exceptions_set:
                is_exception = True


        self.yaml_data=yaml_data
        self.name=name
        self.description=description
        self.properties=properties
        self.base_model=base_model
        self.is_exception=is_exception
        self.subtype_map=subtype_map
        self.discriminator_name = yaml_data['discriminator']['property']['language']['python']['name'] if yaml_data.get('discriminator') else None
        self.discriminator_value = yaml_data.get('discriminatorValue', None)
