# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import copy
from typing import List, Optional, Set, Tuple
from jinja2 import Environment
from ..models import (
    CodeModel,
    Operation,
    OperationGroup,
    LROOperation,
    PagingOperation,
    CredentialSchema,
    ParameterList
)
from ..models.imports import FileImport
from .import_serializer import FileImportSerializer

def _correct_credential_parameter(global_parameters: ParameterList, async_mode: bool) -> None:
    # currently this is just copied over from general_serializer.
    # this code will be changed when i merge my async multiapi client
    # pr, since I need two copies of global parameters (one sync and one async).
    credential_param = [
        gp for gp in global_parameters.parameters if isinstance(gp.schema, CredentialSchema)
    ][0]
    credential_param.schema = CredentialSchema(async_mode=async_mode)


class MetadataSerializer:
    def __init__(self, code_model: CodeModel, env: Environment) -> None:
        self.code_model = code_model
        self.env = env

    def _choose_api_version(self) -> Tuple[str, List[str]]:
        chosen_version = ""
        total_api_version_set: Set[str] = set()
        for operation_group in self.code_model.operation_groups:
            total_api_version_set.update(operation_group.api_versions)

        total_api_version_list = list(total_api_version_set)
        total_api_version_list.sort()

        # switching ' to " so json can decode the dict we end up writing to file
        total_api_version_list = [str(api_version).replace("'", "\"") for api_version in total_api_version_list]
        if len(total_api_version_list) == 1:
            chosen_version = total_api_version_list[0]
        elif len(total_api_version_list) > 1:
            module_version = self.code_model.namespace.split(".")[-1]
            for api_version in total_api_version_list:
                if "v{}".format(api_version.replace("-", "_")) == module_version:
                    chosen_version = api_version

        return chosen_version, total_api_version_list

    def _make_async_copy_of_global_parameters(self) -> ParameterList:
        global_parameters = copy.deepcopy(self.code_model.global_parameters)
        _correct_credential_parameter(global_parameters, True)
        return global_parameters

    def serialize(self) -> str:
        def _is_lro(operation):
            return isinstance(operation, LROOperation)

        def _is_paging(operation):
            return isinstance(operation, PagingOperation)

        mixin_operation_group: Optional[OperationGroup] = next(
            (operation_group
            for operation_group in self.code_model.operation_groups if operation_group.is_empty_operation_group),
            None
        )
        mixin_operations: List[Operation] = []
        if mixin_operation_group:
            mixin_operations = mixin_operation_group.operations
        chosen_version, total_api_version_list = self._choose_api_version()

        parameter_imports = FileImport()
        for operation_group in self.code_model.operation_groups:
            for operation in operation_group.operations:
                for parameter in operation.parameters:
                    parameter_imports.merge(parameter.imports())

        # we separate out async and sync for the case of credentials.
        # In this case, we need two copies of the credential global parameter
        # for typing purposes.
        async_global_parameters = self.code_model.global_parameters
        if self.code_model.options['credential']:
            # this ensures that the CredentialSchema showing up in the list of code model's global parameters
            # is sync. This way we only have to make a copy for an async_credential
            _correct_credential_parameter(self.code_model.global_parameters, False)
            async_global_parameters = self._make_async_copy_of_global_parameters()

        template = self.env.get_template("metadata.json.jinja2")
        return template.render(
            chosen_version=chosen_version,
            total_api_version_list=total_api_version_list,
            code_model=self.code_model,
            sync_global_parameters=self.code_model.global_parameters,
            async_global_parameters=async_global_parameters,
            mixin_operations=mixin_operations,
            any=any,
            is_lro=_is_lro,
            is_paging=_is_paging,
            str=str,
            sync_parameter_imports=FileImportSerializer(parameter_imports, is_python_3_file=False),
            async_parameter_imports=FileImportSerializer(parameter_imports, is_python_3_file=True)
        )
