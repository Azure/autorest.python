from .baseschema import BaseSchema
from typing import Any, Dict

class ListSchema(BaseSchema):
    def __init__(self, name, description, element_type, **kwargs):
        super(ListSchema, self).__init__(name, description, **kwargs)
        self.element_type = element_type
        self.max_items = kwargs.pop('max_items', None)
        self.min_items = kwargs.pop('min_items', None)
        self.unique_items = kwargs.pop('unique_items', None)


    def get_attribute_map_type(self):
        return '[{}]'.format(self.element_type)

    @classmethod
    def from_yaml(cls, name: str, yaml_data: Dict[str, str], **kwargs: Any) -> "SequenceType":
        common_parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data,
            required_list=kwargs.pop('required_list', None)
        )
        # TODO: for items, if the type is a primitive is it listed in type instead of $ref?
        if yaml_data['items'].get('$ref'):
            # type of entry in list is another Class
            element_type = yaml_data['items']['$ref']
        else:
            # type of entry in list is a known type
            try:
                element_type = yaml_data['items']['type']
            except:
                # TODO: don't know what to do for anyOf etc yet
                element_type = None
        return cls(
            name=name,
            description=common_parameters_dict['description'],
            element_type=element_type,
            required=common_parameters_dict['required'],
            readonly=common_parameters_dict['readonly'],
            constant=common_parameters_dict['constant'],
            max_items=yaml_data.get('maxItems'),
            min_items=yaml_data.get('minItems'),
            unique_items=yaml_data.get('uniqueItems')
        )