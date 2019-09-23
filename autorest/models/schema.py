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
from typing import Any, Dict, List

class ComposedProperty:
    """Represents a property / parameter of a composite type schema ready
    to be serialized in Python.

    :param str name: The name of the property
    :param str description: Description of the property
    :param str property_type: Type of variable of the property
    :param bool required: Whether the property is required
    :param bool readonly: Whether the property is readonly
    :param bool constant: Whether the property is a constant
    :param str default_value: The default value, if any of the property
    :returns: A ComposedProperty model of the property
    :rtype: ~autorest.models.schema.ComposedProperty
    """
    def __init__(
        self,
        name: str,
        description: str,
        property_type: str,
        **kwargs: "**Any"
    ) -> "ComposedProperty":
        self.name = name
        self.description = description
        self.property_type = property_type
        self.required = kwargs.pop('required', False)
        self.readonly = kwargs.pop('readonly', False)
        self.constant = kwargs.pop('constant', False)
        self.default_value = kwargs.pop('default_value', None)

    """Constructs the documentation string for a property

    :returns: The documentation string of the property
    :rtype: str
    """
    def get_property_documentation_string(self) -> str:
        if self.constant or self.readonly:
            doc_string = ":ivar {}:".format(self.name)
        else:
            doc_string = ":param {}:".format(self.name)
        if self.required:
            doc_string += " Required."

        description = self.description
        if description and description[-1] != ".":
            description += "."

        # documentation = self.documentation
        # if documentation:
        #     if documentation[-1] != ".":
        #         documentation += "."
        #     documentation += " Default value: " + self.default_value + " ."
        if description:
            doc_string += " " + description
        if self.default_value:
            doc_string += " Default value: \"" + self.default_value + "\"."
        # if documentation:
        #     doc_string += " " + documentation
        return doc_string

    """Returns a ComposedProperty from the dict object constructed from a yaml file.

    :param str name: The name of the property
    :param yaml_data: A representation of the schema of a property from a yaml file
    :type yaml_data: dict(str, str)
    :returns: A ComposedProperty
    :rtype: ~autorest.models.schema.ComposedProperty
    """
    @classmethod
    def from_yaml(cls, name: str, yaml_data: Dict[str, str]) -> "ComposedProperty":
        required = yaml_data['details']['default']['required']
        readonly = yaml_data['details']['default']['readOnly']
        constant = yaml_data['details']['default'].get('constant', False)
        property_type = yaml_data['schema']['type']
        if property_type == 'object':
            property_type = yaml_data['schema']['details']['default']['name']

        # what if list, dict

        return cls(
            name=name,
            description=yaml_data['details']['default']['description'].strip(),
            property_type=property_type,
            required=required,
            readonly=readonly,
            constant=constant,
            default_value=yaml_data['schema'].get('default')
        )


class CompositeType:
    """Represents a composite type schema ready to be serialized in Python.

    :param str name: The name of the composite type.
    :param str description: The description of the composite type.
    :param properties: the optional properties of the composite thpe.
    :type properties: dict(str, str)
    """
    def __init__(self, name: str, description: str, **kwargs: "**Any") -> "CompositeType":
        self.name = name
        self.description = description
        self.properties = kwargs.pop('properties', None)

    """Returns the properties of a CompositeType if they exist.

    :param yaml_data: a dictionary object representative of the yaml schema
    for the composite type.
    :type yaml_data: dict(str, str)
    :returns: a list of the properties of the composite type
    :rtype: list[~autorest.models.schema.ComposedProperty]
    """
    @classmethod
    def _create_properties(cls, yaml_data: Dict[str, str]) -> List["ComposedProperty"]:
        properties = []
        for k, v in yaml_data['properties'].items():
            properties.append(ComposedProperty.from_yaml(k, v))
        # properties.sort(key=lambda item: (not(item.readonly or item.constant), item.name))
        if not properties:
            properties = None
        return properties

    """Returns a CompositeType from the dict object constructed from a yaml file.

    :param str name: The name of the composite type.
    :param yaml_data: A representation of the schema of a composite type from a yaml file.
    :type yaml_data: dict(str, str)
    :returns: A CompositeType.
    :rtype: ~autorest.models.schema.CompositeType
    """
    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str]) -> "CompositeType":
        # Returns a CompositeType from a yaml file
        name = yaml_data['details']['default']['name']
        description = yaml_data['details']['default']['description'].strip() or (name + ".")
        properties = cls._create_properties(yaml_data)
        return cls(
            name=name,
            description=description,
            properties=properties
        )