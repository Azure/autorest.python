# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from multiprocessing import Pool
import os
from typing import Any, Dict, Optional
from enum import Enum, auto
from colorama import init, Fore
from invoke import task, run
import shutil
import re

init()
class _SwaggerGroup(Enum):
    VANILLA = auto()
    AZURE = auto()
    AZURE_ARM = auto()

_SERVICE_TO_README_PATH = {
    'azure-ai-textanalytics': 'test/services/azure-ai-textanalytics/README.md',
    'azure-ai-formrecognizer': 'test/services/azure-ai-formrecognizer/README.md',
    'azure-storage-blob': '../azure-sdk-for-python/sdk/storage/azure-storage-blob/swagger/README.md',
    'azure-mgmt-storage': 'test/services/azure-mgmt-storage/README.md',
    'azure-mgmt-network': 'test/services/azure-mgmt-network/README.md',
    'azure-mgmt-resources#features': 'test/services/azure-mgmt-resources#features/README.md',
    'azure-graphrbac': 'test/services/azure-graphrbac/README.md',
    'azure-search': 'test/services/azure-search/README.md',
    'azure-keyvault': 'test/services/azure-keyvault/README.md',
}

_VANILLA_SWAGGER_MAPPINGS = {
    'AdditionalProperties': 'additionalProperties.json',
    'Anything': 'any-type.json',
    'ParameterFlattening': 'parameter-flattening.json',
    'BodyArray': 'body-array.json',
    'BodyBoolean': 'body-boolean.json',
    'BodyByte': 'body-byte.json',
    'BodyComplex': 'body-complex.json',
    'BodyDate': 'body-date.json',
    'BodyDateTime': 'body-datetime.json',
    'BodyDateTimeRfc1123': 'body-datetime-rfc1123.json',
    'BodyDuration': 'body-duration.json',
    'BodyDictionary': 'body-dictionary.json',
    'BodyFile': 'body-file.json',
    'Constants': 'constants.json',
    'BodyFormData': 'body-formdata.json',
    'BodyInteger': 'body-integer.json',
    'BodyNumber': 'body-number.json',
    'BodyString': 'body-string.json',
    'BodyTime': 'body-time.json',
    'ExtensibleEnums': 'extensible-enums-swagger.json',
    'Header': 'header.json',
    'Http': 'httpInfrastructure.json',
    'IncorrectErrorResponse': 'incorrect-error-response.json',
    'Report': 'report.json',
    'RequiredOptional': 'required-optional.json',
    'Url': 'url.json',
    'Validation': 'validation.json',
    'CustomBaseUri': 'custom-baseUrl.json',
    'CustomBaseUriMoreOptions': 'custom-baseUrl-more-options.json',
    'ModelFlattening': 'model-flattening.json',
    'Xml': 'xml-service.json',
    'UrlMultiCollectionFormat' : 'url-multi-collectionFormat.json',
    'XmsErrorResponse': 'xms-error-responses.json',
    'MediaTypes': 'media_types.json',
    'ObjectType': 'object-type.json',
    'NonStringEnums': 'non-string-enum.json',
    'MultipleInheritance': 'multiple-inheritance.json',
    'NoOperations': 'no-operations.json',
    "ReservedWords": "reserved-words.json"
}

_UPDATE_SWAGGER_MAPPINGS = {
    'LLCInitial': 'llc_initial.json',
    'LLCUpdateOne': 'llc_update1.json'
}

_AZURE_SWAGGER_MAPPINGS = {
    'AzureBodyDuration': 'body-duration.json',
    'AzureReport': 'azure-report.json',
    'AzureParameterGrouping': 'azure-parameter-grouping.json',
    'CustomBaseUri': 'custom-baseUrl.json',
    'LroWithParameterizedEndpoints': 'lro-parameterized-endpoints.json',
    'Paging': 'paging.json',
    'CustomUrlPaging': 'custom-baseUrl-paging.json',
}

