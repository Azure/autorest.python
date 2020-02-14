# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import json
from typing import Any, List, Dict, Optional, Set, Tuple
from ..models import CodeModel, Operation, OperationGroup



class MetadataSerializer:
    def __init__(self, code_model: CodeModel):
        self.code_model = code_model

    def _choose_api_version(self) -> Tuple[str, List[str]]:
        chosen_version = ""
        total_api_version_set: Set[str] = set()
        for operation_group in self.code_model.operation_groups:
            total_api_version_set.update(operation_group.api_versions)
        if len(total_api_version_set) == 1:
            chosen_version = total_api_version_set[0]
        return chosen_version, total_api_version_set


    def serialize(self) -> str:
        mixin_operation_group: Optional[OperationGroup] = next(
            (operation_group
            for operation_group in self.code_model.operation_groups if operation_group.is_empty_operation_group),
            None
        )
        mixin_operations: List[Operation] = []
        if mixin_operation_group:
            mixin_operations = mixin_operation_group.operations
        chosen_version, total_api_version_set = self._choose_api_version()

        return json.dumps(
            {
                "chosen_version": chosen_version,
                "all_versions": total_api_version_set,
                "client": {
                    "name": self.code_model.class_name,
                    "filename": f"_{self.code_model.module_name}.py",
                    "description": self.code_model.description,
                    "has_subscription_id": any(
                        [
                            gp for gp in self.code_model.global_parameters.method
                            if gp.serialized_name == "subscription_id"
                        ]
                    )
                },
                "operation_groups": {
                    operation_group.name: operation_group.class_name
                    for operation_group in self.code_model.operation_groups
                    if not operation_group.is_empty_operation_group
                },
                "operation_mixins": {
                    operation.name: {
                        "doc": "FIXME",
                        "signature": "FIXME",
                        "call": "FIXME"
                    } for operation in mixin_operations
                }
                # "operation_mixins": {
                #     operation_group.name: {
                #         "description": operation_group.description,
                #         "signature": ___,
                #         "call": __
                #     }
                # }
            }
        )
