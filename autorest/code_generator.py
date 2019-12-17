# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import logging
from pathlib import Path
import sys

import yaml

from jinja2 import Template, PackageLoader, Environment

from .jsonrpc import AutorestAPI

from .plugins import NameConverter, CloudErrorPlugin
from .models.code_model import CodeModel
from .models import build_schema, EnumSchema, ConstantSchema
from .models.operation_group import OperationGroup
from .models.parameter import Parameter
from .serializers import (
    EnumSerializer,
    FileImportSerializer,
    GeneralSerializer,
    ModelGenericSerializer,
    ModelInitSerializer,
    ModelPython3Serializer,
    OperationsInitSerializer,
    OperationGroupSerializer
)


_LOGGER = logging.getLogger(__name__)


class CodeGenerator:
    def __init__(self, autorestapi: AutorestAPI):
        self._autorestapi = autorestapi

    def _build_exceptions_set(self, yaml_data):
        exceptions_set = set()
        for group in yaml_data:
            for operation in group['operations']:
                if not operation.get('exceptions'):
                    continue
                for exception in operation['exceptions']:
                    if not exception.get('schema'):
                        continue
                    exceptions_set.add(exception['schema']['language']['python']['name'])
        return exceptions_set

    def _create_code_model(self, yaml_code_model, options):
        # Create a code model
        code_model = CodeModel(options)
        code_model.module_name = yaml_code_model['info']['python_title']
        code_model.class_name = yaml_code_model['info']['pascal_case_title']
        code_model.description = yaml_code_model['info']['description'] if yaml_code_model['info'].get('description') else ""
        code_model.package_version = self._autorestapi.get_value("package-version")
        code_model.options["payload-flattening-threshold"] = self._autorestapi.get_value("payload-flattening-threshold") or 0
        code_model.options["basic-setup-py"] = self._autorestapi.get_boolean_value("basic-setup-py")

        # Check consistency of parameters
        if code_model.options["basic-setup-py"] and not code_model.package_version:
            raise ValueError("--basic-setup-py must be used with --package-version")

        # Global parameters
        code_model.global_parameters = [Parameter.from_yaml(param) for param in yaml_code_model.get('globalParameters', [])]

        # Custom URL
        dollar_host = [parameter for parameter in code_model.global_parameters if parameter.rest_api_name == "$host"]
        if not dollar_host:
            # We don't want to support multi-api customurl YET (will see if that goes well....)
            # So far now, let's get the first one in the first operation
            # UGLY as hell.....
            code_model.custom_base_url = yaml_code_model['operationGroups'][0]['operations'][0]['request']['protocol']['http']['uri']
        else:
            dollar_host_parameter = dollar_host[0]
            code_model.global_parameters.remove(dollar_host_parameter)
            code_model.base_url = dollar_host_parameter.yaml_data['clientDefaultValue']

        # Get whether we are tracing
        code_model.tracing = self._autorestapi.get_boolean_value("trace")

        # Create operations
        code_model.operation_groups = [OperationGroup.from_yaml(code_model, op_group) for op_group in yaml_code_model['operationGroups']]

        # Get my namespace
        namespace = self._autorestapi.get_value("namespace")
        _LOGGER.debug("Namespace parameter was %s", namespace)
        if not namespace:
            namespace = yaml_code_model["info"]["python_title"]
        code_model.namespace = namespace

        if yaml_code_model.get('schemas'):
            exceptions_set = self._build_exceptions_set(yaml_data=yaml_code_model['operationGroups'])

            for type_list in yaml_code_model['schemas'].values():
                for schema in type_list:
                    build_schema(
                        yaml_data=schema,
                        exceptions_set=exceptions_set,
                        code_model=code_model
                    )
            # sets the enums property in our code_model variable, which will later be passed to EnumSerializer

            code_model.add_inheritance_to_models()
            code_model.sort_schemas()
            code_model.add_schema_link_to_operation()
            code_model.add_schema_link_to_global_parameters()

        # Parameter flattening
        code_model.enable_parameter_flattening()

        # LRO operation
        code_model.format_lro_operations()
        code_model.remove_next_operation()

        if code_model.options['credential']:
            code_model.add_credential_global_parameter()

        return code_model

    def _serialize_and_write_models_folder(self, code_model, env):
        namespace_path = Path(*[ns_part for ns_part in code_model.namespace.split(".")])
        # Serialize the models folder

        model_generic_serializer = ModelGenericSerializer(code_model=code_model, env=env)
        model_generic_serializer.serialize()

        model_python3_serializer = ModelPython3Serializer(code_model=code_model, env=env)
        model_python3_serializer.serialize()

        if code_model.enums:
            enum_serializer = EnumSerializer(enums=code_model.enums, env=env)
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
        namespace_path = Path(*[ns_part for ns_part in code_model.namespace.split(".")])
        general_serializer = GeneralSerializer(code_model=code_model, env=env, async_mode=False)
        general_serializer.serialize()

        # Write the __init__ file
        self._autorestapi.write_file(namespace_path / Path("__init__.py"), general_serializer.init_file)

        # Write the service client
        self._autorestapi.write_file(
            namespace_path / Path("_{}.py".format(code_model.module_name)),
            general_serializer.service_client_file
        )

        # Write the version if necessary
        if code_model.package_version:
            self._autorestapi.write_file(namespace_path / Path("_version.py"), general_serializer.version_file)

        # Write the config file
        self._autorestapi.write_file(namespace_path / Path("_configuration.py"), general_serializer.config_file)

        # Write the setup file
        if code_model.options["basic-setup-py"]:
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


    def process(self) -> bool:
        # List the input file, should be only one
        inputs = self._autorestapi.list_inputs()
        _LOGGER.debug("Possible Inputs: %s", inputs)
        if "code-model-v4-no-tags.yaml" not in inputs:
            raise ValueError("code-model-v4-no-tags.yaml must be a possible input")

        file_content = self._autorestapi.read_file("code-model-v4-no-tags.yaml")
        self._autorestapi.write_file("code-model-v4-no-tags.yaml", file_content)

        env = Environment(
            loader=PackageLoader('autorest', 'templates'),
            keep_trailing_newline=True,
            line_statement_prefix="##",
            line_comment_prefix="###",
            trim_blocks=True,
            lstrip_blocks=True,
        )

        # Parse the received YAML
        yaml_code_model = yaml.safe_load(file_content)

        azure_arm = self._autorestapi.get_boolean_value("azure-arm")
        if azure_arm:
            CloudErrorPlugin.remove_cloud_errors(yaml_code_model)
        # convert the names to python names
        NameConverter.convert_yaml_names(yaml_code_model)

        credential_scopes = self._autorestapi.get_value('credential-scopes')
        if not credential_scopes and azure_arm:
            credential_scopes = "https://management.azure.com/.default"

        options = {
            'azure_arm': azure_arm,
            'credential': self._autorestapi.get_boolean_value("add-credentials") or self._autorestapi.get_boolean_value('add-credential'),
            "credential_scopes": credential_scopes.split(",") if credential_scopes else None,
            'head_as_boolean': self._autorestapi.get_boolean_value('head-as-boolean')
        }

        # Force some options in ARM MODE:
        if azure_arm:
            options['credential'] = True
            options['head_as_boolean'] = True

        # save a new copy for debug
        #self._autorestapi.write_file("code-model-v4-no-tags-python.yaml", yaml.safe_dump(yaml_code_model))

        code_model = self._create_code_model(yaml_code_model=yaml_code_model, options=options)

        if code_model.schemas:
            self._serialize_and_write_models_folder(code_model=code_model, env=env)

        self._serialize_and_write_operations_folder(code_model=code_model, env=env)

        self._serialize_and_write_top_level_folder(
            code_model=code_model,
            env=env
        )

        self._serialize_and_write_aio_folder(
            code_model=code_model,
            env=env
        )

        return True

def main(yaml_model_file):
    from .jsonrpc.localapi import LocalAutorestAPI

    code_generator = CodeGenerator(
        autorestapi=LocalAutorestAPI(
            reachable_files=[yaml_model_file])
    )
    if not code_generator.process():
        raise SystemExit("Process didn't finish gracefully")

if __name__ == "__main__":
    main(sys.argv[1])
