from jinja2 import Template, PackageLoader, Environment
from ..common.utils import get_namespace_name

class GeneralSerializer:
    def __init__(self, code_model, client_name, version):
        self.code_model = code_model
        self.client_name = client_name
        self.version = version
        self._init_file = None
        self._service_client_file = None
        self._config_file = None
        self._version_file = None

    def serialize(self):
        env = Environment(
            loader=PackageLoader('autorest', 'templates'),
            keep_trailing_newline=True
        )

        template = env.get_template("top_level_init.py.jinja2")
        self._init_file = template.render(client_name=self.client_name, pycase_client_name=get_namespace_name(self.client_name))

        template = env.get_template("service_client.py.jinja2")
        self._service_client_file = template.render(code_model=self.code_model)

        template = env.get_template("config.py.jinja2")
        self._config_file = template.render(client_name=self.client_name, lowercase_client_name = self.client_name.lower())

        template = env.get_template("version.py.jinja2")
        self._version_file = template.render(version=self.version)

    @property
    def init_file(self):
        return self._init_file

    @property
    def service_client_file(self):
        return self._service_client_file

    @property
    def config_file(self):
        return self._config_file

    @property
    def version_file(self):
        return self._version_file