# The list is mostly built on Swaggers that uses CloudError feature
# These Swagger should be modified to test their features, and not the CloudError one
_AZURE_ARM_SWAGGER_MAPPINGS = {
    'Head': 'head.json',
    'HeadExceptions': 'head-exceptions.json',
    'StorageManagementClient': 'storage.json',
    'Lro': 'lro.json',
    'SubscriptionIdApiVersion': 'subscriptionId-apiVersion.json',
    'AzureSpecials': 'azure-special-properties.json',
}

"""Overwrite default behavior we have assigned to test flags
"""

_OVERWRITE_DEFAULT_NAMESPACE = {
    'ExtensibleEnums': 'extensibleenumsswagger',
    'Http': 'httpinfrastructure',
    'CustomBaseUri': 'custombaseurl',
    'CustomBaseUriMoreOptions': 'custombaseurlmoreoptions',
    'Xml': 'xmlservice',
    'AzureBodyDuration': 'bodyduration',
    'CustomUrlPaging': 'custombaseurlpaging',
    'AzureSpecials': 'azurespecialproperties',
    'StorageManagementClient': 'storage',
    'CustomUrlPaging': 'custombaseurlpaging',
    'LLCInitial': 'llcpackage',
    'LLCUpdateOne': 'llcpackage'
}

_PACKAGES_WITH_CLIENT_SIDE_VALIDATION = [
    'Validation',
    'Url',
    'RequiredOptional',
    'CustomBaseUri',
    'BodyComplex',
    'AzureParameterGrouping',
    'AzureSpecials'
]

def _build_flags(
    package_name: str,
    swagger_name: str,
    debug: bool,
    swagger_group: _SwaggerGroup,
    override_flags: Optional[Dict[str, Any]] = None,
    **kwargs
) -> Dict[str, Any]:
    autorest_dir = os.path.dirname(__file__)
    testserver_dir = "node_modules/@microsoft.azure/autorest.testserver/swagger"

    if swagger_group == _SwaggerGroup.VANILLA:
        generation_section = "vanilla"
    else:
        generation_section = "azure"
    namespace = _OVERWRITE_DEFAULT_NAMESPACE.get(package_name, package_name.lower())
    low_level_client = kwargs.pop("low_level_client", False)
    version_tolerant = kwargs.pop("version_tolerant", False)
    combine_operation_files = kwargs.pop("combine_operation_files", False)
    if low_level_client:
        package_name += "LowLevel"
        generation_section += "/low-level"
        override_flags = override_flags or {}
        override_flags["low-level-client"] = True
        namespace += "lowlevel"
    elif version_tolerant:
        package_name += "VersionTolerant"
        generation_section += "/version-tolerant"
        override_flags = override_flags or {}
        override_flags["version-tolerant"] = True
        namespace += "versiontolerant"
    elif combine_operation_files:
        package_name += "CombineOperationFiles"
        generation_section += "/combine-operation-files"
        override_flags = override_flags or {}
        override_flags["combine-operation-files"] = True
        namespace += "combineoperationfiles"
    else:
        generation_section += "/legacy"
        override_flags = override_flags or {}
        override_flags["payload-flattening-threshold"] = 1

    flags = {
        "use": autorest_dir,
        "clear-output-folder": True,
        "output-folder": f"test/{generation_section}/Expected/AcceptanceTests/{package_name}",
        "license-header": "MICROSOFT_MIT_NO_VERSION",
        "enable-xml": True,
        "basic-setup-py": True,
        "package-version": "0.1.0",
        "output-artifact": "code-model-v4-no-tags",
        "input-file": f"{testserver_dir}/{swagger_name}",
        "add-credential": False,
        "vanilla": swagger_group == _SwaggerGroup.VANILLA,
        "azure-arm": swagger_group == _SwaggerGroup.AZURE_ARM,
        "keep-version-file": True,
        "namespace": namespace,
        "client-side-validation": package_name in _PACKAGES_WITH_CLIENT_SIDE_VALIDATION,
        "black": True,
    }
    if override_flags:
        flags.update(override_flags)
    return flags

def _build_command_line(
    package_name: str,
    swagger_name: str,
    debug: bool,
    swagger_group: _SwaggerGroup,
    override_flags: Optional[Dict[str, Any]] = None,
    **kwargs,
) -> str:
    flags = _build_flags(package_name, swagger_name, debug, swagger_group, override_flags, **kwargs)
    flag_strings = [
        f"--{flag}={value}" for flag, value in flags.items()
    ]
    debug_str = " --python.debugger" if debug else ""
    return "autorest " + " ".join(flag_strings) + debug_str

