from .basetype import BaseType
from typing import Any, Dict

class SequenceType(BaseType):
    def __init__(self, name, description, element_type, **kwargs):
        super(SequenceType, self).__init__(name, description, **kwargs)
        self.element_type = element_type
    def get_attribute_map_type(self):
        return '[{}]'.format(self.element_type)

    @classmethod
    def from_yaml(cls, name: str, yaml_data: Dict[str, str], **kwargs: Any) -> "SequenceType":
        parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data,
            required_list=kwargs.pop('required_list', None)
        )
        if yaml_data['elementType'].get('$ref'):
            # type of entry in list is another Class
            element_type = yaml_data['elementType']['$ref']
        else:
            # type of entry in list is a known type
            element_type = yaml_data['elementType']['type']
        return cls(
            name=name,
            description=parameters_dict['description'],
            element_type=element_type,
            required=parameters_dict['required'],
            readonly=parameters_dict['readonly'],
            constant=parameters_dict['constant']
        )