import re
from ..models import DictionarySchema, EnumSchema, ListSchema, ObjectSchema, PrimitiveSchema
from ..common.utils import to_python_type
from .import_serializer import FileImportSerializer
from jinja2 import Template, PackageLoader, Environment


class ModelBaseSerializer:
    def __init__(self, code_model):
        self.code_model = code_model
        self._model_file = None

    def _format_model_name_and_description(self, model):
        model_name_list = re.split('[^a-zA-Z\\d]', model.name)
        model_name_list = [s[0].upper() + s[1:] if len(s) > 1 else s.upper()
                            for s in model_name_list]
        model.name= ''.join(model_name_list)
        if not model.description:
            model.description = model.name + "."

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
            type_doc_string += "str or ~{}.models.{}".format(self.code_model.namespace, prop.enum_type)
        elif isinstance(prop, ObjectSchema):
            type_doc_string += "~{}.models.{}".format(self.code_model.namespace, prop.schema_type)
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

        # Generate the models
        template = env.get_template("model_container.py.jinja2")
        self._model_file = template.render(
            code_model=self.code_model,
            imports=FileImportSerializer(self.code_model.imports())
        )

    @property
    def model_file(self):
        return self._model_file