def _run_autorest(cmds, debug):
    if len(cmds) == 1:
        success = _run_single_autorest(cmds[0], debug=debug)
    else:
        # Execute actual taks in parallel
        with Pool() as pool:
            result = pool.map(_run_single_autorest, cmds)
        success = all(result)
    if not success:
        raise SystemExit("Autorest generation fails")

def _run_single_autorest(cmd_line, debug=False):
    result = run(cmd_line, warn=True, hide=not debug)
    if result.ok or result.return_code is None:
        print(Fore.GREEN + f'Call "{cmd_line}" done with success')
        return True
    print(Fore.RED + f'Call "{cmd_line}" failed with {result.return_code}\n{result.stdout}\n{result.stderr}')

    output_folder = re.findall(r"--output-folder=([^\s]+)", cmd_line)[0]
    shutil.rmtree(output_folder, ignore_errors=True)
    return False

def _regenerate(
    mapping: Dict[str, str],
    debug: bool,
    swagger_group: _SwaggerGroup,
    override_flags: Optional[Dict[str, Any]] = None,
    **kwargs
) -> None:
    cmds = []
    for package_name, swagger_name in mapping.items():
        command_line = _build_command_line(package_name, swagger_name, debug, swagger_group, override_flags, **kwargs)

        print(Fore.YELLOW + f'Queuing up: {command_line}')
        cmds.append(command_line)
    _run_autorest(cmds, debug=debug)

def _prepare_mapping_and_regenerate(c, mapping, swagger_group, swagger_name=None, debug=False, **kwargs):
    if swagger_name:
        prepared_mapping = {k: v for k, v in mapping.items() if swagger_name.lower() in k.lower()}
    else:
        prepared_mapping = mapping
    _regenerate(prepared_mapping, debug, swagger_group=swagger_group, **kwargs)

@task
def regenerate_vanilla_legacy(c, swagger_name=None, debug=False, **kwargs):
    return _prepare_mapping_and_regenerate(c, _VANILLA_SWAGGER_MAPPINGS, _SwaggerGroup.VANILLA, swagger_name, debug, **kwargs)

@task
def regenerate_vanilla_llc(c, swagger_name=None, debug=False, **kwargs):
    mapping = _VANILLA_SWAGGER_MAPPINGS
    mapping.update(_UPDATE_SWAGGER_MAPPINGS)
    return _prepare_mapping_and_regenerate(
        c,
        mapping,
        _SwaggerGroup.VANILLA,
        swagger_name,
        debug,
        low_level_client=True,
        **kwargs
    )

@task
def regenerate_vanilla_version_tolerant(c, swagger_name=None, debug=False, **kwargs):
    mapping = _VANILLA_SWAGGER_MAPPINGS
    mapping.update(_UPDATE_SWAGGER_MAPPINGS)
    return _prepare_mapping_and_regenerate(
        c,
        mapping,
        _SwaggerGroup.VANILLA,
        swagger_name,
        debug,
        version_tolerant=True,
        **kwargs
    )

@task
def regenerate_azure_legacy(c, swagger_name=None, debug=False, **kwargs):
    return _prepare_mapping_and_regenerate(c, _AZURE_SWAGGER_MAPPINGS, _SwaggerGroup.AZURE, swagger_name, debug, **kwargs)

@task
def regenerate_azure_llc(c, swagger_name=None, debug=False, **kwargs):
    return _prepare_mapping_and_regenerate(c, _AZURE_SWAGGER_MAPPINGS, _SwaggerGroup.AZURE, swagger_name, debug, low_level_client=True, **kwargs)

@task
def regenerate_azure_version_tolerant(c, swagger_name=None, debug=False, **kwargs):
    return _prepare_mapping_and_regenerate(c, _AZURE_SWAGGER_MAPPINGS, _SwaggerGroup.AZURE, swagger_name, debug, version_tolerant=True, **kwargs)

