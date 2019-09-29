from typing import Any, Dict


class BaseType:
    def __init__(self, name, description, **kwargs):
        self.name = name
        self.description = description
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
    def _get_common_parameters(self, name, yaml_data, required_list=None) -> Dict[str, Any]:
        return_dict = {}
        return_dict['required'] = name in required_list if required_list else None
        return_dict['readonly'] = yaml_data.get('readOnly')
        return_dict['constant'] = yaml_data.get('constant')
        return_dict['description'] = (yaml_data['description'].strip()
                                      if yaml_data.get('description') else name + ".")
        return return_dict