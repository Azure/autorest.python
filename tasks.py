# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import copy
import itertools
from multiprocessing import Pool
import os
from typing import Any, Dict, Optional, Union
from enum import Enum, auto
from colorama import init, Fore
from invoke import task, run
import shutil
import re

init()
class _SwaggerGroup(str, Enum):
    VANILLA = "vanilla"
    AZURE = "azure"
    AZURE_ARM = "azure-arm"
    DPG = "dpg"

class _Generator(Enum):
    LEGACY = "legacy"
    VERSION_TOLERANT = "version_tolerant"
    LOW_LEVEL_CLIENT = "low_level_client"

_VANILLA_SWAGGER_MAPPINGS = {
    'AdditionalProperties': 'additionalProperties.json',
    'Anything': 'any-type.json',
    'ParameterFlattening': 'parameter-flattening.json',
    'BodyArray': 'body-array.json',
    'BodyBinary': 'body-binary.json',
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
    'BodyFormUrlEncodedData': 'body-formdata-urlencoded.json',
    'BodyInteger': 'body-integer.json',
    'BodyNumber': 'body-number.json',
    'BodyString': 'body-string.json',
    'BodyTime': 'body-time.json',
    'ErrorWithSecrets': 'error-with-secrets.json',
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
    'MergePatchJson': 'merge-patch.json',
    'ModelFlattening': 'model-flattening.json',
    'Xml': 'xml-service.json',
    'UrlMultiCollectionFormat' : 'url-multi-collectionFormat.json',
    'XmsErrorResponse': 'xms-error-responses.json',
    'MediaTypes': 'media_types.json',
    'ObjectType': 'object-type.json',
    'NonStringEnums': 'non-string-enum.json',
    'MultipleInheritance': 'multiple-inheritance.json',
    'NoOperations': 'no-operations.json',
    "ParameterizedEndpoint": "parameterized-endpoint.json",
    "ReservedWords": "reserved-words.json",
    "SecurityAadSwagger": "security-aad.json",
    "SecurityKeySwagger": "security-key.json",
}

_DPG_SWAGGER_MAPPINGS = {
    'DPGServiceDrivenInitial': 'dpg-initial.json',
    'DPGServiceDrivenUpdateOne': 'dpg-update1.json',
    'DPGCustomizationInitial': 'dpg-customization.json',
    'DPGCustomizationCustomized': 'dpg-customization.json',
}

_GENERATOR_SPECIFIC_TESTS = {
    _Generator.LEGACY: {
        _SwaggerGroup.VANILLA: {
            "BodyComplexPythonThreeOnly": "body-complex.json",
            'BodyArrayWithNamespaceFolders': 'body-array.json',
            'BodyByteWithPackageName': 'body-byte.json',
            'BodyArrayWithPythonThreeOperationFiles': 'body-array.json',
            'SecurityAadSwaggerCredentialFlag': 'security-aad.json',
            'SecurityKeySwaggerCredentialFlag': 'security-key.json',
        },
        _SwaggerGroup.AZURE_ARM: {
            'HeadWithAzureKeyCredentialPolicy': 'head.json',
            'SecurityAadSwagger': 'security-aad.json',
            'SecurityKeySwagger': 'security-key.json',
        }
    },
    _Generator.VERSION_TOLERANT: {
        _SwaggerGroup.DPG: {
            'DPGTestModels': 'dpg-customization.json',
        }
    },
}

