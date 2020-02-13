# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import json
from typing import Any, Dict
from ..models import CodeModel


class MetadataSerializer:
    def __init__(self, code_model: CodeModel):
        self.code_model = code_model

    def serialize(self) -> Dict[str, Any]:
        return json.dumps(
            {
                "version": self.code_model.options['package_version'],
                "client": {
                    "name": self.code_model.class_name,
                    "filename": f"_{self.code_model.module_name}.py",
                    "description": self.code_model.description,
                    "has_subscription_id": any([gp for gp in self.code_model.global_parameters.method if gp.serialized_name == "subscription_id"])
                },
                "operation_groups": {
                    operation_group.name: operation_group.class_name for operation_group in self.code_model.operation_groups if not operation_group.is_empty_operation_group
                },
                "operation_mixins": {
                    operation.name: {
                        doc: "FIXME",
                        signature: "FIXME",
                        call: "FIXME"
                    } for operation in next((operation_group for operation_group in self.code_model.operation_groups if operation_group.is_empty_operation_group), [])
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
