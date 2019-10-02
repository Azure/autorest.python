from typing import Any, Dict


class BaseSchema:
    def __init__(self, name, description, **kwargs):
        self.name = name
        self.description = description
        self.serialize_name = kwargs.pop('serialize_name', '')
        if self.serialize_name:
            self.serialize_name = self.serialize_name.replace('.', '\\\\.')
        self.required = kwargs.pop('required', False)
        self.readonly = kwargs.pop('readonly', False)
        self.constant = kwargs.pop('constant', False)
        self.documentation_string = None
        self.attribute_map_string = None

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
        if description:
            doc_string += " " + description
        return doc_string

    @classmethod
    def _get_common_parameters(self, name, yaml_data) -> Dict[str, Any]:
        return_dict = {}
        description = yaml_data['description'].strip()
        if description == 'MISSING-SCHEMA-DESCRIPTION-OBJECTSCHEMA':
            description = name + "."
        elif 'MISSING' in description:
            description = ""
        return_dict['required'] = yaml_data.get('required', False)
        return_dict['readonly'] = yaml_data.get('readOnly', False)
        return_dict['constant'] = yaml_data.get('constant', False)
        return_dict['description'] = description
        return return_dict