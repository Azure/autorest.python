# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
class OperationsInitSerializer:
    def __init__(self, code_model, env, async_mode):
        self.code_model = code_model
        self.env = env
        self.async_mode = async_mode
        self._operations_init_file = None

    def serialize(self):
        operation_group_init_template = self.env.get_template("operations_container_init.py.jinja2")

        self._operations_init_file = operation_group_init_template.render(
            code_model=self.code_model,
            operation_groups=self.code_model.operation_groups,
            async_mode=self.async_mode
        )

    @property
    def operations_init_file(self):
        return self._operations_init_file
