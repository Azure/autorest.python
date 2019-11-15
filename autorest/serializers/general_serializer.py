from jinja2 import Template, PackageLoader, Environment
from ..common.utils import get_namespace_name, get_method_name, get_client_name, to_camel_case

class GeneralSerializer:
    def __init__(self, code_model, operation_group_names):
        self.code_model = code_model
        self.operation_group_names = operation_group_names
        self._init_file = None
        self._service_client_file = None
        self._config_file = None
        self._version_file = None
        self._setup_file = None

    def serialize(self):
        env = Environment(
            loader=PackageLoader('autorest', 'templates'),
            keep_trailing_newline=True
        )
        env.globals.update(get_namespace_name=get_namespace_name)
        env.globals.update(get_method_name=get_method_name)
        env.globals.update(get_client_name=get_client_name)
        env.globals.update(to_camel_case=to_camel_case)

        template = env.get_template("init.py.jinja2")
        self._init_file = template.render(
            client_name=self.code_model.client_name,
            is_async=False
        )

        template = env.get_template("service_client.py.jinja2")
        self._service_client_file = template.render(
            code_model=self.code_model,
            operation_group_names=self.operation_group_names,
            is_async=False
        )

        template = env.get_template("config.py.jinja2")
        self._config_file = template.render(client_name=self.code_model.client_name, is_async=False)

        template = env.get_template("version.py.jinja2")
        self._version_file = template.render(version=self.code_model.api_version)

        template = env.get_template("setup.py.jinja2")
        self._setup_file = template.render(code_model=self.code_model)

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

    @property
    def setup_file(self):
        return self._setup_file