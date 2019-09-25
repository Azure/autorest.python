from ..models import CompositeType, DictionaryType, SequenceType
from jinja2 import Template, PackageLoader, Environment

class GenericSerializer:
    def __init__(self, code_model):
        self.code_model = code_model
        self.schemas = code_model.schemas
        self._service_client_file = None
        self._model_file = None



    def type_documentation(property_type):
        if isinstance(property_type, DictionaryType):
            return "dict[str, {}]".format(property_type.element_type)
        if isinstance(property_type, SequenceType):
            return "list[{}]".format(self.element_type)
        return property_type.property_type

    def serialize(self):
        env = Environment(
            loader=PackageLoader('autorest', 'templates'),
            keep_trailing_newline=True
        )
        # Generate the service client content
        template = env.get_template("service_client.py.jinja2")
        self._service_client_file = template.render(code_model=self.code_model)

        template = env.get_template("model_container.py.jinja2")
        self._model_file = template.render(code_model=self.code_model)

    def service_client_file(self):
        return self._service_client_file

    def model_file(self):
        return self._model_file