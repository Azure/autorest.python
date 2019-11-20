from jinja2 import Template, PackageLoader, Environment

class AioGeneralSerializer:
    def __init__(self, code_model):
        self.code_model = code_model
        self._init_file = None
        self._service_client_file = None
        self._config_file = None

    def serialize(self):
        env = Environment(
            loader=PackageLoader('autorest', 'templates'),
            keep_trailing_newline=True,
            line_statement_prefix="##",
            line_comment_prefix="###",
            trim_blocks=True,
            lstrip_blocks=True
        )

        template = env.get_template("init.py.jinja2")
        self._init_file = template.render(
            module_name=self.code_model.module_name,
            class_name=self.code_model.class_name,
            async_mode=True
        )

        template = env.get_template("service_client.py.jinja2")
        self._service_client_file = template.render(
            code_model=self.code_model,
            async_mode=True
        )

        template = env.get_template("config.py.jinja2")
        self._config_file = template.render(class_name=self.code_model.class_name, async_mode=True)

    @property
    def init_file(self):
        return self._init_file

    @property
    def service_client_file(self):
        return self._service_client_file

    @property
    def config_file(self):
        return self._config_file