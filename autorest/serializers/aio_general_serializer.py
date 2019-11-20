from jinja2 import Template, PackageLoader, Environment

class AioGeneralSerializer:
    def __init__(self, code_model, env):
        self.code_model = code_model
        self.env = env
        self._init_file = None
        self._service_client_file = None
        self._config_file = None

    def serialize(self):

        template = self.env.get_template("init.py.jinja2")
        self._init_file = template.render(
            module_name=self.code_model.module_name,
            class_name=self.code_model.class_name,
            async_mode=True
        )

        template = self.env.get_template("service_client.py.jinja2")
        self._service_client_file = template.render(
            code_model=self.code_model,
            async_mode=True
        )

        template = self.env.get_template("config.py.jinja2")
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