_PACKAGE_NAME_TO_OVERRIDE_FLAGS: Dict[str, Dict[str, Union[bool, str]]] = {
    'DPGTestModels': {
        "models-mode": "msrest",
    },
    'BodyComplexPythonThreeOnly': {
        "python3-only": True,
        "namespace": "bodycomplexpython3only",
        "package-name": "bodycomplexpython3only",
    },
    'BodyArrayWithNamespaceFolders': {
        "namespace": "vanilla.body.array"
    },
    "BodyByteWithPackageName": {
        "package-name": "package-name",
        "override-client-name": "class_name"
    },
    "HeadWithAzureKeyCredentialPolicy": {
        "credential-default-policy-type": "AzureKeyCredentialPolicy",
        "credential-key-header-name": "Authorization"
    },
    "BodyArrayWithPythonThreeOperationFiles": {
        "add-python3-operation-files": True
    },
    "SecurityAadSwaggerCredentialFlag": {
        "add-credential": True,
        "credential-default-policy-type": "AzureKeyCredentialPolicy",
        "title": "SecurityAadSwaggerCredentialFlag",
    },
    "SecurityKeySwaggerCredentialFlag": {
        "add-credential": True,
        "title": "SecurityKeySwaggerCredentialFlag",
    }
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
    override_flags = override_flags or {}
    override_flags.update(_PACKAGE_NAME_TO_OVERRIDE_FLAGS.get(package_name, {}))
    if swagger_group == _SwaggerGroup.VANILLA:
        generation_section = "vanilla"
    elif swagger_group == _SwaggerGroup.DPG:
        generation_section = "dpg"
    else:
        generation_section = "azure"
    namespace = kwargs.pop("namespace", _OVERWRITE_DEFAULT_NAMESPACE.get(package_name, package_name.lower()))
    low_level_client = kwargs.pop("low_level_client", False)
    version_tolerant = kwargs.pop("version_tolerant", False)
    client_side_validation = package_name in _PACKAGES_WITH_CLIENT_SIDE_VALIDATION and not (low_level_client or version_tolerant)
    if low_level_client:
        package_name += "LowLevel"
        generation_section += "/low-level"
        override_flags["low-level-client"] = True
        namespace += "lowlevel"
    elif version_tolerant:
        package_name += "VersionTolerant"
        generation_section += "/version-tolerant"
        override_flags["version-tolerant"] = True
        namespace += "versiontolerant"
    else:
        generation_section += "/legacy"
        override_flags["payload-flattening-threshold"] = 1
        override_flags["reformat-next-link"] = False

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
        "client-side-validation": client_side_validation,
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
    if swagger_group == _SwaggerGroup.DPG:
        # for DPG, we always have to generate multiple packages for swaggers with the same
        # package name, so we override package names
        override_flags = override_flags or {}
        override_flags.update({"package-name": package_name.lower()})
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
    if kwargs.get("low_level_client", False):
        generator = _Generator.LOW_LEVEL_CLIENT
    elif kwargs.get("version_tolerant", False):
        generator = _Generator.VERSION_TOLERANT
    else:
        generator = _Generator.LEGACY
    mapping_copy = copy.copy(mapping)
    mapping_copy.update(_GENERATOR_SPECIFIC_TESTS.get(generator, {}).get(swagger_group, {}))
    if swagger_name:
        prepared_mapping = {k: v for k, v in mapping_copy.items() if swagger_name.lower() in k.lower()}
    else:
        prepared_mapping = mapping_copy
    _regenerate(prepared_mapping, debug, swagger_group=swagger_group, **kwargs)

@task
def regenerate_vanilla_legacy(c, swagger_name=None, debug=False, **kwargs):
    _prepare_mapping_and_regenerate(c, _VANILLA_SWAGGER_MAPPINGS, _SwaggerGroup.VANILLA, swagger_name, debug, **kwargs)
    if not swagger_name:
        regenerate_package_mode(c, swagger_group=_SwaggerGroup.VANILLA)

@task
def regenerate_dpg_low_level_client(c, swagger_name=None, debug=False, **kwargs):
    return _prepare_mapping_and_regenerate(
        c,
        _DPG_SWAGGER_MAPPINGS,
        _SwaggerGroup.DPG,
        swagger_name,
        debug,
        low_level_client=True,
        **kwargs
    )

@task
def regenerate_vanilla_low_level_client(c, swagger_name=None, debug=False, **kwargs):
    return _prepare_mapping_and_regenerate(
        c,
        _VANILLA_SWAGGER_MAPPINGS,
        _SwaggerGroup.VANILLA,
        swagger_name,
        debug,
        low_level_client=True,
        **kwargs
    )

@task
def regenerate_dpg_version_tolerant(c, swagger_name=None, debug=False, **kwargs):
    _prepare_mapping_and_regenerate(
        c,
        _DPG_SWAGGER_MAPPINGS,
        _SwaggerGroup.DPG,
        swagger_name,
        debug,
        version_tolerant=True,
        **kwargs
    )

@task
def regenerate_vanilla_version_tolerant(c, swagger_name=None, debug=False, **kwargs):
    _prepare_mapping_and_regenerate(
        c,
        _VANILLA_SWAGGER_MAPPINGS,
        _SwaggerGroup.VANILLA,
        swagger_name,
        debug,
        version_tolerant=True,
        **kwargs
    )

@task
def regenerate_azure_legacy(c, swagger_name=None, debug=False, **kwargs):
    _prepare_mapping_and_regenerate(c, _AZURE_SWAGGER_MAPPINGS, _SwaggerGroup.AZURE, swagger_name, debug, **kwargs)
    if not swagger_name:
        regenerate_custom_poller_pager_legacy(c, debug)
        regenerate_package_mode(c, swagger_group=_SwaggerGroup.AZURE)

@task
def regenerate_azure_low_level_client(c, swagger_name=None, debug=False, **kwargs):
    return _prepare_mapping_and_regenerate(c, _AZURE_SWAGGER_MAPPINGS, _SwaggerGroup.AZURE, swagger_name, debug, low_level_client=True, **kwargs)

@task
def regenerate_azure_version_tolerant(c, swagger_name=None, debug=False, **kwargs):
    _prepare_mapping_and_regenerate(c, _AZURE_SWAGGER_MAPPINGS, _SwaggerGroup.AZURE, swagger_name, debug, version_tolerant=True, **kwargs)
    if not swagger_name:
        regenerate_custom_poller_pager_version_tolerant(c, debug)

@task
def regenerate_azure_arm_legacy(c, swagger_name=None, debug=False, **kwargs):
    _prepare_mapping_and_regenerate(c, _AZURE_ARM_SWAGGER_MAPPINGS, _SwaggerGroup.AZURE_ARM, swagger_name, debug, **kwargs)

@task
def regenerate_azure_arm_low_level_client(c, swagger_name=None, debug=False, **kwargs):
    return _prepare_mapping_and_regenerate(c, _AZURE_ARM_SWAGGER_MAPPINGS, _SwaggerGroup.AZURE_ARM, swagger_name, debug, low_level_client=True, **kwargs)

@task
def regenerate_azure_arm_version_tolerant(c, swagger_name=None, debug=False, **kwargs):
    return _prepare_mapping_and_regenerate(c, _AZURE_ARM_SWAGGER_MAPPINGS, _SwaggerGroup.AZURE_ARM, swagger_name, debug, version_tolerant=True, **kwargs)

@task
def regenerate_legacy(c, swagger_name=None, debug=False):
    # regenerate expected code for tests
    regenerate_vanilla_legacy(c, swagger_name, debug)
    regenerate_azure_legacy(c, swagger_name, debug)
    regenerate_azure_arm_legacy(c, swagger_name, debug)
    if not swagger_name:
        regenerate_multiapi(c, debug)
        regenerate_samples(c, debug)

@task
def regenerate(
    c,
    swagger_name=None,
    debug=False,
    version_tolerant=False,
    low_level_client=False,
    legacy=False,
    vanilla=False,
    azure=False,
    azure_arm=False,
    dpg=False
):
    if legacy and dpg:
        raise ValueError("Can not specify legacy flag and dpg flag at the same time.")
    generators = [
        "version_tolerant" if version_tolerant else "",
        "low_level_client" if low_level_client else "",
        "legacy" if legacy else "",
    ]
    generators = [g for g in generators if g] or ["legacy", "low_level_client", "version_tolerant"]
    folders = [
        "vanilla" if vanilla else "",
        "azure" if azure else "",
        "azure_arm" if azure_arm else "",
        "dpg" if dpg else "",
    ]
    folder_flags = [f for f in folders if f]
    if not folder_flags:
        mapping = {
            "legacy": regenerate_legacy,
            "low_level_client": regenerate_low_level_client,
            "version_tolerant": regenerate_version_tolerant,
        }
        funcs = [mapping[g] for g in generators if g in mapping.keys()]
    else:
        mapping = {
            ("legacy", "vanilla"): regenerate_vanilla_legacy,
            ("legacy", "azure"): regenerate_azure_legacy,
            ("legacy", "azure_arm"): regenerate_azure_arm_legacy,
            ("version_tolerant", "vanilla"): regenerate_vanilla_version_tolerant,
            ("version_tolerant", "azure"): regenerate_azure_version_tolerant,
            ("version_tolerant", "azure_arm"): regenerate_azure_arm_version_tolerant,
            ("version_tolerant", "dpg"): regenerate_dpg_version_tolerant,
            ("low_level_client", "vanilla"): regenerate_vanilla_low_level_client,
            ("low_level_client", "azure"): regenerate_azure_low_level_client,
            ("low_level_client", "azure_arm"): regenerate_azure_arm_low_level_client,
            ("low_level_client", "dpg"): regenerate_dpg_low_level_client,
        }
        funcs = [
            v for k, v in mapping.items() if k in itertools.product(generators, folder_flags)
        ]
    for func in funcs:
        func(c, swagger_name, debug)

@task
def regenerate_low_level_client(c, swagger_name=None, debug=False):
    regenerate_dpg_low_level_client(c, swagger_name, debug)
    regenerate_vanilla_low_level_client(c, swagger_name, debug)
    regenerate_azure_low_level_client(c, swagger_name, debug)
    regenerate_azure_arm_low_level_client(c, swagger_name, debug)

@task
def regenerate_version_tolerant(c, swagger_name=None, debug=False):
    regenerate_dpg_version_tolerant(c, swagger_name, debug)
    regenerate_vanilla_version_tolerant(c, swagger_name, debug)
    regenerate_azure_version_tolerant(c, swagger_name, debug)
    regenerate_azure_arm_version_tolerant(c, swagger_name, debug)

@task
def test(c):
    # run language-specific tests
    base_dir = os.path.dirname(__file__)
    cmd = 'tox -e ci'

    autorest_types = ["azure", "vanilla"]
    gen_types = ["legacy", "low-level", "version-tolerant"]
    for autorest_type, gen_type in itertools.product(autorest_types, gen_types):
        os.chdir(f"{base_dir}/test/{autorest_type}/{gen_type}")
        c.run(cmd)

    # multiapi
    os.chdir(f"{base_dir}/test/multiapi/")
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
        # create multiapi client with security definition (package-name=multapisecurity)
        "test/multiapi/specification/multiapisecurity/README.md",
    ]

    cmds = [_multiapi_command_line(spec, debug) for spec in available_specifications if swagger_name.lower() in spec]

    _run_autorest(cmds, debug)

@task
def regenerate_package_mode(c, debug=False, swagger_group=None):
    cwd = os.getcwd()
    azure_packages = [
        'test/azure/legacy/specification/packagemodemgmtplane/README.md',
        'test/azure/legacy/specification/packagemodecustomize/README.md',
    ]
    vanilla_packages = [
        'test/vanilla/legacy/specification/packagemodedataplane/README.md',
    ]
    if swagger_group == _SwaggerGroup.VANILLA:
        package_mode = vanilla_packages
    elif swagger_group == _SwaggerGroup.AZURE:
        package_mode = azure_packages
    else:
        package_mode = azure_packages + vanilla_packages
    cmds = [
        f'autorest {readme} --use=. --python-sdks-folder={cwd}/test/' for readme in package_mode
    ]

    _run_autorest(cmds, debug=debug)

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
