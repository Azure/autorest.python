from .constant_schema import ConstantSchema
class Property:
    def __init__(self, name, schema, original_swagger_name, property_data, **kwargs):
        self.name = name
        self.schema = schema
        self.original_swagger_name = original_swagger_name.replace('.', '\\\\.')

        self.required = property_data.get('required', False)
        self.readonly = property_data.get('readOnly', False)
        self.is_discriminator = property_data.get('isDiscriminator', False)
        # this bool doesn't consider you to be constant if you are a discriminator
        self.constant = isinstance(self.schema, ConstantSchema) and not self.is_discriminator
        self.documentation_string = None

        if kwargs.get('description', None):
            self.description = kwargs.pop('description')
        else:
            description = property_data['language']['default']['description'].strip()
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
        self.validation_map = validation_map if validation_map else None

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
