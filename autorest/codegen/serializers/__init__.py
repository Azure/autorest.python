# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from pathlib import Path

from jinja2 import PackageLoader, Environment

from ...jsonrpc import AutorestAPI
from ..models import CodeModel

from .enum_serializer import EnumSerializer
from .general_serializer import GeneralSerializer
from .model_generic_serializer import ModelGenericSerializer
from .model_init_serializer import ModelInitSerializer
from .model_python3_serializer import ModelPython3Serializer
from .operations_init_serializer import OperationsInitSerializer
from .operation_group_serializer import OperationGroupSerializer
from .metadata_serializer import MetadataSerializer

__all__ = [
    "JinjaSerializer",
]


class JinjaSerializer:
    def __init__(self, autorestapi: AutorestAPI):
        self._autorestapi = autorestapi

    def serialize(self, code_model: CodeModel) -> None:
        env = Environment(
            loader=PackageLoader("autorest.codegen", "templates"),
            keep_trailing_newline=True,
            line_statement_prefix="##",
            line_comment_prefix="###",
            trim_blocks=True,
            lstrip_blocks=True,
        )

        namespace_path = (
            Path(".") if code_model.options["no_namespace_folders"] else Path(*(code_model.namespace.split(".")))
        )

        if code_model.schemas:
            self._serialize_and_write_models_folder(code_model=code_model, env=env, namespace_path=namespace_path)

        self._serialize_and_write_operations_folder(code_model=code_model, env=env, namespace_path=namespace_path)

        self._serialize_and_write_top_level_folder(code_model=code_model, env=env, namespace_path=namespace_path)

        if not code_model.options["no_async"]:
            self._serialize_and_write_aio_folder(
                code_model=code_model, env=env, namespace_path=namespace_path,
            )

        if code_model.options["multiapi"]:
            self._serialize_and_write_metadata(
                code_model, env=env, namespace_path=namespace_path
            )

    def _serialize_and_write_models_folder(self, code_model: CodeModel, env: Environment, namespace_path: Path) -> None:
        # Write the models folder
        models_path = namespace_path / Path("models")
        self._autorestapi.write_file(
            models_path / Path("_models.py"), ModelGenericSerializer(code_model=code_model, env=env).serialize()
        )
        self._autorestapi.write_file(
            models_path / Path("_models_py3.py"), ModelPython3Serializer(code_model=code_model, env=env).serialize()
        )
        if code_model.enums:
            self._autorestapi.write_file(
                models_path / Path(f"_{code_model.module_name}_enums.py"),
                EnumSerializer(code_model=code_model, env=env).serialize(),
            )
        self._autorestapi.write_file(
            models_path / Path("__init__.py"), ModelInitSerializer(code_model=code_model, env=env).serialize()
        )

    def _serialize_and_write_operations_folder(
        self, code_model: CodeModel, env: Environment, namespace_path: Path
    ) -> None:
        # write sync operations init file
        operations_init_serializer = OperationsInitSerializer(code_model=code_model, env=env, async_mode=False)
        self._autorestapi.write_file(
            namespace_path / Path(f"operations") / Path("__init__.py"), operations_init_serializer.serialize()
        )

        # write async operations init file
        if not code_model.options["no_async"]:
            operations_async_init_serializer = OperationsInitSerializer(code_model=code_model, env=env, async_mode=True)
            self._autorestapi.write_file(
                namespace_path / Path("aio") / Path(f"operations_async") / Path("__init__.py"),
                operations_async_init_serializer.serialize(),
            )

        for operation_group in code_model.operation_groups:
            # write sync operation group and operation files
            operation_group_serializer = OperationGroupSerializer(
                code_model=code_model, env=env, operation_group=operation_group, async_mode=False
            )
            self._autorestapi.write_file(
                namespace_path / Path(f"operations") / Path(f"{operation_group.get_filename(async_mode=False)}.py"),
                operation_group_serializer.serialize(),
            )

            if not code_model.options["no_async"]:
                # write async operation group and operation files
                operation_group_async_serializer = OperationGroupSerializer(
                    code_model=code_model, env=env, operation_group=operation_group, async_mode=True
                )
                self._autorestapi.write_file(
                    (
                        namespace_path
                        / Path("aio")
                        / Path(f"operations_async")
                        / Path(f"{operation_group.get_filename(async_mode=True)}.py")
                    ),
                    operation_group_async_serializer.serialize(),
                )

    def _serialize_and_write_top_level_folder(
        self, code_model: CodeModel, env: Environment, namespace_path: Path
    ) -> None:
        general_serializer = GeneralSerializer(code_model=code_model, env=env, async_mode=False)

        self._autorestapi.write_file(namespace_path / Path("__init__.py"), general_serializer.serialize_init_file())
        p = namespace_path.parent
        while p.parent != Path("."):
            # write pkgutil init file
            self._autorestapi.write_file(
                namespace_path / Path("__init__.py"), general_serializer.serialize_pkgutil_init_file()
            )
            p = p.parent

        # Write the service client
        self._autorestapi.write_file(
            namespace_path / Path(f"_{code_model.module_name}.py"), general_serializer.serialize_service_client_file()
        )

        # Write the version if necessary
        if (
            code_model.options['keep_version_file'] and
            self._autorestapi.read_file(namespace_path / Path("_version.py"))
        ):
            self._autorestapi.write_file(
                namespace_path / Path("_version.py"),
                self._autorestapi.read_file(namespace_path / Path("_version.py"))
            )
        elif code_model.options['package_version']:
            self._autorestapi.write_file(
                namespace_path / Path("_version.py"),
                general_serializer.serialize_version_file()
            )

        # write the empty py.typed file
        self._autorestapi.write_file(namespace_path / Path("py.typed"), code_model.options['license_header'] + "\n")

        # Write the config file
        self._autorestapi.write_file(
            namespace_path / Path("_configuration.py"), general_serializer.serialize_config_file()
        )

        # Write the setup file
        if code_model.options["basic_setup_py"]:
            self._autorestapi.write_file(Path("setup.py"), general_serializer.serialize_setup_file())

    def _serialize_and_write_aio_folder(self, code_model: CodeModel, env: Environment, namespace_path: Path) -> None:
        aio_general_serializer = GeneralSerializer(code_model=code_model, env=env, async_mode=True)

        aio_path = namespace_path / Path("aio")

        # Write the __init__ file
        self._autorestapi.write_file(aio_path / Path("__init__.py"), aio_general_serializer.serialize_init_file())

        # Write the service client
        self._autorestapi.write_file(
            aio_path / Path(f"_{code_model.module_name}_async.py"),
            aio_general_serializer.serialize_service_client_file(),
        )

        # Write the config file
        self._autorestapi.write_file(
            aio_path / Path("_configuration_async.py"), aio_general_serializer.serialize_config_file()
        )

    def _serialize_and_write_metadata(self, code_model: CodeModel, env: Environment, namespace_path: Path) -> None:
        metadata_serializer = MetadataSerializer(code_model, env)
        self._autorestapi.write_file(namespace_path / Path("_metadata.json"), metadata_serializer.serialize())