@task
def regenerate_azure_combine_operation(c, swagger_name=None, debug=False, **kwargs):
    return _prepare_mapping_and_regenerate(c, _AZURE_SWAGGER_MAPPINGS, _SwaggerGroup.AZURE, swagger_name, debug, combine_operation_files=True, **kwargs)

@task
def regenerate_azure_arm_legacy(c, swagger_name=None, debug=False, **kwargs):
    return _prepare_mapping_and_regenerate(c, _AZURE_ARM_SWAGGER_MAPPINGS, _SwaggerGroup.AZURE_ARM, swagger_name, debug, **kwargs)

@task
def regenerate_azure_arm_llc(c, swagger_name=None, debug=False, **kwargs):
    return _prepare_mapping_and_regenerate(c, _AZURE_ARM_SWAGGER_MAPPINGS, _SwaggerGroup.AZURE_ARM, swagger_name, debug, low_level_client=True, **kwargs)

@task
def regenerate_azure_arm_version_tolerant(c, swagger_name=None, debug=False, **kwargs):
    return _prepare_mapping_and_regenerate(c, _AZURE_ARM_SWAGGER_MAPPINGS, _SwaggerGroup.AZURE_ARM, swagger_name, debug, version_tolerant=True, **kwargs)

@task
def regenerate_azure_arm_combine_operation(c, swagger_name=None, debug=False, **kwargs):
    return _prepare_mapping_and_regenerate(c, _AZURE_ARM_SWAGGER_MAPPINGS, _SwaggerGroup.AZURE_ARM, swagger_name, debug, combine_operation_files=True, **kwargs)

@task
def regenerate_namespace_folders_test(c, debug=False):
    # regenerate a swagger (randomly chose BodyArray) to have a namespace length > 1
    # to test pkgutil logic
    mapping = {'BodyArrayWithNamespaceFolders': 'body-array.json'}
    override_flags = {"namespace": "vanilla.body.array"}
    _regenerate(mapping, debug, swagger_group=_SwaggerGroup.VANILLA, override_flags=override_flags)

@task
def regenerate_credential_default_policy(c, debug=False):
    mapping = {'HeadWithAzureKeyCredentialPolicy': 'head.json'}
    override_flags = {
        "credential-default-policy-type": "AzureKeyCredentialPolicy",
        "credential-key-header-name": "Authorization"
    }
    _regenerate(mapping, debug, swagger_group=_SwaggerGroup.AZURE_ARM, override_flags=override_flags)

@task
def regenerate_package_name_setup_py(c, debug=False):
    mapping = {'BodyByteWithPackageName': 'body-byte.json'}
    override_flags = {
        "package-name": "package-name",
        "override-client-name": "class_name"
    }
    _regenerate(mapping, debug, swagger_group=_SwaggerGroup.VANILLA, override_flags=override_flags)

@task
def regenerate_legacy(c, swagger_name=None, debug=False):
    # regenerate expected code for tests
    regenerate_vanilla_legacy(c, swagger_name, debug)
    regenerate_azure_legacy(c, swagger_name, debug)
    regenerate_azure_arm_legacy(c, swagger_name, debug)
    if not swagger_name:
        regenerate_namespace_folders_test(c, debug)
        regenerate_multiapi(c, debug)
        regenerate_credential_default_policy(c, debug)
        regenerate_package_name_setup_py(c, debug)
        regenerate_custom_poller_pager_legacy(c, debug)
        regenerate_samples(c, debug)
        regenerate_with_python3_operation_files(c, debug)

@task
def regenerate_combine_operation(c, swagger_name=None, debug=False):
    # regenerate expected code for tests
    regenerate_azure_arm_combine_operation(c, swagger_name, debug)
    regenerate_azure_combine_operation(c, swagger_name, debug)

@task
def regenerate(c, swagger_name=None, debug=False):
    regenerate_legacy(c, swagger_name, debug)
    regenerate_llc(c, swagger_name, debug)
    regenerate_version_tolerant(c, swagger_name, debug)
    regenerate_combine_operation(c, swagger_name, debug)

