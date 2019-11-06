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

from .common.utils import get_namespace_name, get_method_name
from .models.code_model import CodeModel
from .models import build_schema, EnumSchema
from .models.operation_group import OperationGroup
from .serializers import (
    AioGeneralSerializer,
    EnumSerializer,
    FileImportSerializer,
    GeneralSerializer,
    ModelGenericSerializer,
    ModelInitSerializer,
    ModelPython3Serializer
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
                    exceptions_set.add(exception['schema']['$key'])
        return exceptions_set

    def _create_code_model(self, yaml_code_model):
        # Create a code model
        code_model = CodeModel()
        code_model.client_name = yaml_code_model['info']['title']
        code_model.description = yaml_code_model['info']['description'] if yaml_code_model['info'].get('description') else ""
        code_model.api_version = self._autorestapi.get_value("package-version")
        if not code_model.api_version:
            code_model.api_version = "1.0.0"

        # Get my namespace
        namespace = self._autorestapi.get_value("namespace")
        _LOGGER.debug("Namespace parameter was %s", namespace)
        if not namespace:
            namespace = get_namespace_name(yaml_code_model["info"]["title"])
        code_model.namespace = Path(*[ns_part for ns_part in namespace.split(".")])

        if not yaml_code_model['schemas']:
            return code_model

        exceptions_set = self._build_exceptions_set(yaml_data=yaml_code_model['operationGroups'])

        classes = [a for a in yaml_code_model['schemas']['objects']]
        code_model.schemas = [build_schema(name=s['language']['default']['name'], yaml_data=s, exceptions_set=exceptions_set) for s in classes]
        # sets the enums property in our code_model variable, which will later be passed to EnumSerializer
        code_model.build_enums()
        code_model.add_inheritance_to_models()
        code_model.sort_schemas()


        return code_model

    def _serialize_and_write_models_folder(self, namespace, code_model):
        # Serialize the models folder

        model_generic_serializer = ModelGenericSerializer(code_model=code_model)
        model_generic_serializer.serialize()

        model_python3_serializer = ModelPython3Serializer(code_model=code_model)
        model_python3_serializer.serialize()

        if code_model.enums:
            enum_serializer = EnumSerializer(enums=code_model.enums)
            enum_serializer.serialize()

        model_init_serializer = ModelInitSerializer(code_model=code_model)
        model_init_serializer.serialize()

        # Write the models folder
        models_path = namespace / Path("models")
        self._autorestapi.write_file(models_path / Path("_models.py"), model_generic_serializer.model_file)
        self._autorestapi.write_file(models_path / Path("_models_py3.py"), model_python3_serializer.model_file)
        if code_model.enums:
            self._autorestapi.write_file(models_path / Path("_{}_enums.py".format(get_namespace_name(code_model.client_name))), enum_serializer.enum_file)
        self._autorestapi.write_file(models_path / Path("__init__.py"), model_init_serializer.model_init_file)

    def _serialize_and_write_operations_folder(self, namespace, operation_groups, env):
        template = env.get_template("operations_container.py.jinja2")
        for operation_group in operation_groups:
            operation_group_content = template.render(
                operation_group=operation_group,
                imports=FileImportSerializer(operation_group.imports())
            )
            self._autorestapi.write_file(
                namespace / Path("operations") / Path(f"_{get_method_name(operation_group.name)}_operations.py"),
                operation_group_content
            )

    def _serialize_and_write_top_level_folder(self, namespace, operation_group_names, code_model):
        general_serializer = GeneralSerializer(
            code_model=code_model, operation_group_names=operation_group_names
        )
        general_serializer.serialize()

        # Write the __init__ file
        self._autorestapi.write_file(namespace / Path("__init__.py"), general_serializer.init_file)

        # Write the service client
        self._autorestapi.write_file(
            namespace / Path("_{}.py".format(get_namespace_name(code_model.client_name))),
            general_serializer.service_client_file
        )

        # Write the version
        self._autorestapi.write_file(namespace / Path("version.py"), general_serializer.version_file)

        # Write the config file
        self._autorestapi.write_file(namespace / Path("_configuration.py"), general_serializer.config_file)

        # Write the setup file
        self._autorestapi.write_file(Path("setup.py"), general_serializer.setup_file)

    def _serialize_and_write_aio_folder(self, namespace, operation_group_names, code_model):
        aio_general_serializer = AioGeneralSerializer(
            code_model=code_model,
            operation_group_names=operation_group_names
        )
        aio_general_serializer.serialize()

        aio_path = namespace / Path("aio")

        # Write the __init__ file
        self._autorestapi.write_file(aio_path / Path("__init__.py"), aio_general_serializer.init_file)

        # Write the service client
        self._autorestapi.write_file(
            aio_path / Path("_{}_async.py".format(get_namespace_name(code_model.client_name))),
            aio_general_serializer.service_client_file
        )

        # Write the config file
        self._autorestapi.write_file(aio_path / Path("_configuration_async.py"), aio_general_serializer.config_file)


    def process(self) -> bool:
        # List the input file, should be only one
        inputs = self._autorestapi.list_inputs()
        _LOGGER.info("Possible Inputs: %s", inputs)
        if "code-model-v4-no-tags.yaml" not in inputs:
            raise ValueError("code-model-v4-no-tags.yaml must be a possible input")

        file_content = self._autorestapi.read_file("code-model-v4-no-tags.yaml")

        env = Environment(
            loader=PackageLoader('autorest', 'templates'),
            keep_trailing_newline=True
        )

        # Parse the received YAML
        yaml_code_model = yaml.safe_load(file_content)

        code_model = self._create_code_model(yaml_code_model=yaml_code_model)

        if code_model.schemas:
            self._serialize_and_write_models_folder(namespace=code_model.namespace, code_model=code_model)

        operation_groups = [OperationGroup.from_yaml(op_group) for op_group in yaml_code_model['operationGroups']]
        self._serialize_and_write_operations_folder(namespace=code_model.namespace, operation_groups=operation_groups, env=env)

        operation_group_names = [o.name for o in operation_groups]
        self._serialize_and_write_top_level_folder(
            namespace=code_model.namespace,
            operation_group_names=operation_group_names,
            code_model=code_model
        )

        self._serialize_and_write_aio_folder(
            namespace=code_model.namespace,
            code_model=code_model,
            operation_group_names=operation_group_names
        )

        return True

def main(yaml_model_file):
    from .jsonrpc.localapi import LocalAutorestAPI

    logging.basicConfig(
        level=logging.DEBUG,
    )

    code_generator = CodeGenerator(
        autorestapi=LocalAutorestAPI(
            reachable_files=[yaml_model_file])
    )
    if not code_generator.process():
        raise SystemExit("Process didn't finish gracefully")

if __name__ == "__main__":
    main(sys.argv[1])