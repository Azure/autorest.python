# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from multiprocessing import Pool
import os
from colorama import init, Fore
from invoke import task, run

init()
_AUTOREST_CMD_LINE = "autorest-beta"

service_to_readme_path = {
    'azure-ai-textanalytics': 'test/services/azure-ai-textanalytics/README.md',
    'azure-storage-blob': '../azure-sdk-for-python/sdk/storage/azure-storage-blob/swagger/README.md',
    # 'azure-mgmt-storage': ,
    # 'azure-graphrbac': ,
    # 'azure-cognitiveservices-search-websearch': ,
}

default_mappings = {
  'AcceptanceTests/AdditionalProperties': 'additionalProperties.json',
  'AcceptanceTests/ParameterFlattening': 'parameter-flattening.json',
  'AcceptanceTests/BodyArray': 'body-array.json',
  'AcceptanceTests/BodyBoolean': 'body-boolean.json',
  'AcceptanceTests/BodyByte': 'body-byte.json',
  'AcceptanceTests/BodyComplex': 'body-complex.json',
  'AcceptanceTests/BodyDate': 'body-date.json',
  'AcceptanceTests/BodyDateTime': 'body-datetime.json',
  'AcceptanceTests/BodyDateTimeRfc1123': 'body-datetime-rfc1123.json',
  'AcceptanceTests/BodyDuration': 'body-duration.json',
  'AcceptanceTests/BodyDictionary': 'body-dictionary.json',
  'AcceptanceTests/BodyFile': 'body-file.json',
  'AcceptanceTests/BodyFormData': 'body-formdata.json',
  'AcceptanceTests/BodyInteger': 'body-integer.json',
  'AcceptanceTests/BodyNumber': 'body-number.json',
  'AcceptanceTests/BodyString': 'body-string.json',
  'AcceptanceTests/ExtensibleEnums': ['extensible-enums-swagger.json', 'extensibleenumsswagger'],
  'AcceptanceTests/Header': 'header.json',
  'AcceptanceTests/Http': ['httpInfrastructure.json', 'httpinfrastructure'],
  'AcceptanceTests/Report': 'report.json',
  'AcceptanceTests/RequiredOptional': 'required-optional.json',
  'AcceptanceTests/Url': 'url.json',
  'AcceptanceTests/Validation': 'validation.json',
  'AcceptanceTests/CustomBaseUri': ['custom-baseUrl.json', 'custombaseurl'],
  'AcceptanceTests/CustomBaseUriMoreOptions': ['custom-baseUrl-more-options.json', 'custombaseurlmoreoptions'],
  'AcceptanceTests/ModelFlattening': 'model-flattening.json',
  'AcceptanceTests/Xml': ['xml-service.json', 'xmlservice'],
  'AcceptanceTests/UrlMultiCollectionFormat' : 'url-multi-collectionFormat.json',
  'AcceptanceTests/XmsErrorResponse': 'xms-error-responses.json',
}

default_azure_mappings = {
  'AcceptanceTests/AzureBodyDuration': ['body-duration.json', 'bodyduration'],
  'AcceptanceTests/AzureReport': 'azure-report.json',
  'AcceptanceTests/AzureParameterGrouping': 'azure-parameter-grouping.json',
  'AcceptanceTests/ModelFlattening': 'model-flattening.json',
  'AcceptanceTests/CustomBaseUri': ['custom-baseUrl.json', 'custombaseurl'],
}

# The list is mostly built on Swaggers that uses CloudError feature
# These Swagger should be modified to test their features, and not the CloudError one
default_arm_mappings = {
  'AcceptanceTests/Head': 'head.json',
  'AcceptanceTests/HeadExceptions': 'head-exceptions.json',
  'AcceptanceTests/StorageManagementClient': ['storage.json', 'storage'],
  'AcceptanceTests/Lro': 'lro.json',
  'AcceptanceTests/SubscriptionIdApiVersion': 'subscriptionId-apiVersion.json',
  'AcceptanceTests/Paging': 'paging.json',
  'AcceptanceTests/CustomUrlPaging': ['custom-baseUrl-paging.json', 'custombaseurlpaging'],
  'AcceptanceTests/AzureSpecials': ['azure-special-properties.json', 'azurespecialproperties'],
}

base_dir = os.path.dirname(__file__)

swagger_dir = "node_modules/@microsoft.azure/autorest.testserver/swagger"


