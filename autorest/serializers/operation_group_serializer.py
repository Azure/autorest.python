from .import_serializer import FileImportSerializer, ImportType
from ..models import FileImport

class OperationGroupSerializer:
    def __init__(self, code_model, env, operation_group, async_mode):
        self.code_model = code_model
        self.env = env
        self.operation_group = operation_group
        self.async_mode = async_mode
        self._operation_group_file = None

    @staticmethod
    def _change_imports_for_async(imports):
        new_imports = FileImport()
        new_imports.merge(imports)
        # change model import for async operation groups
        local_imports = new_imports.imports[ImportType.LOCAL]
        new_imports.add_from_import("...", "models", ImportType.LOCAL)
        local_imports[".."].remove("models")
        if not local_imports[".."]:
            del local_imports[".."]

        # change distributed_trace import for async operation groups
        azure_core_imports = new_imports.imports[ImportType.AZURECORE]
        if azure_core_imports.get("azure.core.tracing.decorator"):
            new_imports.add_from_import("azure.core.tracing.decorator_async", "distributed_trace_async", ImportType.AZURECORE)
            del azure_core_imports["azure.core.tracing.decorator"]

        return new_imports


    def serialize(self):
        operation_group_template = self.env.get_template("operations_container.py.jinja2")
        if self.operation_group.is_empty_operation_group:
            operation_group_template = self.env.get_template("operations_container_mixin.py.jinja2")

        imports = self.operation_group.imports()
        if self.async_mode:
            imports = OperationGroupSerializer._change_imports_for_async(imports)
        self._operation_group_file = operation_group_template.render(
            code_model=self.code_model,
            operation_group=self.operation_group,
            imports=FileImportSerializer(imports),
            async_mode=self.async_mode,
        )

    def filename(self):
        basename = self.operation_group.name
        if self.operation_group.is_empty_operation_group:
            basename = self.code_model.module_name
        async_suffix = "_async" if self.async_mode else ""

        return f"_{basename}_operations{async_suffix}.py"

    @property
    def operation_group_file(self):
        return self._operation_group_file