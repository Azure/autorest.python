# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import copy
import json
from typing import List, Optional, Set, Tuple, Dict
from jinja2 import Environment
from ..models import (
    CodeModel,
    Operation,
    OperationGroup,
    LROOperation,
    PagingOperation,
    CredentialSchema,
    ParameterList,
    TypingSection,
    ImportType
)

def _correct_credential_parameter(global_parameters: ParameterList, async_mode: bool) -> None:
    credential_param = [
        gp for gp in global_parameters.parameters if isinstance(gp.schema, CredentialSchema)
    ][0]
    credential_param.schema = CredentialSchema(async_mode=async_mode)

def _json_serialize_imports(
    imports: Dict[TypingSection, Dict[ImportType, Dict[str, Set[Optional[str]]]]]
):
    if not imports:
        return None

    json_serialize_imports = {}
    # need to make name_import set -> list to make the dictionary json serializable
    # not using an OrderedDict since we're iterating through a set and the order there varies
    # going to sort the list instead

    for typing_section_key, typing_section_value in imports.items():
        json_import_type_dictionary = {}
        for import_type_key, import_type_value in typing_section_value.items():
            json_package_name_dictionary = {}
            for package_name, name_imports in import_type_value.items():
                name_import_ordered_list = []
                if name_imports:
                    name_import_ordered_list = list(name_imports)
                    name_import_ordered_list.sort()
                json_package_name_dictionary[package_name] = name_import_ordered_list
            json_import_type_dictionary[import_type_key] = json_package_name_dictionary
        json_serialize_imports[typing_section_key] = json_import_type_dictionary
    return json.dumps(json_serialize_imports)


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
        mixin_operation_group: Optional[OperationGroup] = next(
            (operation_group
            for operation_group in self.code_model.operation_groups if operation_group.is_empty_operation_group),
            None
        )
        mixin_operations: List[Operation] = []
        sync_mixin_imports = None
        async_mixin_imports = None
        if mixin_operation_group:
            mixin_operations = mixin_operation_group.operations
            sync_mixin_imports = mixin_operation_group.imports(async_mode=False, has_schemas=False)
            async_mixin_imports = mixin_operation_group.imports(async_mode=True, has_schemas=False)
        chosen_version, total_api_version_list = self._choose_api_version()

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
            str=str,
            sync_mixin_imports=(
                _json_serialize_imports(sync_mixin_imports.imports)
                if sync_mixin_imports else None
            ),
            async_mixin_imports=(
                _json_serialize_imports(async_mixin_imports.imports)
                if async_mixin_imports else None
            )
        )
