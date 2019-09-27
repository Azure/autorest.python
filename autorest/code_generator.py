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

from .common.code_namer import CodeNamer
from .models.codemodel import CodeModel
from .models.compositetype import CompositeType
from .models.operation_group import OperationGroup
from .serializers.genericserializer import GenericSerializer
from .serializers.python3serializer import Python3Serializer
from .serializers.import_serializer import FileImportSerializer


_LOGGER = logging.getLogger(__name__)


class CodeGenerator:
    def __init__(self, autorestapi: AutorestAPI):
        self._autorestapi = autorestapi

    def process(self) -> bool:
        # List the input file, should be only one
        inputs = self._autorestapi.list_inputs()
        _LOGGER.info("Possible Inputs: %s", inputs)
        if "code-model-v4-no-tags.yaml" not in inputs:
            raise ValueError("code-model-v4-no-tags.yaml must be a possible input")

        file_content = self._autorestapi.read_file("code-model-v4-no-tags.yaml")
        self._autorestapi.write_file("code-model-v4-no-tags.yaml", file_content)

        env = Environment(
            loader=PackageLoader('autorest', 'templates'),
            keep_trailing_newline=True
        )

        # Parse the received YAML
        yaml_code_model = yaml.safe_load(file_content)

        # Create a code model
        code_model = CodeModel()
        code_model.client_name = yaml_code_model["info"]["title"]
        # code_model.api_version = yaml_code_model["info"]["version"]

        composite_types = [d for d in yaml_code_model['schemas']['objects']]
        child_composite_types = [c for c in yaml_code_model['schemas']['ands']]
        code_model.schemas = []
        seen_names = set()
        # only adds a CompositeType to the list of schemas if we have not seen the name of the CompositeType yet
        code_model.schemas = [CompositeType.from_yaml(s, child_composite_types=child_composite_types)
                            for s in composite_types if s['language']['default']['name'] not in seen_names and
                            not seen_names.add(s['language']['default']['name'])]
        code_model.sort_schemas()

        generic_serializer = GenericSerializer(code_model=code_model)
        generic_serializer.serialize()

        python3_serializer = Python3Serializer(code_model=code_model)
        python3_serializer.serialize()

        operation_groups = [OperationGroup.from_yaml(op_group) for op_group in yaml_code_model['operationGroups']]

        # Get my namespace
        namespace = self._autorestapi.get_value("namespace")
        _LOGGER.debug("Namespace parameter was %s", namespace)
        if not namespace:
            namespace = CodeNamer.to_python_case(yaml_code_model["info"]["title"])
        namespace = Path(*[ns_part for ns_part in namespace.split(".")])

        template = env.get_template("operations_container.py.jinja2")
        for operation_group in operation_groups:
            operation_group_content = template.render(
                operation_group=operation_group,
                imports=FileImportSerializer(operation_group.imports())
            )
            self._autorestapi.write_file(
                namespace / Path("operations") / Path(f"{operation_group.name}_operation_group.py"),
                operation_group_content
            )

        # Write it
        self._autorestapi.write_file(namespace / Path("service_client.py"), generic_serializer.service_client_file())
        self._autorestapi.write_file(namespace / Path("models") / Path("_models.py"), generic_serializer.model_file())
        self._autorestapi.write_file(namespace / Path("models") / Path("_models_py3.py"), python3_serializer.model_file())
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