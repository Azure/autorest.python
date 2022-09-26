# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Dict, Any, Union, cast
from pathlib import Path
import yaml


from .. import Plugin
from ..utils import parse_args
from .models.client import Client, Config
from .models.code_model import CodeModel
from .models import build_type
from .models.request_builder import get_request_builder
from .models.operation_group import OperationGroup
from .serializers import JinjaSerializer
from ._utils import DEFAULT_HEADER_TEXT


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

    if options["models_mode"] not in ["msrest", "dpg", "none"]:
        raise ValueError(
            "--models-mode can only be 'msrest', 'dpg' or 'none'. "
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
            "dependency_azure_mgmt_core": "azure-mgmt-core<2.0.0,>=1.3.2",
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
        """Build an options dict from the user input while running autorest."""
        azure_arm = self.options.get("azure-arm", False)
        license_header = self.options.get("header-text", DEFAULT_HEADER_TEXT)
        if license_header:
            license_header = license_header.replace("\n", "\n# ")
            license_header = (
                "# --------------------------------------------------------------------------\n# "
                + license_header
            )
            license_header += "\n# --------------------------------------------------------------------------"

        low_level_client = cast(bool, self.options.get("low-level-client", False))
        version_tolerant = cast(bool, self.options.get("version-tolerant", True))
        show_operations = self.options.get("show-operations", not low_level_client)

        options: Dict[str, Any] = {
            "azure_arm": azure_arm,
            "head_as_boolean": self.options.get("head-as-boolean", True),
            "license_header": license_header,
            "keep_version_file": self.options.get("keep-version-file", False),
            "no_async": self.options.get("no-async", False),
            "no_namespace_folders": self.options.get("no-namespace-folders", False),
            "basic_setup_py": self.options.get("basic-setup-py", False),
            "package_name": self.options.get("package-name"),
            "package_version": self.options.get("package-version"),
            "client_side_validation": self.options.get("client-side-validation", False),
            "tracing": self.options.get("tracing", show_operations),
            "multiapi": self.options.get("multiapi", False),
            "polymorphic_examples": self.options.get("polymorphic-examples", 5),
            "models_mode": self.options.get("models-mode", "dpg").lower(),
            "builders_visibility": self.options.get("builders-visibility"),
            "show_operations": show_operations,
            "show_send_request": self.options.get(
                "show-send-request", low_level_client or version_tolerant
            ),
            "only_path_and_body_params_positional": self.options.get(
                "only-path-and-body-params-positional",
                low_level_client or version_tolerant,
            ),
            "version_tolerant": version_tolerant,
            "low_level_client": low_level_client,
            "combine_operation_files": self.options.get(
                "combine-operation-files", version_tolerant
            ),
            "package_mode": self.options.get("package-mode"),
            "package_pprint_name": self.options.get("package-pprint-name"),
            "package_configuration": self.options.get("package-configuration"),
            "default_optional_constants_to_none": self.options.get(
                "default-optional-constants-to-none",
                low_level_client or version_tolerant,
            ),
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

    def get_yaml(self) -> Dict[str, Any]:
        # cadl file doesn't have to be relative to output folder
        with open(self.options["cadl_file"], "r", encoding="utf-8") as fd:
            return yaml.safe_load(fd.read())

    def get_serializer(self, code_model: CodeModel):
        return JinjaSerializer(code_model, output_folder=self.output_folder)

    def process(self) -> bool:
        # List the input file, should be only one

        options = self._build_code_model_options()
        yaml_data = self.get_yaml()

        if options["azure_arm"]:
            self.remove_cloud_errors(yaml_data)

        code_model = self._create_code_model(yaml_data=yaml_data, options=options)

        serializer = self.get_serializer(code_model)
        serializer.serialize()

        return True


if __name__ == "__main__":
    # CADL pipeline will call this
    args, additional_args = parse_args()
    CodeGenerator(
        output_folder=args.output_folder, cadl_file=args.cadl_file, **additional_args
    ).process()
