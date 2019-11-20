from .import_serializer import FileImportSerializer

class OperationGroupSerializer:
    def __init__(self, code_model, env, operation_group, async_mode):
        self.code_model = code_model
        self.env = env
        self.operation_group = operation_group
        self.async_mode = async_mode
        self._operation_group_file = None

    def serialize(self):
        operation_group_template = self.env.get_template("operations_container.py.jinja2")

        self._operation_group_file = operation_group_template.render(
            code_model=self.code_model,
            operation_group=self.operation_group,
            imports=FileImportSerializer(self.operation_group.imports()),
            async_mode=self.async_mode
        )

    @property
    def operation_group_file(self):
        return self._operation_group_file