@task
def regen_expected(c, opts, debug):
    output_dir = "{}/{}".format(opts['output_base_dir'], opts['output_dir']) if opts.get('output_base_dir') else opts['output_dir']
    keys = opts['mappings'].keys()

    cmds = []
    for key in keys:
        opts_mappings_value = opts['mappings'][key]
        key = key.strip()

        swagger_files = (opts_mappings_value[0] if isinstance(opts_mappings_value, list) else opts_mappings_value).split(';')
        args = [
            "--use={}".format(base_dir),
            # "--{}".format(opts['language']),
            "--clear-output-folder",
            "--output-folder={}/{}".format(output_dir, key),
            "--license-header={}".format(opts['header'] if opts.get('header') else 'MICROSOFT_MIT_NO_VERSION'),
            "--enable-xml",
            "--basic-setup-py",
            "--package-version=0.1.0",
            "--trace",
            "--output-artifact=code-model-v4-no-tags",
        ]

        for swagger_file in swagger_files:
            input_file_name = "{}/{}".format(opts['input_base_dir'], swagger_file) if opts.get('input_base_dir') else swagger_file
            args.append("--input-file={}".format(input_file_name))

        if debug:
            args.append("--debug")

        if opts.get('add_credentials') and opts['add_credentials']:
            args.append("--add-credentials=true")

        if opts.get('vanilla') and opts['vanilla']:
            args.append("--vanilla=true")

        if opts.get('azure_arm') and opts['azure_arm']:
            args.append("--azure-arm=true")

        if opts.get('flattening_threshold'):
            args.append("--payload-flattening-threshold={}".format(opts['flattening_threshold']))

        if opts.get('keep_version') and opts['keep_version']:
            args.append("--keep-version-file=true")

        if opts.get('ns_prefix'):
            if isinstance(opts_mappings_value, list) and len(opts_mappings_value) > 1:
                args.append("--namespace={}".format(opts_mappings_value[1]))
            else:
                namespace = key.split('/')[-1].lower()
                args.append("--namespace={}".format(namespace))

        if opts.get('override-info.version'):
            args.append("--override-info.version={}".format(opts['override-info.version']))
        if opts.get('override-info.title'):
            args.append("--override-info.title={}".format(opts['override-info.title']))
        if opts.get('override-info.description'):
            args.append("--override-info.description={}".format(opts['override-info.description']))

        cmd_line = '{} {}'.format(_AUTOREST_CMD_LINE, " ".join(args))
        print(Fore.YELLOW + f'Queuing up: {cmd_line}')
        cmds.append(cmd_line)

    if len(cmds) == 1:
        run_autorest(cmds[0])
    else:
        # Execute actual taks in parallel
        with Pool() as pool:
            pool.map(run_autorest, cmds)

def run_autorest(cmd_line):
    result = run(cmd_line, warn=True, hide=True)
    if result.ok or result.return_code is None:
        print(Fore.GREEN + f'Call "{cmd_line}" done with success')
    else:
        print(Fore.RED + f'Call "{cmd_line}" failed with {result.return_code}\n{result.stdout}\n{result.stderr}')
    return result


@task
def regenerate_python(c, swagger_name=None, debug=False):
    if swagger_name:
        default_mapping = {k: v for k, v in default_mappings.items() if swagger_name.lower() in k.lower()}
    else:
        default_mapping = default_mappings
    opts = {
        'output_base_dir': 'test/vanilla',
        'input_base_dir': swagger_dir,
        'mappings': default_mapping,
        'output_dir': 'Expected',
        'flattening_threshold': '1',
        'vanilla': True,
        'keep_version': True,
        'ns_prefix': True
    }
    regen_expected(c, opts, debug)


@task
def regenerate_python_azure(c, swagger_name=None, debug=False):
    if swagger_name:
        default_mapping = {k: v for k, v in default_azure_mappings.items() if swagger_name.lower() in k.lower()}
    else:
        default_mapping = default_azure_mappings
    opts = {
        'output_base_dir': 'test/azure',
        'input_base_dir': swagger_dir,
        'mappings': default_mapping,
        'output_dir': 'Expected',
        'flattening_threshold': '1',
        'ns_prefix': True
    }
    regen_expected(c, opts, debug)


@task
def regenerate_python_arm(c, swagger_name=None, debug=False):
    if swagger_name:
        default_mapping = {k: v for k, v in default_arm_mappings.items() if swagger_name.lower() in k.lower()}
    else:
        default_mapping = default_arm_mappings
    opts = {
        'output_base_dir': 'test/azure',
        'input_base_dir': swagger_dir,
        'mappings': default_mapping,
        'output_dir': 'Expected',
        'azure_arm': True,
        'flattening_threshold': '1',
        'ns_prefix': True
    }
    regen_expected(c, opts, debug)


@task
def regenerate(c, swagger_name=None, debug=False):
    # regenerate expected code for tests
    regenerate_python(c, swagger_name, debug)
    regenerate_python_azure(c, swagger_name, debug)
    regenerate_python_arm(c, swagger_name, debug)


@task
def test(c, env=None):
    # run language-specific tests
    cmd = f'tox -e {env}' if env else 'tox'
    os.chdir("{}/test/vanilla/".format(base_dir))
    c.run(cmd)
    os.chdir("{}/test/azure/".format(base_dir))
    c.run(cmd)


@task
def regenerate_services(c, swagger_name=None, debug=False):
    # regenerate service from swagger
    if swagger_name:
        service_mapping = {k: v for k, v in service_to_readme_path.items() if swagger_name.lower() in k.lower()}
    else:
        service_mapping = service_to_readme_path

    cmds = []
    for service in service_mapping:
        readme_path = service_to_readme_path[service]
        service = service.strip()
        cmd_line = f'{_AUTOREST_CMD_LINE} {readme_path} --use=.'
        print(Fore.YELLOW + f'Queuing up: {cmd_line}')
        cmds.append(cmd_line)

    if len(cmds) == 1:
        run_autorest(cmds[0])
    else:
        # Execute actual taks in parallel
        with Pool() as pool:
            pool.map(run_autorest, cmds)