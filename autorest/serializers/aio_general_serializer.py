from jinja2 import Template, PackageLoader, Environment

class AioGeneralSerializer:
    def __init__(self, code_model, operation_group_names):
        self.code_model = code_model
        self.operation_group_names = operation_group_names
        self._init_file = None
        self._service_client_file = None
        self._config_file = None

    def serialize(self):
        env = Environment(
            loader=PackageLoader('autorest', 'templates'),
            keep_trailing_newline=True
        )

        template = env.get_template("init.py.jinja2")
        self._init_file = template.render(
            python_client_name=self.code_model.python_client_name,
            camel_case_client_name=self.code_model.camel_case_client_name,
            async_mode=True
        )

        template = env.get_template("service_client.py.jinja2")
        self._service_client_file = template.render(
            code_model=self.code_model,
            operation_group_names=self.operation_group_names,
            async_mode=True
        )

        template = env.get_template("config.py.jinja2")
        self._config_file = template.render(python_client_name=self.code_model.python_client_name, async_mode=True)

    @property
    def init_file(self):
        return self._init_file

    @property
    def service_client_file(self):
        return self._service_client_file

    @property
    def config_file(self):
        return self._config_file