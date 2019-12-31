# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from pathlib import Path
import sys

import yaml

from . import Plugin
from .plugins import NameConverter, CloudErrorPlugin
from .models.code_model import CodeModel
from .models import build_schema, EnumSchema, ConstantSchema
from .models.operation_group import OperationGroup
from .models.parameter import Parameter
from .serializers import JinjaSerializer


_LOGGER = logging.getLogger(__name__)


class CodeGenerator(Plugin):

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
        code_model.tracing = self._autorestapi.get_boolean_value("trace", False)

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

    def _build_code_model_options(self):
        azure_arm = self._autorestapi.get_boolean_value("azure-arm", False)
        credential_scopes = self._autorestapi.get_value('credential-scopes')
        if not credential_scopes and azure_arm:
            credential_scopes = "https://management.azure.com/.default"

        license_header = self._autorestapi.get_value("header-text")
        if license_header:
            license_header = license_header.replace("\n", "\n# ")
            license_header = "# --------------------------------------------------------------------------\n# " + license_header
            license_header += "\n# --------------------------------------------------------------------------"

        options = {
            'azure_arm': azure_arm,
            'credential': self._autorestapi.get_boolean_value("add-credentials", False) or self._autorestapi.get_boolean_value('add-credential', False),
            "credential_scopes": credential_scopes.split(",") if credential_scopes else None,
            'head_as_boolean': self._autorestapi.get_boolean_value('head-as-boolean', False),
            'license_header': license_header,
            'keep_version_file': self._autorestapi.get_boolean_value("keep-version-file", False),
            'no_async': self._autorestapi.get_boolean_value("no-async", False),
            'override_client_name': self._autorestapi.get_value("override-client-name"),
            'payload-flattening-threshold': self._autorestapi.get_value("payload-flattening-threshold") or 0,
            'basic_setup_py': self._autorestapi.get_boolean_value("basic-setup-py", False),
            'package_version': self._autorestapi.get_value("package-version"),
            'client_side_validation': self._autorestapi.get_boolean_value('client-side-validation', True)
        }

        if options["basic_setup_py"] and not options['package_version']:
            raise ValueError("--basic-setup-py must be used with --package-version")

        # Force some options in ARM MODE:
        if azure_arm:
            options['credential'] = True
            options['head_as_boolean'] = True
        return options


    def process(self) -> bool:
        # List the input file, should be only one
        inputs = self._autorestapi.list_inputs()
        _LOGGER.debug("Possible Inputs: %s", inputs)
        if "code-model-v4-no-tags.yaml" not in inputs:
            raise ValueError("code-model-v4-no-tags.yaml must be a possible input")

        file_content = self._autorestapi.read_file("code-model-v4-no-tags.yaml")

        # Parse the received YAML
        yaml_code_model = yaml.safe_load(file_content)

        options = self._build_code_model_options()

        if options['azure_arm']:
            CloudErrorPlugin.remove_cloud_errors(yaml_code_model)
        # convert the names to python names
        NameConverter.convert_yaml_names(yaml_code_model, options['override_client_name'])

        code_model = self._create_code_model(yaml_code_model=yaml_code_model, options=options)

        serializer = JinjaSerializer(self._autorestapi)
        serializer.serialize(code_model)

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
