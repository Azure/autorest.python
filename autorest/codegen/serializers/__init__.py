# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import re
import logging
from typing import Dict, List, Optional, Any, Union
from pathlib import Path
import black
from jinja2 import PackageLoader, Environment, FileSystemLoader, StrictUndefined

from autorest.codegen.models.credential_types import (
    AzureKeyCredentialType,
    TokenCredentialType,
)
from autorest.codegen.models.imports import FileImport, ImportType
from autorest.codegen.models.operation import OperationBase
from autorest.codegen.models.request_builder import OverloadedRequestBuilder

from ...jsonrpc import AutorestAPI
from ..models import CodeModel, OperationGroup, RequestBuilder
from ..models import TokenCredentialType
from .enum_serializer import EnumSerializer
from .general_serializer import GeneralSerializer
from .model_generic_serializer import ModelGenericSerializer
from .model_init_serializer import ModelInitSerializer
from .model_python3_serializer import ModelPython3Serializer
from .operations_init_serializer import OperationsInitSerializer
from .operation_groups_serializer import OperationGroupsSerializer
from .metadata_serializer import MetadataSerializer
from .request_builders_serializer import RequestBuildersSerializer
from .patch_serializer import PatchSerializer
from .sample_serializer import SampleSerializer
from ..models import BodyParameter
from .utils import SAMPLE_AAD_ANNOTATION, SAMPLE_KEY_ANNOTATION

_LOGGER = logging.getLogger(__name__)
_BLACK_MODE = black.Mode()

__all__ = [
    "JinjaSerializer",
]

_PACKAGE_FILES = [
    "CHANGELOG.md.jinja2",
    "dev_requirements.txt.jinja2",
    "LICENSE.jinja2",
    "MANIFEST.in.jinja2",
    "README.md.jinja2",
    "setup.py.jinja2",
]

_REGENERATE_FILES = {"setup.py", "MANIFEST.in"}


