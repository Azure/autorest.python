from jinja2 import Template, PackageLoader, Environment
from .import_serializer import FileImportSerializer


class GeneralSerializer:
    def __init__(self, code_model, env, async_mode):
        self.code_model = code_model
        self.env = env
        self.async_mode = async_mode
        self._init_file = None
        self._service_client_file = None
        self._config_file = None
        self._version_file = None
        self._setup_file = None

    def serialize(self):
        template = self.env.get_template("pkgutil_init.py.jinja2")
        self._pkgutil_init_file = template.render()

        template = self.env.get_template("init.py.jinja2")
        self._init_file = template.render(
            code_model=self.code_model,
            async_mode=self.async_mode,
        )

        template = self.env.get_template("service_client.py.jinja2")
        self._service_client_file = template.render(
            code_model=self.code_model,
            async_mode=self.async_mode,
            imports=FileImportSerializer(
                self.code_model.service_client.imports(self.code_model, self.async_mode)
            ),
        )

        template = self.env.get_template("config.py.jinja2")
        self._config_file = template.render(
            code_model=self.code_model,
            async_mode=self.async_mode
        )

        if not self.async_mode:
            template = self.env.get_template("version.py.jinja2")
            self._version_file = template.render(code_model=self.code_model)

            template = self.env.get_template("setup.py.jinja2")
            self._setup_file = template.render(code_model=self.code_model)

    @property
    def pkgutil_init_file(self):
        return self._pkgutil_init_file

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