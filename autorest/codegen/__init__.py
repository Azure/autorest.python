# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
import sys
from typing import Dict, Any, Union, cast
from pathlib import Path
import yaml


from .. import Plugin
from .models.client import Client, Config
from .models.code_model import CodeModel
from .models import build_type
from .models.request_builder import get_request_builder
from .models.operation_group import OperationGroup
from .serializers import JinjaSerializer


def _build_convenience_layer(yaml_data: Dict[str, Any], code_model: CodeModel) -> None:
    # Create operations
    if code_model.options["show_operations"] and yaml_data.get("operationGroups"):
        code_model.operation_groups = [
            OperationGroup.from_yaml(op_group, code_model)
            for op_group in yaml_data["operationGroups"]
        ]
    if yaml_data.get("types"):
        if code_model.options["models_mode"]:
            code_model.sort_model_types()

    if code_model.options["show_operations"]:
        # LRO operation
        code_model.format_lro_operations()


def _validate_code_model_options(options: Dict[str, Any]) -> None:

    if options["builders_visibility"] not in ["public", "hidden", "embedded"]:
        raise ValueError(
            "The value of --builders-visibility must be either 'public', 'hidden', "
            "or 'embedded'"
        )

    if options["models_mode"] not in ["msrest", "none"]:
        raise ValueError(
            "--models-mode can only be 'msrest' or 'none'. "
            "Pass in 'msrest' if you want msrest models, or "
            "'none' if you don't want any."
        )

    if not options["show_operations"] and options["builders_visibility"] == "embedded":
        raise ValueError(
            "Can not embed builders without operations. "
            "Either set --show-operations to True, or change the value of --builders-visibility "
            "to 'public' or 'hidden'."
        )

    if options["basic_setup_py"] and not options["package_version"]:
        raise ValueError("--basic-setup-py must be used with --package-version")

    if options["package_mode"] and not options["package_version"]:
        raise ValueError("--package-mode must be used with --package-version")

    if not options["show_operations"] and options["combine_operation_files"]:
        raise ValueError(
            "Can not combine operation files if you are not showing operations. "
            "If you want operation files, pass in flag --show-operations"
        )

    if options["package_mode"]:
        if (
            options["package_mode"] not in ("mgmtplane", "dataplane")
            and not Path(options["package_mode"]).exists()
        ):
            raise ValueError(
                "--package-mode can only be 'mgmtplane' or 'dataplane' or directory which contains template files"
            )

    if options["multiapi"] and options["version_tolerant"]:
        raise ValueError(
            "Can not currently generate version tolerant multiapi SDKs. "
            "We are working on creating a new multiapi SDK for version tolerant and it is not available yet."
        )

    if options["client_side_validation"] and options["version_tolerant"]:
        raise ValueError(
            "Can not generate version tolerant with --client-side-validation. "
        )


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
                    if (
                        exception.get("schema")
                        and exception["schema"]["language"]["default"]["name"]
                        == "CloudError"
                    ):
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
    def _build_package_dependency() -> Dict[str, str]:
        return {
            "dependency_azure_mgmt_core": "azure-mgmt-core<2.0.0,>=1.3.0",
            "dependency_azure_core": "azure-core<2.0.0,>=1.24.0",
            "dependency_msrest": "msrest>=0.7.1",
        }

    def _create_code_model(
        self, yaml_data: Dict[str, Any], options: Dict[str, Union[str, bool]]
    ) -> CodeModel:
        # Create a code model

        code_model = CodeModel(yaml_data, options=options)
        for type_yaml in yaml_data.get("types", []):
            build_type(yaml_data=type_yaml, code_model=code_model)

        code_model.client = Client.from_yaml(yaml_data["client"], code_model)
        code_model.config = Config.from_yaml(yaml_data["client"], code_model)

        # Build request builders
        if yaml_data.get("operationGroups"):
            for og_group in yaml_data["operationGroups"]:
                for operation_yaml in og_group["operations"]:
                    request_builder = get_request_builder(
                        operation_yaml, code_model=code_model
                    )
                    if request_builder.overloads:
                        code_model.request_builders.extend(request_builder.overloads)  # type: ignore
                    code_model.request_builders.append(request_builder)
                    if operation_yaml.get("nextOperation"):
                        # i am a paging operation and i have a next operation. Make sure to include my next operation
                        code_model.request_builders.append(
                            get_request_builder(
                                operation_yaml["nextOperation"], code_model=code_model
                            )
                        )

        _build_convenience_layer(yaml_data=yaml_data, code_model=code_model)
        code_model.package_dependency = self._build_package_dependency()
        return code_model

    def _build_code_model_options(self) -> Dict[str, Any]:
        """Build en options dict from the user input while running autorest."""
        azure_arm = self._autorestapi.get_boolean_value("azure-arm", False)
        license_header = self._autorestapi.get_value("header-text")
        if license_header:
            license_header = license_header.replace("\n", "\n# ")
            license_header = (
                "# --------------------------------------------------------------------------\n# "
                + license_header
            )
            license_header += "\n# --------------------------------------------------------------------------"

        low_level_client = cast(
            bool, self._autorestapi.get_boolean_value("low-level-client", False)
        )
        version_tolerant = cast(
            bool, self._autorestapi.get_boolean_value("version-tolerant")
        )
        show_operations = self._autorestapi.get_boolean_value(
            "show-operations", not low_level_client
        )
        models_mode_default = (
            "none" if low_level_client or version_tolerant else "msrest"
        )
        if self._autorestapi.get_boolean_value("python3-only") is False:
            _LOGGER.warning(
                "You have passed in --python3-only=False. We have force overriden "
                "this to True."
            )
        if self._autorestapi.get_boolean_value("add-python3-operation-files"):
            _LOGGER.warning(
                "You have passed in --add-python3-operation-files. "
                "This flag no longer has an effect bc all SDKs are now Python3 only."
            )
        if self._autorestapi.get_boolean_value("reformat-next-link"):
            _LOGGER.warning(
                "You have passed in --reformat-next-link. We have force overriden "
                "this to False because we no longer reformat initial query parameters into next "
                "calls unless explicitly defined in the service definition."
            )

        options: Dict[str, Any] = {
            "azure_arm": azure_arm,
            "head_as_boolean": self._autorestapi.get_boolean_value(
                "head-as-boolean", False
            ),
            "license_header": license_header,
            "keep_version_file": self._autorestapi.get_boolean_value(
                "keep-version-file", False
            ),
            "no_async": self._autorestapi.get_boolean_value("no-async", False),
            "no_namespace_folders": self._autorestapi.get_boolean_value(
                "no-namespace-folders", False
            ),
            "basic_setup_py": self._autorestapi.get_boolean_value(
                "basic-setup-py", False
            ),
            "package_name": self._autorestapi.get_value("package-name"),
            "package_version": self._autorestapi.get_value("package-version"),
            "client_side_validation": self._autorestapi.get_boolean_value(
                "client-side-validation", False
            ),
            "tracing": self._autorestapi.get_boolean_value("trace", show_operations),
            "multiapi": self._autorestapi.get_boolean_value("multiapi", False),
            "polymorphic_examples": self._autorestapi.get_value("polymorphic-examples")
            or 5,
            "models_mode": (
                self._autorestapi.get_value("models-mode") or models_mode_default
            ).lower(),
            "builders_visibility": self._autorestapi.get_value("builders-visibility"),
            "show_operations": show_operations,
            "show_send_request": self._autorestapi.get_boolean_value(
                "show-send-request", low_level_client or version_tolerant
            ),
            "only_path_and_body_params_positional": self._autorestapi.get_boolean_value(
                "only-path-and-body-params-positional",
                low_level_client or version_tolerant,
            ),
            "version_tolerant": version_tolerant,
            "low_level_client": low_level_client,
            "combine_operation_files": self._autorestapi.get_boolean_value(
                "combine-operation-files", version_tolerant
            ),
            "package_mode": self._autorestapi.get_value("package-mode"),
            "package_pprint_name": self._autorestapi.get_value("package-pprint-name"),
            "package_configuration": self._autorestapi.get_value(
                "package-configuration"
            ),
            "default_optional_constants_to_none": self._autorestapi.get_boolean_value(
                "default-optional-constants-to-none",
                low_level_client or version_tolerant,
            ),
            "clear_python_folder": self._autorestapi.get_value("clear-python-folder"),
        }

        if options["builders_visibility"] is None:
            options["builders_visibility"] = (
                "public" if low_level_client else "embedded"
            )
        else:
            options["builders_visibility"] = options["builders_visibility"].lower()

        _validate_code_model_options(options)

        if options["models_mode"] == "none":
            # switch to falsy value for easier code writing
            options["models_mode"] = False

        # Force some options in ARM MODE:
        if azure_arm:
            options["head_as_boolean"] = True
        return options

    def process(self) -> bool:
        # List the input file, should be only one
        inputs = self._autorestapi.list_inputs()
        _LOGGER.debug("Possible Inputs: %s", inputs)
        if "code-model-v4-no-tags.yaml" not in inputs:
            raise ValueError("code-model-v4-no-tags.yaml must be a possible input")

        if self._autorestapi.get_value("input-yaml"):
            input_yaml = self._autorestapi.get_value("input-yaml")
            file_content = self._autorestapi.read_file(input_yaml)
        else:
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

        serializer = JinjaSerializer(self._autorestapi, code_model)
        serializer.serialize()

        return True


def main(yaml_model_file: str) -> None:
    from ..jsonrpc.localapi import (  # pylint: disable=import-outside-toplevel
        LocalAutorestAPI,
    )

    code_generator = CodeGenerator(
        autorestapi=LocalAutorestAPI(reachable_files=[yaml_model_file])
    )
    if not code_generator.process():
        raise SystemExit("Process didn't finish gracefully")


if __name__ == "__main__":
    main(sys.argv[1])
