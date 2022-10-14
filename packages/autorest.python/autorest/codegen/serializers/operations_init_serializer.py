# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List
from jinja2 import Environment

from autorest.codegen.models.operation_group import OperationGroup
from ..models import NamespaceModel


class OperationsInitSerializer:
    def __init__(
        self, namespace_model: NamespaceModel, env: Environment, async_mode: bool
    ) -> None:
        self.namespace_model = namespace_model
        self.env = env
        self.async_mode = async_mode

    def operation_group_imports(self) -> List[str]:
        def _get_filename(operation_group: OperationGroup) -> str:
            return (
                "_operations"
                if self.namespace_model.options["combine_operation_files"]
                else operation_group.filename
            )

        return [
            f"from .{_get_filename(og)} import {og.class_name}"
            for og in self.namespace_model.operation_groups
        ]

    def serialize(self) -> str:
        operation_group_init_template = self.env.get_template(
            "operations_folder_init.py.jinja2"
        )

        return operation_group_init_template.render(
            namespace_model=self.namespace_model,
            async_mode=self.async_mode,
            operation_group_imports=self.operation_group_imports,
        )
