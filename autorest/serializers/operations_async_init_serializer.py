class OperationsAsyncSerializer:

    
    def serialize(self):
        operation_group_template = self.env.get_template("operations_container.py.jinja2")
        operation_group_init_template = self.env.get_template("operations_container_init.py.jinja2")

        base_path = namespace if not async_mode else namespace / Path("aio")

        operation_groups = code_model.operation_groups

        operation_group_init_content = operation_group_init_template.render(
            code_model=code_model,
            operation_groups=operation_groups,
            async_mode=async_mode
        )
        async_suffix = "_async" if async_mode else ""

        self._autorestapi.write_file(
            base_path / Path(f"operations{async_suffix}") / Path("__init__.py"),
            operation_group_init_content
        )

        for operation_group in operation_groups:
            operation_group_content = operation_group_template.render(
                code_model=code_model,
                operation_group=operation_group,
                imports=FileImportSerializer(operation_group.imports()),
                async_mode=async_mode
            )
            self._autorestapi.write_file(
                base_path / Path(f"operations{async_suffix}") / Path(f"_{operation_group.name}_operations{async_suffix}.py"),
                operation_group_content
            )