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


class ComposedProperty:
    """Represents a property of a CompositeType
    """
    def __init__(self, name, description, property_type, **kwargs):
        self.name = name
        self.description = description
        self.property_type = property_type
        self.required = kwargs.pop('required', False)
        self.readonly = kwargs.pop('readonly', False)
        self.constant = kwargs.pop('constant', False)
        self.default_value = kwargs.pop('default_value', None)

    def get_property_documentation_string(self):
        if not self:
            raise TypeError("Property can not be none.")
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


class CompositeType:
    """Represents a composite type schema ready to be serialized in Python.
    """
    def __init__(self, name, description, **kwargs):
        self.name = name
        self.description = description
        self.properties = kwargs.pop('properties', None)

    @classmethod
    def _create_properties(cls, yaml_data):
        # Returns the properties of a CompositeType.
        properties = []
        for k, v in yaml_data['properties'].items():
            required = v['details']['default']['required']
            readonly = v['details']['default']['readOnly']
            constant = v['details']['default'].get('constant', False)
            property_type = v['schema']['type']
            if property_type == 'object':
                property_type = v['schema']['details']['default']['name']

            # what if list, dict

            composed_property = ComposedProperty(
                name=k,
                description=v['details']['default']['description'].strip(),
                property_type=property_type,
                required=required,
                readonly=readonly,
                constant=constant,
                default_value=v['schema'].get('default')
            )
            properties.append(composed_property)
        properties.sort(key=lambda item: (not(item.readonly or item.constant), item.name))
        if not properties:
            properties = None
        return properties

    @classmethod
    def from_yaml(cls, yaml_data):
        # Returns a CompositeType from a yaml file
        name = yaml_data['details']['default']['name']
        description = yaml_data['details']['default']['description'].strip() or (name + ".")
        properties = cls._create_properties(yaml_data)

        return cls(
            name=name,
            description=description,
            properties=properties
        )