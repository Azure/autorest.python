from ..models import DictionarySchema, EnumSchema, ListSchema, ObjectSchema, PrimitiveSchema
from .import_serializer import FileImportSerializer
from jinja2 import Template, PackageLoader, Environment


class ModelBaseSerializer:
    def __init__(self, code_model, namespace):
        self.code_model = code_model
        self.namespace = namespace
        self._service_client_file = None
        self._model_file = None


    def _format_property_doc_string_for_file(self, prop):
        # building the param line of the property doc
        if prop.constant or prop.readonly:
            param_doc_string = ":ivar {}:".format(prop.name)
        else:
            param_doc_string = ":param {}:".format(prop.name)
        description = prop.description
        if description and description[-1] != ".":
            description += "."
        if prop.name == 'tags':
            description = "A set of tags. " + description
        if prop.required:
            if description:
                description = "Required. " + description
            else:
                description = "Required."
        if isinstance(prop, EnumSchema):
            values = ["\'" + v.value + "\'" for v in prop.values]
            description += " Possible values include: {}.".format(", ".join(values))
            if prop.default_value:
                description += " Default value: \"{}\".".format(prop.default_value)
        if description:
            param_doc_string += " " + description

        # building the type line of the property doc
        if prop.constant or prop.readonly:
            type_doc_string = ":vartype {}: ".format(prop.name)
        else:
            type_doc_string = ":type {}: ".format(prop.name)
        if isinstance(prop, DictionarySchema):
            type_doc_string += "dict[str, {}]".format(prop.element_type)
        elif isinstance(prop, ListSchema):
            type_doc_string += "list[{}]".format(prop.element_type)
        elif isinstance(prop, EnumSchema):
            type_doc_string += "str or ~{}.models.{}".format(self.namespace, prop.enum_type)
        elif isinstance(prop, ObjectSchema):
            type_doc_string += prop.schema_type
        elif isinstance(prop, PrimitiveSchema):
            type_doc_string += prop.schema_type
        prop.documentation_string = param_doc_string + "\n\t" + type_doc_string


    def serialize(self):
        env = Environment(
            loader=PackageLoader('autorest', 'templates'),
            keep_trailing_newline=True
        )

        for model in self.code_model.schemas:
            self._format_model_for_file(model)

        # Generate the service client content
        template = env.get_template("service_client.py.jinja2")
        self._service_client_file = template.render(code_model=self.code_model)

        # Generate the models
        template = env.get_template("model_container.py.jinja2")
        self._model_file = template.render(
            code_model=self.code_model,
            imports=FileImportSerializer(self.code_model.imports())
        )


    @property
    def service_client_file(self):
        return self._service_client_file

    @property
    def model_file(self):
        return self._model_file