class JinjaSerializer:
    def __init__(self, autorestapi: AutorestAPI, code_model: CodeModel) -> None:
        self._autorestapi = autorestapi
        self.code_model = code_model

    @property
    def has_aio_folder(self) -> bool:
        return not self.code_model.options["no_async"] and bool(
            self.code_model.request_builders
        )

    def serialize(self) -> None:
        env = Environment(
            loader=PackageLoader("autorest.codegen", "templates"),
            keep_trailing_newline=True,
            line_statement_prefix="##",
            line_comment_prefix="###",
            trim_blocks=True,
            lstrip_blocks=True,
        )

        namespace_path = (
            Path(".")
            if self.code_model.options["no_namespace_folders"]
            else Path(*(self.code_model.namespace.split(".")))
        )
        # if there was a patch file before, we keep it
        self._keep_patch_file(namespace_path / Path("_patch.py"), env)
        if self.has_aio_folder:
            self._keep_patch_file(namespace_path / Path("aio") / Path("_patch.py"), env)

        if self.code_model.options["models_mode"] and (
            self.code_model.model_types or self.code_model.enums
        ):
            self._keep_patch_file(
                namespace_path / Path("models") / Path("_patch.py"), env
            )
        if (
            self.code_model.options["show_operations"]
            and self.code_model.operation_groups
        ):
            self._keep_patch_file(
                namespace_path
                / Path(self.code_model.operations_folder_name)
                / Path("_patch.py"),
                env,
            )
            if self.has_aio_folder:
                self._keep_patch_file(
                    namespace_path
                    / Path("aio")
                    / Path(self.code_model.operations_folder_name)
                    / Path("_patch.py"),
                    env,
                )

        self._serialize_and_write_top_level_folder(
            env=env, namespace_path=namespace_path
        )

        if self.code_model.request_builders:
            if self.code_model.options["builders_visibility"] != "embedded":
                self._serialize_and_write_rest_layer(
                    env=env, namespace_path=namespace_path
                )
            if self.has_aio_folder:
                self._serialize_and_write_aio_top_level_folder(
                    env=env,
                    namespace_path=namespace_path,
                )

        if (
            self.code_model.options["show_operations"]
            and self.code_model.operation_groups
        ):
            self._serialize_and_write_operations_folder(
                env=env, namespace_path=namespace_path
            )
            if self.code_model.options["multiapi"]:
                self._serialize_and_write_metadata(
                    env=env, namespace_path=namespace_path
                )

        if self.code_model.options["models_mode"] and (
            self.code_model.model_types or self.code_model.enums
        ):
            self._serialize_and_write_models_folder(
                env=env, namespace_path=namespace_path
            )
        if not self.code_model.options["models_mode"]:
            # keep models file if users ended up just writing a models file
            if self._autorestapi.read_file(namespace_path / Path("models.py")):
                self._autorestapi.write_file(
                    namespace_path / Path("models.py"),
                    self._autorestapi.read_file(namespace_path / Path("models.py")),
                )

        if self.code_model.options["package_mode"]:
            self._serialize_and_write_package_files(namespace_path)

        if (
            self.code_model.options["show_operations"]
            and self.code_model.operation_groups
            and self.code_model.options["generate_sample"]
        ):
            self._serialize_and_write_sample_folder(
                env=env, namespace_path=namespace_path
            )

    def _serialize_and_write_package_files(self, out_path: Path) -> None:
        def _serialize_and_write_package_files_proc(**kwargs: Any):
            for template_name in package_files:
                file = template_name.replace(".jinja2", "")
                output_name = out_path / file
                if (
                    not self._autorestapi.read_file(output_name)
                    or file in _REGENERATE_FILES
                ):
                    template = env.get_template(template_name)
                    render_result = template.render(**kwargs)
                    self._autorestapi.write_file(output_name, render_result)

        def _prepare_params() -> Dict[Any, Any]:
            package_parts = self.code_model.options["package_name"].split("-")[:-1]
            token_cred = isinstance(
                getattr(self.code_model.credential, "type", None), TokenCredentialType
            )
            version = self.code_model.options["package_version"]
            if any(x in version for x in ["a", "b", "rc"]) or version[0] == "0":
                dev_status = "4 - Beta"
            else:
                dev_status = "5 - Production/Stable"
            params = {
                "token_credential": token_cred,
                "pkgutil_names": [
                    ".".join(package_parts[: i + 1]) for i in range(len(package_parts))
                ],
                "init_names": [
                    "/".join(package_parts[: i + 1]) + "/__init__.py"
                    for i in range(len(package_parts))
                ],
                "dev_status": dev_status,
                "client_name": self.code_model.client.name,
                "namespace": self.code_model.namespace,
                "code_model": self.code_model,
            }
            params.update(self.code_model.options)
            params.update(self.code_model.package_dependency)
            return params

        out_path = self._package_root_folder(out_path)
        if self.code_model.options["package_mode"] in ("dataplane", "mgmtplane"):
            env = Environment(
                loader=PackageLoader("autorest.codegen", "templates"),
                undefined=StrictUndefined,
            )
            package_files = _PACKAGE_FILES
            _serialize_and_write_package_files_proc(**_prepare_params())
        elif Path(self.code_model.options["package_mode"]).exists():
            env = Environment(
                loader=FileSystemLoader(
                    str(Path(self.code_model.options["package_mode"]))
                ),
                keep_trailing_newline=True,
                undefined=StrictUndefined,
            )
            package_files = env.list_templates()
            params = self.code_model.options["package_configuration"] or {}
            _serialize_and_write_package_files_proc(**params)

    def _keep_patch_file(self, path_file: Path, env: Environment):
        if self._autorestapi.read_file(path_file):
            self._autorestapi.write_file(
                path_file, self._autorestapi.read_file(path_file)
            )
        else:
            self._autorestapi.write_file(
                path_file,
                PatchSerializer(env=env, code_model=self.code_model).serialize(),
            )

    def _serialize_and_write_models_folder(
        self, env: Environment, namespace_path: Path
    ) -> None:
        # Write the models folder
        models_path = namespace_path / Path("models")
        if self.code_model.model_types:
            if not self.code_model.options["python3_only"]:
                self._autorestapi.write_file(
                    models_path
                    / Path(
                        f"{self.code_model.get_models_filename(is_python3_file=False)}.py"
                    ),
                    ModelGenericSerializer(
                        code_model=self.code_model, env=env
                    ).serialize(),
                )
            self._autorestapi.write_file(
                models_path
                / Path(
                    f"{self.code_model.get_models_filename(is_python3_file=True)}.py"
                ),
                ModelPython3Serializer(code_model=self.code_model, env=env).serialize(),
            )
        if self.code_model.enums:
            self._autorestapi.write_file(
                models_path / Path(f"{self.code_model.enums_filename}.py"),
                EnumSerializer(code_model=self.code_model, env=env).serialize(),
            )
        self._autorestapi.write_file(
            models_path / Path("__init__.py"),
            ModelInitSerializer(code_model=self.code_model, env=env).serialize(),
        )

    def _serialize_and_write_rest_layer(
        self, env: Environment, namespace_path: Path
    ) -> None:
        rest_path = namespace_path / Path(self.code_model.rest_layer_name)
        group_names = {rb.group_name for rb in self.code_model.request_builders}

        for group_name in group_names:
            request_builders = [
                r
                for r in self.code_model.request_builders
                if r.group_name == group_name
            ]
            self._serialize_and_write_single_rest_layer(
                env, rest_path, request_builders
            )
        if not "" in group_names:
            self._autorestapi.write_file(
                rest_path / Path("__init__.py"),
                self.code_model.options["license_header"],
            )

    def _serialize_and_write_single_rest_layer(
        self,
        env: Environment,
        rest_path: Path,
        request_builders: List[Union[RequestBuilder, OverloadedRequestBuilder]],
    ) -> None:
        group_name = request_builders[0].group_name
        output_path = rest_path / Path(group_name) if group_name else rest_path
        # write generic request builders file
        self._autorestapi.write_file(
            output_path / Path("_request_builders.py"),
            RequestBuildersSerializer(
                code_model=self.code_model,
                env=env,
                request_builders=request_builders,
                is_python3_file=False,
            ).serialize_request_builders(),
        )

        # write python3 request builders file
        self._autorestapi.write_file(
            output_path / Path("_request_builders_py3.py"),
            RequestBuildersSerializer(
                code_model=self.code_model,
                env=env,
                request_builders=request_builders,
                is_python3_file=True,
            ).serialize_request_builders(),
        )

        # write rest init file
        self._autorestapi.write_file(
            output_path / Path("__init__.py"),
            RequestBuildersSerializer(
                code_model=self.code_model,
                env=env,
                request_builders=request_builders,
                is_python3_file=True,
            ).serialize_init(),
        )

    def _serialize_and_write_operations_file(
        self,
        env: Environment,
        namespace_path: Path,
        operation_group: Optional[OperationGroup] = None,
    ) -> None:
        filename = operation_group.filename if operation_group else "_operations"
        # write first sync file
        operation_group_serializer = OperationGroupsSerializer(
            code_model=self.code_model,
            env=env,
            async_mode=False,
            is_python3_file=self.code_model.options["python3_only"],
            operation_group=operation_group,
        )
        self._autorestapi.write_file(
            namespace_path
            / Path(self.code_model.operations_folder_name)
            / Path(f"{filename}.py"),
            operation_group_serializer.serialize(),
        )

        if (
            not self.code_model.options["python3_only"]
            and self.code_model.options["add_python3_operation_files"]
        ):
            # write typed second file if not python 3 only
            operation_group_serializer = OperationGroupsSerializer(
                code_model=self.code_model,
                env=env,
                async_mode=False,
                is_python3_file=True,
            )
            self._autorestapi.write_file(
                namespace_path
                / Path(self.code_model.operations_folder_name)
                / Path(f"{filename}_py3.py"),
                operation_group_serializer.serialize(),
            )

        if self.has_aio_folder:
            # write async operation group and operation files
            operation_group_async_serializer = OperationGroupsSerializer(
                code_model=self.code_model,
                env=env,
                async_mode=True,
                is_python3_file=True,
                operation_group=operation_group,
            )
            self._autorestapi.write_file(
                (
                    namespace_path
                    / Path("aio")
                    / Path(self.code_model.operations_folder_name)
                    / Path(f"{filename}.py")
                ),
                operation_group_async_serializer.serialize(),
            )

    def _serialize_and_write_operations_folder(
        self, env: Environment, namespace_path: Path
    ) -> None:
        # write sync operations init file
        operations_init_serializer = OperationsInitSerializer(
            code_model=self.code_model, env=env, async_mode=False
        )
        self._autorestapi.write_file(
            namespace_path
            / Path(self.code_model.operations_folder_name)
            / Path("__init__.py"),
            operations_init_serializer.serialize(),
        )

        # write async operations init file
        if self.has_aio_folder:
            operations_async_init_serializer = OperationsInitSerializer(
                code_model=self.code_model, env=env, async_mode=True
            )
            self._autorestapi.write_file(
                namespace_path
                / Path("aio")
                / Path(self.code_model.operations_folder_name)
                / Path("__init__.py"),
                operations_async_init_serializer.serialize(),
            )

        if self.code_model.options["combine_operation_files"]:
            self._serialize_and_write_operations_file(
                env=env,
                namespace_path=namespace_path,
            )
        else:
            for operation_group in self.code_model.operation_groups:
                self._serialize_and_write_operations_file(
                    env=env,
                    namespace_path=namespace_path,
                    operation_group=operation_group,
                )

    def _serialize_and_write_version_file(
        self, namespace_path: Path, general_serializer: GeneralSerializer
    ):
        def _read_version_file(original_version_file_name: str) -> str:
            return self._autorestapi.read_file(
                namespace_path / original_version_file_name
            )

        def _write_version_file(original_version_file_name: str) -> None:
            self._autorestapi.write_file(
                namespace_path / Path("_version.py"),
                _read_version_file(original_version_file_name),
            )

        keep_version_file = self.code_model.options["keep_version_file"]
        if keep_version_file and _read_version_file("_version.py"):
            _write_version_file(original_version_file_name="_version.py")
        elif keep_version_file and _read_version_file("version.py"):
            _write_version_file(original_version_file_name="version.py")
        elif self.code_model.options["package_version"]:
            self._autorestapi.write_file(
                namespace_path / Path("_version.py"),
                general_serializer.serialize_version_file(),
            )

    def _serialize_and_write_top_level_folder(
        self, env: Environment, namespace_path: Path
    ) -> None:
        general_serializer = GeneralSerializer(
            code_model=self.code_model, env=env, async_mode=False
        )

        self._autorestapi.write_file(
            namespace_path / Path("__init__.py"),
            general_serializer.serialize_init_file(),
        )
        p = namespace_path.parent
        while p != Path("."):
            # write pkgutil init file
            self._autorestapi.write_file(
                p / Path("__init__.py"),
                general_serializer.serialize_pkgutil_init_file(),
            )
            p = p.parent

        # Write the service client
        if self.code_model.request_builders:
            self._autorestapi.write_file(
                namespace_path / Path(f"{self.code_model.client.filename}.py"),
                general_serializer.serialize_service_client_file(),
            )

        if self.code_model.need_vendored_code(async_mode=False):
            self._autorestapi.write_file(
                namespace_path / Path("_vendor.py"),
                general_serializer.serialize_vendor_file(),
            )

        self._serialize_and_write_version_file(namespace_path, general_serializer)

        # write the empty py.typed file
        self._autorestapi.write_file(
            namespace_path / Path("py.typed"), "# Marker file for PEP 561."
        )

        # Write the config file
        if self.code_model.request_builders:
            self._autorestapi.write_file(
                namespace_path / Path("_configuration.py"),
                general_serializer.serialize_config_file(),
            )

        # Write the setup file
        if self.code_model.options["basic_setup_py"]:
            self._autorestapi.write_file(
                Path("setup.py"), general_serializer.serialize_setup_file()
            )

    def _serialize_and_write_aio_top_level_folder(
        self, env: Environment, namespace_path: Path
    ) -> None:
        aio_general_serializer = GeneralSerializer(
            code_model=self.code_model, env=env, async_mode=True
        )

        aio_path = namespace_path / Path("aio")

        # Write the __init__ file
        self._autorestapi.write_file(
            aio_path / Path("__init__.py"), aio_general_serializer.serialize_init_file()
        )

        # Write the service client
        if self.code_model.request_builders:
            self._autorestapi.write_file(
                aio_path / Path(f"{self.code_model.client.filename}.py"),
                aio_general_serializer.serialize_service_client_file(),
            )

        # Write the config file
        self._autorestapi.write_file(
            aio_path / Path("_configuration.py"),
            aio_general_serializer.serialize_config_file(),
        )
        if self.code_model.need_vendored_code(async_mode=True):
            self._autorestapi.write_file(
                aio_path / Path("_vendor.py"),
                aio_general_serializer.serialize_vendor_file(),
            )

    def _serialize_and_write_metadata(
        self, env: Environment, namespace_path: Path
    ) -> None:
        metadata_serializer = MetadataSerializer(self.code_model, env)
        self._autorestapi.write_file(
            namespace_path / Path("_metadata.json"), metadata_serializer.serialize()
        )

    def _package_root_folder(self, namespace_path: Path) -> Path:
        count = (self.code_model.options.get("package_name") or "").count("-")
        extra = 2 if self.code_model.options["multiapi"] else 1
        for _ in range(count + extra):
            namespace_path = namespace_path / Path("..")
        return namespace_path

    def _prepare_sample_render_param(self) -> Dict[Any, Any]:
        # client params
        credential = ""
        annotation = ""
        credential_type = getattr(self.code_model.credential, "type", None)
        if isinstance(credential_type, TokenCredentialType):
            credential = "DefaultAzureCredential"
            annotation = SAMPLE_AAD_ANNOTATION
        elif isinstance(credential_type, AzureKeyCredentialType):
            credential = "AzureKeyCredential"
            annotation = SAMPLE_KEY_ANNOTATION

        addtional_info = (
            'key=os.getenv("AZURE_KEY")' if credential == "AzureKeyCredential" else ""
        )
        special_param = {
            "credential": f"{credential}({addtional_info})",
        }
        params_positional = [
            p
            for p in self.code_model.client.parameters.positional
            if not (p.optional or p.client_default_value)
        ]
        client_params = {
            p.client_name: special_param.get(
                p.client_name, f'"{p.client_name.upper()}"'
            )
            for p in params_positional
        }

        # imports
        imports = FileImport()
        namespace = (self.code_model.options["package_name"] or "").replace(
            "-", "."
        ) or self.code_model.namespace
        imports.add_submodule_import(
            namespace, self.code_model.client.name, ImportType.THIRDPARTY
        )
        if credential:
            imports.add_submodule_import(
                "azure.identity", credential, ImportType.THIRDPARTY
            )

        return {
            "imports": imports,
            "client_params": client_params,
            "annotation": annotation,
        }

    @staticmethod
    def _operation_additional(operation: OperationBase[Any]) -> str:
        lro = ".result()"
        paging = "\n    response = [item for item in response]"
        if operation.operation_type == "paging":
            return "\n    response = [item for item in response]"
        if operation.operation_type == "lro":
            return ".result()"
        if operation.operation_type == "lropaging":
            return lro + paging
        return ""

    @staticmethod
    def _to_lower_camel_case(name: str) -> str:
        return re.sub(r"_([a-z])", lambda x: x.group(1).upper(), name)

    @staticmethod
    def _to_snake_case(name: str) -> str:
        return re.sub(
            "((?!^)(?<!_)[A-Z][a-z]+|(?<=[a-z0-9])[A-Z])",
            r"_\1",
            name.replace("-", "").replace(" ", "_"),
        ).lower()

    def _serialize_and_write_sample_folder(
        self, env: Environment, namespace_path: Path
    ) -> None:
        out_path = self._package_root_folder(namespace_path) / Path("generated_samples")
        sample_params = self._prepare_sample_render_param()
        cls = lambda x: f'"{x}"' if isinstance(x, str) else str(x)
        failure_info = '"fail to find required param named {%s} in example file {%s}"'
        # pylint: disable=too-many-nested-blocks
        for operation_group in self.code_model.operation_groups:
            if self.code_model.options["multiapi"]:
                api_version_folder = f"{operation_group.api_versions[0]}/"
                sample_params["client_params"][
                    "api_version"
                ] = f'"{operation_group.api_versions[0]}"'
            else:
                api_version_folder = ""
            for operation in operation_group.operations:
                samples = operation.yaml_data["samples"]
                if not samples:
                    continue
                params_positional = [
                    p
                    for p in operation.parameters.positional
                    if not p.client_default_value
                ]
                operation_result = self._operation_additional(operation)
                for key, value in samples.items():
                    # update client parameters if it is defined in example files
                    for param in sample_params["client_params"].keys():
                        param_value = value["parameters"].get(
                            self._to_lower_camel_case(param)
                        )
                        if param_value:
                            sample_params["client_params"][param] = f'"{param_value}"'

                    # prepare method parameters
                    operation_params = {}
                    for param in params_positional:
                        if isinstance(param, BodyParameter):
                            name = self._to_lower_camel_case(param.client_name)
                            fake_value = '"can not find valie value"'
                        else:
                            name = param.rest_api_name
                            fake_value = param.client_name.upper()

                        param_value = value["parameters"].get(name)
                        if param_value or not param.optional:
                            if not param_value:
                                # if can't find required param, need to log it
                                _LOGGER.warning(failure_info, name, key)
                                param_value = fake_value
                            operation_params[param.client_name] = cls(param_value)

                    # serialize and output
                    try:
                        file_name = self._to_snake_case(key) + ".py"
                        sample_params["file_name"] = file_name
                        file_str = SampleSerializer(
                            code_model=self.code_model,
                            env=env,
                            operation_group_name=operation_group.property_name,
                            operation_name=operation.name,
                            operation_params=operation_params,
                            sample_params=sample_params,
                            operation_result=operation_result,
                            origin_file=value.get("x-ms-original-file"),
                        ).serialize()
                        self._autorestapi.write_file(
                            out_path / f"{api_version_folder}{file_name}",
                            black.format_file_contents(
                                file_str, fast=True, mode=_BLACK_MODE
                            ),
                        )
                    except Exception as e:  # pylint: disable=broad-except
                        # sample generation shall not block code generation, so just log error
                        _LOGGER.error(
                            "error happens when generate sample with {%s}: {%s}", key, e
                        )
