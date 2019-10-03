from jinja2 import Template, PackageLoader, Environment
from ..common.utils import get_namespace_name

class ModelInitSerializer:
    def __init__(self, code_model):
        self.code_model = code_model
        self._model_init_file = None

    def serialize(self):
        env = Environment(
            loader=PackageLoader('autorest', 'templates'),
            keep_trailing_newline=True
        )
        schemas = sorted(self.code_model.schemas, key=lambda x: x.name)
        enums = [e.enum_type for e in self.code_model.enums] if self.code_model.enums else None

        if enums:
            enums.sort()

        template = env.get_template("model_init.py.jinja2")
        self._model_init_file = template.render(
            schemas=schemas,
            enums=enums,
            client_name=get_namespace_name(self.code_model.client_name)
        )

    @property
    def model_init_file(self):
        return self._model_init_file
