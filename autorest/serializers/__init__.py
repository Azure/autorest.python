# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from pathlib import Path

from jinja2 import PackageLoader, Environment

from ..jsonrpc import AutorestAPI
from ..models import CodeModel

from .enum_serializer import EnumSerializer
from .general_serializer import GeneralSerializer
from .model_generic_serializer import ModelGenericSerializer
from .model_init_serializer import ModelInitSerializer
from .model_python3_serializer import ModelPython3Serializer
from .operations_init_serializer import OperationsInitSerializer
from .operation_group_serializer import OperationGroupSerializer

__all__ = [
    "JinjaSerializer",
]


class JinjaSerializer:

    def __init__(self, autorestapi: AutorestAPI):
        self._autorestapi = autorestapi

    def serialize(self, code_model: CodeModel) -> None:
        env = Environment(
            loader=PackageLoader('autorest', 'templates'),
            keep_trailing_newline=True,
            line_statement_prefix="##",
            line_comment_prefix="###",
            trim_blocks=True,
            lstrip_blocks=True,
        )

        if code_model.schemas:
            self._serialize_and_write_models_folder(code_model=code_model, env=env)

        self._serialize_and_write_operations_folder(code_model=code_model, env=env)

        self._serialize_and_write_top_level_folder(
            code_model=code_model,
            env=env
        )

        if not code_model.options['no_async']:
            self._serialize_and_write_aio_folder(
                code_model=code_model,
                env=env
            )

    def _serialize_and_write_models_folder(self, code_model, env):
        namespace_path = Path(*[ns_part for ns_part in code_model.namespace.split(".")])
        # Serialize the models folder

        model_generic_serializer = ModelGenericSerializer(code_model=code_model, env=env)
        model_generic_serializer.serialize()

        model_python3_serializer = ModelPython3Serializer(code_model=code_model, env=env)
        model_python3_serializer.serialize()

        if code_model.enums:
            enum_serializer = EnumSerializer(code_model=code_model, env=env)
            enum_serializer.serialize()

        model_init_serializer = ModelInitSerializer(code_model=code_model, env=env)
        model_init_serializer.serialize()

        # Write the models folder
        models_path = namespace_path / Path("models")
        self._autorestapi.write_file(models_path / Path("_models.py"), model_generic_serializer.model_file)
        self._autorestapi.write_file(models_path / Path("_models_py3.py"), model_python3_serializer.model_file)
        if code_model.enums:
            self._autorestapi.write_file(models_path / Path("_{}_enums.py".format(code_model.module_name)), enum_serializer.enum_file)
        self._autorestapi.write_file(models_path / Path("__init__.py"), model_init_serializer.model_init_file)

    def _serialize_and_write_operations_folder(self, code_model, env):
        namespace_path = Path(*[ns_part for ns_part in code_model.namespace.split(".")])
        # write sync operations init file
        operations_init_serializer = OperationsInitSerializer(code_model=code_model, env=env, async_mode=False)
        operations_init_serializer.serialize()
        self._autorestapi.write_file(
            namespace_path / Path(f"operations") / Path("__init__.py"),
            operations_init_serializer.operations_init_file
        )

        # write async operations init file
        if not code_model.options['no_async']:
            operations_async_init_serializer = OperationsInitSerializer(code_model=code_model, env=env, async_mode=True)
            operations_async_init_serializer.serialize()
            self._autorestapi.write_file(
                namespace_path / Path("aio") / Path(f"operations_async") / Path("__init__.py"),
                operations_async_init_serializer.operations_init_file
            )

        for operation_group in code_model.operation_groups:
            # write sync operation group and operation files
            operation_group_serializer = OperationGroupSerializer(
                code_model=code_model, env=env, operation_group=operation_group, async_mode=False
            )
            operation_group_serializer.serialize()
            self._autorestapi.write_file(
                namespace_path / Path(f"operations") / Path(operation_group_serializer.filename()),
                operation_group_serializer.operation_group_file
            )

            if not code_model.options['no_async']:
                # write async operation group and operation files
                operation_group_async_serializer = OperationGroupSerializer(
                    code_model=code_model, env=env, operation_group=operation_group, async_mode=True
                )
                operation_group_async_serializer.serialize()
                self._autorestapi.write_file(
                    namespace_path / Path("aio") / Path(f"operations_async") / Path(operation_group_async_serializer.filename()),
                    operation_group_async_serializer.operation_group_file
                )

    def _serialize_and_write_top_level_folder(self, code_model, env):
        # namespace_path = Path(*[ns_part for ns_part in code_model.namespace.split(".")])
        general_serializer = GeneralSerializer(code_model=code_model, env=env, async_mode=False)
        general_serializer.serialize()

        namespace_parts = [ns_part for ns_part in code_model.namespace.split(".")]
        namespace_path = None
        for i in range(len(namespace_parts)):
            namespace_path = Path(namespace_parts[i]) if not namespace_path else namespace_path / Path(namespace_parts[i])
            if i == len(namespace_parts) - 1:
                # Write the main __init__ file
                self._autorestapi.write_file(namespace_path / Path("__init__.py"), general_serializer.init_file)
            else:
                # write pkgutil init file
                self._autorestapi.write_file(namespace_path / Path("__init__.py"), general_serializer.pkgutil_init_file)


        # Write the service client
        self._autorestapi.write_file(
            namespace_path / Path("_{}.py".format(code_model.module_name)),
            general_serializer.service_client_file
        )

        # Write the version if necessary
        if code_model.options['package_version'] or not code_model.options['keep_version_file'] or not self._autorestapi.read_file(namespace_path / Path("_version.py")):
            self._autorestapi.write_file(namespace_path / Path("_version.py"), general_serializer.version_file)

        # Write the config file
        self._autorestapi.write_file(namespace_path / Path("_configuration.py"), general_serializer.config_file)

        # Write the setup file
        if code_model.options["basic_setup_py"]:
            self._autorestapi.write_file(Path("setup.py"), general_serializer.setup_file)

    def _serialize_and_write_aio_folder(self, code_model, env):
        namespace_path = Path(*[ns_part for ns_part in code_model.namespace.split(".")])
        aio_general_serializer = GeneralSerializer(code_model=code_model, env=env, async_mode=True)
        aio_general_serializer.serialize()

        aio_path = namespace_path / Path("aio")

        # Write the __init__ file
        self._autorestapi.write_file(aio_path / Path("__init__.py"), aio_general_serializer.init_file)

        # Write the service client
        self._autorestapi.write_file(
            aio_path / Path("_{}_async.py".format(code_model.module_name)),
            aio_general_serializer.service_client_file
        )

        # Write the config file
        self._autorestapi.write_file(aio_path / Path("_configuration_async.py"), aio_general_serializer.config_file)
