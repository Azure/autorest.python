from ..models import DictionarySchema, EnumSchema, ListSchema, ObjectSchema, PrimitiveSchema
from jinja2 import Template, PackageLoader, Environment


class BaseSerializer:
    def __init__(self, code_model):
        self.code_model = code_model
        self._service_client_file = None
        self._model_file = None


    def _format_property_doc_string_for_file(self, prop):
        # building the param line of the property doc
        if prop.constant or prop.readonly:
            param_doc_string = ":ivar {}:".format(prop.name)
        else:
            param_doc_string = ":param {}:".format(prop.name)
        description = prop.description
        if prop.required:
            description = "Required. " + description
        if description and description[-1] != ".":
            description += "."
        if description:
            param_doc_string += " " + description

        # building the type line of the property doc
        try:
            type_doc_string = ":type {}: ".format(prop.name)
            if isinstance(prop, DictionarySchema):
                type_doc_string += "dict[str, {}]".format(prop.element_type)
            elif isinstance(prop, ListSchema):
                type_doc_string += "list[{}]".format(prop.element_type)
            elif isinstance(prop, EnumSchema):
                type_doc_string += "str or {}".format(prop.enum_type)
            elif isinstance(prop, ObjectSchema):
                type_doc_string += prop.schema_type
            elif isinstance(prop, PrimitiveSchema):
                type_doc_string += prop.schema_type
            prop.documentation_string = param_doc_string + "\n\t" + type_doc_string
        except:
            raise ValueError("{} {}".format(prop.name, prop.description))




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

        template = env.get_template("model_container.py.jinja2")
        self._model_file = template.render(code_model=self.code_model)


    @property
    def service_client_file(self):
        return self._service_client_file

    @property
    def model_file(self):
        return self._model_file