@task
def regenerate_llc(c, swagger_name=None, debug=False):
    regenerate_vanilla_llc(c, swagger_name, debug)
    regenerate_azure_llc(c, swagger_name, debug)
    regenerate_azure_arm_llc(c, swagger_name, debug)

@task
def regenerate_version_tolerant(c, swagger_name=None, debug=False):
    regenerate_vanilla_version_tolerant(c, swagger_name, debug)
    regenerate_azure_version_tolerant(c, swagger_name, debug)
    regenerate_azure_arm_version_tolerant(c, swagger_name, debug)
    if not swagger_name:
        regenerate_custom_poller_pager_version_tolerant(c, debug)

@task
def test(c, env=None):
    # run language-specific tests
    base_dir = os.path.dirname(__file__)
    cmd = f'tox -e {env}' if env else 'tox'
    os.chdir(f"{base_dir}/test/vanilla/")
    c.run(cmd)
    os.chdir(f"{base_dir}/test/azure/")
    c.run(cmd)

def _multiapi_command_line(location, debug):
    cwd = os.getcwd()
    cmd = (
        f'autorest {location} --use=. --multiapi --output-artifact=code-model-v4-no-tags ' +
        f'--python-sdks-folder={cwd}/test/'
    )
    if debug:
        cmd += " --python.debugger"
    return cmd

@task
def regenerate_multiapi(c, debug=False, swagger_name="test"):
    # being hacky: making default swagger_name 'test', since it appears in each spec name
    available_specifications = [
        # create basic multiapi client (package-name=multapi)
        "test/multiapi/specification/multiapi/README.md",
        # create multiapi client with submodule (package-name=multiapi#submodule)
        "test/multiapi/specification/multiapiwithsubmodule/README.md",
        # create multiapi client with no aio folder (package-name=multiapinoasync)
        "test/multiapi/specification/multiapinoasync/README.md",
        # create multiapi client with AzureKeyCredentialPolicy (package-name=multiapicredentialdefaultpolicy)
        "test/multiapi/specification/multiapicredentialdefaultpolicy/README.md",
        # create multiapi client data plane (package-name=multiapidataplane)
        "test/multiapi/specification/multiapidataplane/README.md",
        # multiapi client with custom base url (package-name=multiapicustombaseurl)
        "test/multiapi/specification/multiapicustombaseurl/README.md",
    ]

    cmds = [_multiapi_command_line(spec, debug) for spec in available_specifications if swagger_name.lower() in spec]

    _run_autorest(cmds, debug)

@task
def regenerate_custom_poller_pager_legacy(c, debug=False):
    cwd = os.getcwd()
    cmd = (
        f'autorest test/azure/legacy/specification/custompollerpager/README.md --use=. --python-sdks-folder={cwd}/test/'
    )
    _run_autorest([cmd], debug=debug)

@task
def regenerate_custom_poller_pager_version_tolerant(c, debug=False):
    cwd = os.getcwd()
    cmd = (
        f'autorest test/azure/version-tolerant/specification/custompollerpager/README.md --use=. --python-sdks-folder={cwd}/test/'
    )
    _run_autorest([cmd], debug=debug)

@task
def regenerate_samples(c, debug=False):
    cwd = os.getcwd()
    sample_to_special_flags = {
        "management": None,
        "multiapi": {
            "multiapi": True,
            "python-sdks-folder": f'{cwd}/docs/samples/specification/multiapi'
        },
        "azure_key_credential": None,
        "directives": None,
        "basic": None,
    }

    cmds = []
    for sample, special_flags in sample_to_special_flags.items():
        cmd =  f'autorest docs/samples/specification/{sample}/readme.md --use=.  '
        if special_flags:
            flag_strings = [
                f"--{flag}={value}" for flag, value in special_flags.items()
            ]
            cmd += " ".join(flag_strings)
        cmds.append(cmd)
    _run_autorest(cmds, debug)

@task
def regenerate_with_python3_operation_files(c, debug=False):
    mapping = {'BodyArrayWithPythonThreeOperationFiles': 'body-array.json'}
    override_flags = {"add-python3-operation-files": True}
    _regenerate(mapping, debug, swagger_group=_SwaggerGroup.VANILLA, override_flags=override_flags)
