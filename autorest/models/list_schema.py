from .base_schema import BaseSchema
from typing import Any, Dict, Optional


class ListSchema(BaseSchema):
    def __init__(self, yaml_data, element_type, **kwargs):
        super(ListSchema, self).__init__(yaml_data, **kwargs)
        self.element_type = element_type
        self.max_items = kwargs.pop('max_items', None)
        self.min_items = kwargs.pop('min_items', None)
        self.unique_items = kwargs.pop('unique_items', None)

    def get_serialization_type(self):
        return '[{}]'.format(self.element_type.get_serialization_type())

    def get_python_type_annotation(self):
        return f'List[{self.element_type.get_python_type_annotation()}]'

    def get_python_type(self, namespace):
        return f'list[{self.element_type.get_python_type(namespace)}]'

    def get_validation_map(self):
        validation_map = {}
        if self.max_items:
            validation_map['max_items'] = self.max_items
            validation_map['min_items'] = self.min_items or 0
        if self.min_items:
            validation_map['min_items'] = self.min_items
        if self.unique_items:
            validation_map['unique'] = True
        return validation_map or None

    def xml_serialization_ctxt(self) -> Optional[str]:
        attrs_list = []
        base_xml_map = super().xml_serialization_ctxt()
        if base_xml_map:
            attrs_list.append(base_xml_map)

        # Attribute at the list level
        if self.xml_metadata.get('wrapped', False):
            attrs_list.append("'wrapped': True")

        # Attributes of the items
        item_xml_metadata = self.element_type.xml_metadata
        if item_xml_metadata.get('name'):
            attrs_list.append(f"'itemsName': '{item_xml_metadata['name']}'")
        if item_xml_metadata.get('prefix', False):
            attrs_list.append(f"'itemsPrefix': '{item_xml_metadata['prefix']}'")
        if item_xml_metadata.get('namespace', False):
            attrs_list.append(f"'itemsNs': '{item_xml_metadata['namespace']}'")

        return ", ".join(attrs_list)

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str], **kwargs) -> "SequenceType":
        # TODO: for items, if the type is a primitive is it listed in type instead of $ref?
        element_schema = yaml_data['elementType']

        from . import build_schema
        element_type = build_schema(
            yaml_data=element_schema,
            **kwargs
        )

        return cls(
            yaml_data=yaml_data,
            element_type=element_type,
            max_items=yaml_data.get('maxItems'),
            min_items=yaml_data.get('minItems'),
            unique_items=yaml_data.get('uniqueItems'),
        )