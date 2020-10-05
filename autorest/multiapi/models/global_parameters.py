# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List
from .global_parameter import GlobalParameter
from .constant_global_parameter import ConstantGlobalParameter

class GlobalParameters:
    def __init__(self, global_parameters_metadata: Dict[str, Any]):
        self.call = global_parameters_metadata["call"]
        self.global_parameters_metadata = global_parameters_metadata

    @property
    def parameters(self) -> List[GlobalParameter]:
        global_parameters_metadata_sync = self.global_parameters_metadata["sync"]
        global_parameters_metadata_async = self.global_parameters_metadata["async"]

        return [
            GlobalParameter(
                name=parameter_name,
                global_parameter_metadata_sync=gp_sync,
                global_parameter_metadata_async=global_parameters_metadata_async[parameter_name]
            )
            for parameter_name, gp_sync in global_parameters_metadata_sync.items()
        ]

    @property
    def constant_parameters(self) -> List[ConstantGlobalParameter]:
        return [
            ConstantGlobalParameter(constant_name, constant_value)
            for constant_name, constant_value in self.global_parameters_metadata["constant"].items()
        ]
