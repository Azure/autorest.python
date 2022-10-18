# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List, Optional, Any, Union, cast
from pathlib import Path
from jinja2 import PackageLoader, Environment, FileSystemLoader, StrictUndefined

from ... import ReaderAndWriter, ReaderAndWriterAutorest
from ...jsonrpc import AutorestAPI
from ..models import (
    OperationGroup,
    RequestBuilder,
    OverloadedRequestBuilder,
    NamespaceModel,
    CodeModel,
)
from .enum_serializer import EnumSerializer
from .general_serializer import GeneralNamespaceSerializer, GeneralSerializer
from .model_init_serializer import ModelInitSerializer
from .model_serializer import DpgModelSerializer, MsrestModelSerializer
from .operations_init_serializer import OperationsInitSerializer
from .operation_groups_serializer import OperationGroupsSerializer
from .metadata_serializer import MetadataSerializer
from .request_builders_serializer import RequestBuildersSerializer
from .patch_serializer import PatchSerializer

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


class JinjaSerializer(ReaderAndWriter):  # pylint: disable=abstract-method
    def __init__(
        self,
        code_model: CodeModel,
        namespace_model: NamespaceModel,
        *,
        output_folder: Union[str, Path],
        **kwargs: Any,
    ) -> None:
        super().__init__(output_folder=output_folder, **kwargs)
        self.code_model = code_model
        self.namespace_model = namespace_model

    @property
    def has_aio_folder(self) -> bool:
        return not self.namespace_model.options["no_async"] and bool(
            self.namespace_model.operation_groups
        )

    @property
    def has_operations_folder(self) -> bool:
        return self.namespace_model.options["show_operations"] and bool(
            self.namespace_model.operation_groups
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
            if self.namespace_model.options["no_namespace_folders"]
            else Path(*(self.namespace_model.namespace.split(".")))
        )
        # if there was a patch file before, we keep it
        self._keep_patch_file(namespace_path / Path("_patch.py"), env)
        if self.has_aio_folder:
            self._keep_patch_file(namespace_path / Path("aio") / Path("_patch.py"), env)

        if self.namespace_model.options["models_mode"] and (
            self.namespace_model.model_types or self.namespace_model.enums
        ):
            self._keep_patch_file(
                namespace_path / Path("models") / Path("_patch.py"), env
            )
        if self.has_operations_folder:
            self._keep_patch_file(
                namespace_path
                / Path(self.namespace_model.operations_folder_name)
                / Path("_patch.py"),
                env,
            )
            if self.has_aio_folder:
                self._keep_patch_file(
                    namespace_path
                    / Path("aio")
                    / Path(self.namespace_model.operations_folder_name)
                    / Path("_patch.py"),
                    env,
                )

        self._serialize_and_write_top_level_folder(
            env=env, namespace_path=namespace_path
        )

        if self.namespace_model.operation_groups:
            if self.namespace_model.options["builders_visibility"] != "embedded":
                self._serialize_and_write_rest_layer(
                    env=env, namespace_path=namespace_path
                )
            if self.has_aio_folder:
                self._serialize_and_write_aio_top_level_folder(
                    env=env,
                    namespace_path=namespace_path,
                )

        if self.has_operations_folder:
            self._serialize_and_write_operations_folder(
                env=env, namespace_path=namespace_path
            )
            if self.namespace_model.options["multiapi"]:
                self._serialize_and_write_metadata(
                    env=env, namespace_path=namespace_path
                )

        if self.namespace_model.options["models_mode"] and (
            self.namespace_model.model_types or self.namespace_model.enums
        ):
            self._serialize_and_write_models_folder(
                env=env, namespace_path=namespace_path
            )
        if not self.namespace_model.options["models_mode"]:
            # keep models file if users ended up just writing a models file
            if self.read_file(namespace_path / Path("models.py")):
                self.write_file(
                    namespace_path / Path("models.py"),
                    cast(str, self.read_file(namespace_path / Path("models.py"))),
                )

        if self.namespace_model.options["package_mode"]:
            self._serialize_and_write_package_files(namespace_path=namespace_path)

    def _serialize_and_write_package_files(self, namespace_path: Path) -> None:
        root_of_sdk = namespace_path / Path(
            "../" * (self.namespace_model.namespace.count(".") + 1)
        )
        if self.namespace_model.options["package_mode"] in ("dataplane", "mgmtplane"):
            env = Environment(
                loader=PackageLoader(
                    "autorest.codegen", "templates/packaging_templates"
                ),
                undefined=StrictUndefined,
            )

            package_files = _PACKAGE_FILES
        elif Path(self.namespace_model.options["package_mode"]).exists():
            env = Environment(
                loader=FileSystemLoader(
                    str(Path(self.namespace_model.options["package_mode"]))
                ),
                keep_trailing_newline=True,
                undefined=StrictUndefined,
            )
            package_files = env.list_templates()
        else:
            return
        serializer = GeneralSerializer(self.code_model, env)
        params = self.namespace_model.options["package_configuration"] or {}
        for template_name in package_files:
            file = template_name.replace(".jinja2", "")
            output_name = root_of_sdk / file
            if not self.read_file(output_name) or file in _REGENERATE_FILES:
                self.write_file(
                    output_name,
                    serializer.serialize_package_file(template_name, **params),
                )

    def _keep_patch_file(self, path_file: Path, env: Environment):
        if self.read_file(path_file):
            self.write_file(path_file, self.read_file(path_file))
        else:
            self.write_file(
                path_file,
                PatchSerializer(
                    env=env, namespace_model=self.namespace_model
                ).serialize(),
            )

    def _serialize_and_write_models_folder(
        self, env: Environment, namespace_path: Path
    ) -> None:
        # Write the models folder
        models_path = namespace_path / Path("models")
        serializer = (
            DpgModelSerializer
            if self.namespace_model.options["models_mode"] == "dpg"
            else MsrestModelSerializer
        )
        if self.namespace_model.model_types:
            self.write_file(
                models_path / Path(f"{self.namespace_model.models_filename}.py"),
                serializer(namespace_model=self.namespace_model, env=env).serialize(),
            )
        if self.namespace_model.enums:
            self.write_file(
                models_path / Path(f"{self.namespace_model.enums_filename}.py"),
                EnumSerializer(
                    namespace_model=self.namespace_model, env=env
                ).serialize(),
            )
        self.write_file(
            models_path / Path("__init__.py"),
            ModelInitSerializer(
                namespace_model=self.namespace_model, env=env
            ).serialize(),
        )

    def _serialize_and_write_rest_layer(
        self, env: Environment, namespace_path: Path
    ) -> None:
        rest_path = namespace_path / Path(self.namespace_model.rest_layer_name)
        group_names = {
            rb.group_name
            for c in self.namespace_model.clients
            for rb in c.request_builders
        }

        for group_name in group_names:
            request_builders = [
                r
                for c in self.namespace_model.clients
                for r in c.request_builders
                if r.group_name == group_name
            ]
            self._serialize_and_write_single_rest_layer(
                env, rest_path, request_builders
            )
        if not "" in group_names:
            self.write_file(
                rest_path / Path("__init__.py"),
                self.namespace_model.options["license_header"],
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
        self.write_file(
            output_path / Path("_request_builders.py"),
            RequestBuildersSerializer(
                namespace_model=self.namespace_model,
                env=env,
                request_builders=request_builders,
            ).serialize_request_builders(),
        )

        # write rest init file
        self.write_file(
            output_path / Path("__init__.py"),
            RequestBuildersSerializer(
                namespace_model=self.namespace_model,
                env=env,
                request_builders=request_builders,
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
            namespace_model=self.namespace_model,
            env=env,
            async_mode=False,
            operation_group=operation_group,
        )
        self.write_file(
            namespace_path
            / Path(self.namespace_model.operations_folder_name)
            / Path(f"{filename}.py"),
            operation_group_serializer.serialize(),
        )

        if self.has_aio_folder:
            # write async operation group and operation files
            operation_group_async_serializer = OperationGroupsSerializer(
                namespace_model=self.namespace_model,
                env=env,
                async_mode=True,
                operation_group=operation_group,
            )
            self.write_file(
                (
                    namespace_path
                    / Path("aio")
                    / Path(self.namespace_model.operations_folder_name)
                    / Path(f"{filename}.py")
                ),
                operation_group_async_serializer.serialize(),
            )

    def _serialize_and_write_operations_folder(
        self, env: Environment, namespace_path: Path
    ) -> None:
        # write sync operations init file
        operations_init_serializer = OperationsInitSerializer(
            namespace_model=self.namespace_model, env=env, async_mode=False
        )
        self.write_file(
            namespace_path
            / Path(self.namespace_model.operations_folder_name)
            / Path("__init__.py"),
            operations_init_serializer.serialize(),
        )

        # write async operations init file
        if self.has_aio_folder:
            operations_async_init_serializer = OperationsInitSerializer(
                namespace_model=self.namespace_model, env=env, async_mode=True
            )
            self.write_file(
                namespace_path
                / Path("aio")
                / Path(self.namespace_model.operations_folder_name)
                / Path("__init__.py"),
                operations_async_init_serializer.serialize(),
            )

        if self.namespace_model.options["combine_operation_files"]:
            self._serialize_and_write_operations_file(
                env=env,
                namespace_path=namespace_path,
            )
        else:
            for operation_group in self.namespace_model.operation_groups:
                self._serialize_and_write_operations_file(
                    env=env,
                    namespace_path=namespace_path,
                    operation_group=operation_group,
                )

    def _serialize_and_write_version_file(
        self,
        namespace_path: Path,
        general_namespace_serializer: GeneralNamespaceSerializer,
    ):
        def _read_version_file(original_version_file_name: str) -> str:
            return self.read_file(namespace_path / original_version_file_name)

        def _write_version_file(original_version_file_name: str) -> None:
            self.write_file(
                namespace_path / Path("_version.py"),
                _read_version_file(original_version_file_name),
            )

        keep_version_file = self.namespace_model.options["keep_version_file"]
        if keep_version_file and _read_version_file("_version.py"):
            _write_version_file(original_version_file_name="_version.py")
        elif keep_version_file and _read_version_file("version.py"):
            _write_version_file(original_version_file_name="version.py")
        elif self.namespace_model.options["package_version"]:
            self.write_file(
                namespace_path / Path("_version.py"),
                general_namespace_serializer.serialize_version_file(),
            )

    def _serialize_and_write_top_level_folder(
        self, env: Environment, namespace_path: Path
    ) -> None:
        general_namespace_serializer = GeneralNamespaceSerializer(
            namespace_model=self.namespace_model, env=env, async_mode=False
        )
        general_serializer = GeneralSerializer(
            code_model=self.code_model,
            env=env,
        )

        self.write_file(
            namespace_path / Path("__init__.py"),
            general_namespace_serializer.serialize_init_file(),
        )
        p = namespace_path.parent
        while p != Path("."):
            # write pkgutil init file
            self.write_file(
                p / Path("__init__.py"),
                general_namespace_serializer.serialize_pkgutil_init_file(),
            )
            p = p.parent

        # Write the service client
        if self.namespace_model.operation_groups:
            self.write_file(
                namespace_path / Path(f"{self.namespace_model.client_filename}.py"),
                general_namespace_serializer.serialize_service_client_file(),
            )

        if self.namespace_model.need_vendored_code(async_mode=False):
            self.write_file(
                namespace_path / Path("_vendor.py"),
                general_namespace_serializer.serialize_vendor_file(),
            )

        self._serialize_and_write_version_file(
            namespace_path, general_namespace_serializer
        )

        # write the empty py.typed file
        self.write_file(namespace_path / Path("py.typed"), "# Marker file for PEP 561.")

        if (
            not self.namespace_model.options["client_side_validation"]
            and not self.namespace_model.options["multiapi"]
        ):
            self.write_file(
                namespace_path / Path("_serialization.py"),
                general_namespace_serializer.serialize_serialization_file(),
            )
        if self.namespace_model.options["models_mode"] == "dpg":
            self.write_file(
                namespace_path / Path("_model_base.py"),
                general_namespace_serializer.serialize_model_base_file(),
            )

        if any(
            og for og in self.namespace_model.operation_groups if og.need_validation
        ):
            self.write_file(
                namespace_path / Path("_validation.py"),
                general_namespace_serializer.serialize_validation_file(),
            )

        # Write the config file
        if self.namespace_model.request_builders:
            self.write_file(
                namespace_path / Path("_configuration.py"),
                general_namespace_serializer.serialize_config_file(),
            )

        # Write the setup file
        if self.namespace_model.options["basic_setup_py"]:
            self.write_file(Path("setup.py"), general_serializer.serialize_setup_file())

    def _serialize_and_write_aio_top_level_folder(
        self, env: Environment, namespace_path: Path
    ) -> None:
        aio_general_namespace_serializer = GeneralNamespaceSerializer(
            namespace_model=self.namespace_model, env=env, async_mode=True
        )

        aio_path = namespace_path / Path("aio")

        # Write the __init__ file
        self.write_file(
            aio_path / Path("__init__.py"),
            aio_general_namespace_serializer.serialize_init_file(),
        )

        # Write the service client
        if self.namespace_model.request_builders:
            self.write_file(
                aio_path / Path(f"{self.namespace_model.client_filename}.py"),
                aio_general_namespace_serializer.serialize_service_client_file(),
            )

        # Write the config file
        self.write_file(
            aio_path / Path("_configuration.py"),
            aio_general_namespace_serializer.serialize_config_file(),
        )
        if self.namespace_model.need_vendored_code(async_mode=True):
            self.write_file(
                aio_path / Path("_vendor.py"),
                aio_general_namespace_serializer.serialize_vendor_file(),
            )

    def _serialize_and_write_metadata(
        self, env: Environment, namespace_path: Path
    ) -> None:
        metadata_serializer = MetadataSerializer(self.namespace_model, env)
        self.write_file(
            namespace_path / Path("_metadata.json"), metadata_serializer.serialize()
        )


class JinjaSerializerAutorest(JinjaSerializer, ReaderAndWriterAutorest):
    def __init__(
        self,
        autorestapi: AutorestAPI,
        code_model: CodeModel,
        namespace_model: NamespaceModel,
        *,
        output_folder: Union[str, Path],
        **kwargs: Any,
    ) -> None:
        super().__init__(
            autorestapi=autorestapi,
            code_model=code_model,
            namespace_model=namespace_model,
            output_folder=output_folder,
            **kwargs,
        )
