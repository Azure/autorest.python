# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
import sys
from typing import Dict, Any, Set, Union, List
import yaml

from .. import Plugin
from .models.code_model import CodeModel
from .models import build_schema
from .models.operation_group import OperationGroup
from .models.parameter import Parameter
from .models.parameter_list import ParameterList
from .serializers import JinjaSerializer


_LOGGER = logging.getLogger(__name__)


class CodeGenerator(Plugin):
    @staticmethod
    def remove_cloud_errors(yaml_data: Dict[str, Any]) -> None:
        for group in yaml_data["operationGroups"]:
            for operation in group["operations"]:
                if not operation.get("exceptions"):
                    continue
                i = 0
                while i < len(operation["exceptions"]):
                    exception = operation["exceptions"][i]
                    if exception.get("schema") and exception["schema"]["language"]["default"]["name"] == "CloudError":
                        del operation["exceptions"][i]
                        i -= 1
                    i += 1
        if yaml_data.get("schemas") and yaml_data["schemas"].get("objects"):
            for i in range(len(yaml_data["schemas"]["objects"])):
                obj_schema = yaml_data["schemas"]["objects"][i]
                if obj_schema["language"]["default"]["name"] == "CloudError":
                    del yaml_data["schemas"]["objects"][i]
                    break

    @staticmethod
    def _build_exceptions_set(yaml_data: List[Dict[str, Any]]) -> Set[Dict[str, Any]]:
        exceptions_set = set()
        for group in yaml_data:
            for operation in group["operations"]:
                if not operation.get("exceptions"):
                    continue
                for exception in operation["exceptions"]:
                    if not exception.get("schema"):
                        continue
                    exceptions_set.add(exception["schema"]["language"]["python"]["name"])
        return exceptions_set

    def _create_code_model(self, yaml_data: Dict[str, Any], options: Dict[str, Union[str, bool]]) -> CodeModel:
        # Create a code model
        code_model = CodeModel(options)
        code_model.module_name = yaml_data["info"]["python_title"]
        code_model.class_name = yaml_data["info"]["pascal_case_title"]
        code_model.description = (
            yaml_data["info"]["description"] if yaml_data["info"].get("description") else ""
        )

        # Global parameters
        code_model.global_parameters = ParameterList(
            [Parameter.from_yaml(param) for param in yaml_data.get("globalParameters", [])],
            implementation="Client",
        )

        # Custom URL
        dollar_host = [parameter for parameter in code_model.global_parameters if parameter.rest_api_name == "$host"]
        if not dollar_host:
            # We don't want to support multi-api customurl YET (will see if that goes well....)
            # So far now, let's get the first one in the first operation
            # UGLY as hell.....
            first_req_of_first_op_of_first_grp = yaml_data["operationGroups"][0]["operations"][0]["requests"][0]
            code_model.custom_base_url = first_req_of_first_op_of_first_grp["protocol"]["http"]["uri"]
        else:
            dollar_host_parameter = dollar_host[0]
            code_model.global_parameters.remove(dollar_host_parameter)
            code_model.base_url = dollar_host_parameter.yaml_data["clientDefaultValue"]

        # Create operations
        code_model.operation_groups = [
            OperationGroup.from_yaml(code_model, op_group) for op_group in yaml_data["operationGroups"]
        ]

        # Get my namespace
        namespace = self._autorestapi.get_value("namespace")
        _LOGGER.debug("Namespace parameter was %s", namespace)
        if not namespace:
            namespace = yaml_data["info"]["python_title"]
        code_model.namespace = namespace

        if yaml_data.get("schemas"):
            exceptions_set = CodeGenerator._build_exceptions_set(yaml_data=yaml_data["operationGroups"])

            for type_list in yaml_data["schemas"].values():
                for schema in type_list:
                    build_schema(yaml_data=schema, exceptions_set=exceptions_set, code_model=code_model)
            # sets the enums property in our code_model variable, which will later be passed to EnumSerializer

            code_model.add_inheritance_to_models()
            code_model.sort_schemas()
            code_model.add_schema_link_to_operation()
            code_model.add_schema_link_to_global_parameters()
            code_model.generate_single_parameter_from_multiple_media_types()

        # LRO operation
        code_model.format_lro_operations()
        code_model.remove_next_operation()

        if options["credential"]:
            code_model.add_credential_global_parameter()

        return code_model

    def _build_code_model_options(self) -> Dict[str, Any]:
        """Build en options dict from the user input while running autorest.
        """
        azure_arm = self._autorestapi.get_boolean_value("azure-arm", False)
        credential_scopes = self._autorestapi.get_value("credential-scopes")
        if not credential_scopes and azure_arm:
            credential_scopes = "https://management.azure.com/.default"

        license_header = self._autorestapi.get_value("header-text")
        if license_header:
            license_header = license_header.replace("\n", "\n# ")
            license_header = (
                "# --------------------------------------------------------------------------\n# " + license_header
            )
            license_header += "\n# --------------------------------------------------------------------------"

        options: Dict[str, Any] = {
            "azure_arm": azure_arm,
            "credential": (
                self._autorestapi.get_boolean_value("add-credentials", False)
                or self._autorestapi.get_boolean_value("add-credential", False)
            ),
            "credential_scopes": credential_scopes.split(",") if credential_scopes else None,
            "head_as_boolean": self._autorestapi.get_boolean_value("head-as-boolean", False),
            "license_header": license_header,
            "keep_version_file": self._autorestapi.get_boolean_value("keep-version-file", False),
            "no_async": self._autorestapi.get_boolean_value("no-async", False),
            "no_namespace_folders": self._autorestapi.get_boolean_value("no-namespace-folders", False),
            "basic_setup_py": self._autorestapi.get_boolean_value("basic-setup-py", False),
            "package_name": self._autorestapi.get_value("package-name"),
            "package_version": self._autorestapi.get_value("package-version"),
            "client_side_validation": self._autorestapi.get_boolean_value("client-side-validation", True),
            "tracing": self._autorestapi.get_boolean_value("trace", False),
            "multiapi": self._autorestapi.get_boolean_value("multiapi", False)
        }

        if options["basic_setup_py"] and not options["package_version"]:
            raise ValueError("--basic-setup-py must be used with --package-version")

        # Force some options in ARM MODE:
        if azure_arm:
            options["credential"] = True
            options["head_as_boolean"] = True
        return options

    def process(self) -> bool:
        # List the input file, should be only one
        inputs = self._autorestapi.list_inputs()
        _LOGGER.debug("Possible Inputs: %s", inputs)
        if "code-model-v4-no-tags.yaml" not in inputs:
            raise ValueError("code-model-v4-no-tags.yaml must be a possible input")

        file_content = self._autorestapi.read_file("code-model-v4-no-tags.yaml")

        # Parse the received YAML
        yaml_data = yaml.safe_load(file_content)

        options = self._build_code_model_options()

        if options["azure_arm"]:
            self.remove_cloud_errors(yaml_data)

        code_model = self._create_code_model(yaml_data=yaml_data, options=options)

        serializer = JinjaSerializer(self._autorestapi)
        serializer.serialize(code_model)

        return True


def main(yaml_model_file: str) -> None:
    from ..jsonrpc.localapi import LocalAutorestAPI  # pylint: disable=import-outside-toplevel

    code_generator = CodeGenerator(autorestapi=LocalAutorestAPI(reachable_files=[yaml_model_file]))
    if not code_generator.process():
        raise SystemExit("Process didn't finish gracefully")


if __name__ == "__main__":
    main(sys.argv[1])
