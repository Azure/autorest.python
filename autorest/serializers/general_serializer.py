from jinja2 import Template, PackageLoader, Environment

class GeneralSerializer:
    def __init__(self, code_model):
        self.code_model = code_model
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

        template = env.get_template("init.py.jinja2")
        self._init_file = template.render(
            python_client_name=self.code_model.python_client_name,
            pascal_case_client_name=self.code_model.pascal_case_client_name,
            async_mode=False
        )

        template = env.get_template("service_client.py.jinja2")
        self._service_client_file = template.render(
            code_model=self.code_model,
            async_mode=False
        )

        template = env.get_template("config.py.jinja2")
        self._config_file = template.render(pascal_case_client_name=self.code_model.pascal_case_client_name, async_mode=False)

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