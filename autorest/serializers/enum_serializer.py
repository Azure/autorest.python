from .import_serializer import FileImportSerializer
from jinja2 import Template, PackageLoader, Environment


class EnumSerializer:
    def __init__(self, enums):
        self.enums = enums
        self._enum_file = None

    def serialize(self):
        env = Environment(
            loader=PackageLoader('autorest', 'templates'),
            keep_trailing_newline=True
        )

        # Generate the enum file
        template = env.get_template("enum_container.py.jinja2")
        self._enum_file = template.render(enums=self.enums)

    @property
    def enum_file(self):
        return self._enum_file