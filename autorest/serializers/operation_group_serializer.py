from .import_serializer import FileImportSerializer, ImportType

class OperationGroupSerializer:
    def __init__(self, code_model, env, operation_group, async_mode):
        self.code_model = code_model
        self.env = env
        self.operation_group = operation_group
        self.async_mode = async_mode
        self._operation_group_file = None

    @staticmethod
    def _change_imports_for_async(imports):
        # change model import for async operation groups
        local_imports = imports.imports[ImportType.LOCAL]
        if local_imports.get("..."):
            local_imports["..."].add("models")
        else:
            local_imports["..."] = {"models"}
        local_imports[".."].remove("models")
        if not local_imports[".."]:
            del local_imports[".."]

        # change distributed_trace import for async operation groups
        azure_core_imports = imports.imports[ImportType.AZURECORE]
        if azure_core_imports.get("azure.core.tracing.decorator"):
            azure_core_imports["azure.core.tracing.decorator_async"] = {"distributed_trace_async"}
            del azure_core_imports["azure.core.tracing.decorator"]


    def serialize(self):
        operation_group_template = self.env.get_template("operations_container.py.jinja2")
        imports = self.operation_group.imports()
        if self.async_mode:
            OperationGroupSerializer._change_imports_for_async(imports)
        self._operation_group_file = operation_group_template.render(
            code_model=self.code_model,
            operation_group=self.operation_group,
            imports=FileImportSerializer(imports),
            async_mode=self.async_mode
        )

    @property
    def operation_group_file(self):
        return self._operation_group_file