from .baseserializer import BaseSerializer
from jinja2 import Template, PackageLoader, Environment


class GenericSerializer(BaseSerializer):
    def __init__(self, code_model):
        super(GenericSerializer, self).__init__(code_model)


    def _format_model_for_file(self, model):
        for prop in model.properties:
            prop = self._format_property_doc_string_for_file(prop)
        model.init_line = "def __init__(self, **kwargs):"


    def serialize(self):
        env = Environment(
            loader=PackageLoader('autorest', 'templates'),
            keep_trailing_newline=True
        )

        for model in self.code_model.schemas:
            model = self._format_model_for_file(model)

        # Generate the service client content
        template = env.get_template("service_client.py.jinja2")
        self._service_client_file = template.render(code_model=self.code_model)

        template = env.get_template("model_container.py.jinja2")
        self._model_file = template.render(code_model=self.code_model)