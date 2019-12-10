from .constant_schema import ConstantSchema
from typing import Any, Dict

class Property:
    def __init__(self, yaml_data, name, schema, original_swagger_name, **kwargs):
        self.yaml_data = yaml_data
        self.name = name
        self.schema = schema
        self.original_swagger_name = original_swagger_name.replace('.', '\\\\.')

        self.required = yaml_data.get('required', False)
        self.readonly = yaml_data.get('readOnly', False)
        self.is_discriminator = yaml_data.get('isDiscriminator', False)
        # this bool doesn't consider you to be constant if you are a discriminator
        self.constant = isinstance(self.schema, ConstantSchema) and not self.is_discriminator
        self.documentation_string = None

        if kwargs.get('description', None):
            self.description = kwargs.pop('description')
        else:
            description = yaml_data['language']['python']['description'].strip()
            if description == 'MISSING-SCHEMA-DESCRIPTION-OBJECTSCHEMA':
                description = name + "."
            elif 'MISSING' in description:
                description = ""
            self.description = description

        validation_map = {}
        if self.required:
            validation_map['required'] = True
        if self.readonly:
            validation_map['readonly'] = True
        if self.constant:
            validation_map['constant'] = True
        if self.schema.get_validation_map():
            validation_map.update(self.schema.get_validation_map())
        self.validation_map = validation_map or None

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
    def from_yaml(cls, yaml_data: Dict[str, Any], **kwargs) -> "Property":
        from . import build_schema
        name = yaml_data['language']['python']['name']
        has_additional_properties = kwargs.pop("has_additional_properties", None)
        if name == 'additional_properties' and has_additional_properties:
            name = 'additional_properties1'
        schema = build_schema(yaml_data=yaml_data['schema'], **kwargs)
        return cls(
            name=name,
            schema=schema,
            original_swagger_name=yaml_data['serializedName'],
            yaml_data=yaml_data
        )
