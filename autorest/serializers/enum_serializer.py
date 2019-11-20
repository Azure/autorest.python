from .import_serializer import FileImportSerializer
from jinja2 import Template, PackageLoader, Environment


class EnumSerializer:
    def __init__(self, enums, env):
        self.enums = enums
        self.env = env
        self._enum_file = None

    def serialize(self):
        # Generate the enum file
        template = self.env.get_template("enum_container.py.jinja2")
        self._enum_file = template.render(enums=self.enums.values())

    @property
    def enum_file(self):
        return self._enum_file