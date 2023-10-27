# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import re
import os
from pathlib import Path
from multiprocessing import Pool
from colorama import init, Fore
from invoke import task, run
import shutil
from typing import Dict, List, Any
import copy

#######################################################
# Working around for issue https://github.com/pyinvoke/invoke/issues/833 in python3.11
import inspect

if not hasattr(inspect, "getargspec"):
    inspect.getargspec = inspect.getfullargspec
#######################################################

init()

PLUGIN_DIR = Path(os.path.dirname(__file__))
PLUGIN = (PLUGIN_DIR / "dist/src/index.js").as_posix()
CADL_RANCH_DIR = PLUGIN_DIR / Path("node_modules/@azure-tools/cadl-ranch-specs/http")
LOCAL_SPECIFICATION_DIR = PLUGIN_DIR / Path("test/azure/specification")
EMITTER_OPTIONS = {
    "resiliency/srv-driven/old.tsp": {
        "package-name": "resiliency-srv-driven1",
        "package-mode": "azure-dataplane",
        "package-pprint-name": "ResiliencySrvDriven1",
    },
    "resiliency/srv-driven": {
        "package-name": "resiliency-srv-driven2",
        "package-mode": "azure-dataplane",
        "package-pprint-name": "ResiliencySrvDriven2",
    },
    "authentication/http/custom": {
        "package-name": "authentication-http-custom",
    },
    "authentication/union": {
        "package-name": "authentication-union",
    },
    "type/array": {
        "package-name": "typetest-array",
    },
    "type/dictionary": {
        "package-name": "typetest-dictionary",
    },
    "type/enum/extensible": {
        "package-name": "typetest-enum-extensible",
    },
    "type/enum/fixed": {
        "package-name": "typetest-enum-fixed",
    },
    "type/model/empty": {
        "package-name": "typetest-model-empty",
    },
    "type/model/inheritance/enum-discriminator": {
        "package-name": "typetest-model-enumdiscriminator",
    },
    "type/model/inheritance/nested-discriminator": {
        "package-name": "typetest-model-nesteddiscriminator",
    },
    "type/model/inheritance/not-discriminated": {
        "package-name": "typetest-model-notdiscriminated",
    },
    "type/model/inheritance/single-discriminator": {
        "package-name": "typetest-model-singlediscriminator",
    },
    "type/model/usage": {
        "package-name": "typetest-model-usage",
    },
    "type/model/visibility": [
        {"package-name": "typetest-model-visibility"},
        {"package-name": "headasbooleantrue", "head-as-boolean": "true"},
        {"package-name": "headasbooleanfalse", "head-as-boolean": "false"},
    ],
    "type/property/nullable": {
        "package-name": "typetest-property-nullable",
    },
    "type/property/optionality": {
        "package-name": "typetest-property-optional",
    },
    "type/scalar": {
        "package-name": "typetest-scalar",
    },
    "type/property/value-types": {
        "package-name": "typetest-property-valuetypes",
    },
    "type/union": {
        "package-name": "typetest-union",
    },
    "azure/core/lro/rpc-legacy": {
        "package-name": "azurecore-lro-rpclegacy",
    },
    "azure/core/lro/rpc": {
        "package-name": "azurecore-lro-rpc",
    },
    "client/structure/multi-client": {
        "package-name": "client-structure-multiclient",
    },
    "client/structure/renamed-operation": {
        "package-name": "client-structure-renamedoperation",
    },
    "client/structure/two-operation-group": {
        "package-name": "client-structure-twooperationgroup",
    },
    "mgmt/sphere": [
        {"package-name": "azure-mgmt-spherejson", "models-mode": "none"},
        {"package-name": "azure-mgmt-spheredpg", "models-mode": "dpg"},
        {"package-name": "azure-mgmt-spheremsrest"},
    ],
}


def _package_name_folder(spec: Path, specification_dirs: List[Path]) -> str:
    for item in specification_dirs:
        if item.as_posix() in spec.as_posix():
            return spec.relative_to(item).as_posix()
    raise ValueError(f"Cannot find package name for {spec}")


def _default_package_name(spec: Path, specification_dirs: List[Path]) -> str:
    return _package_name_folder(spec, specification_dirs).replace("/", "-")


def _get_emitter_option(
    spec: Path, specification_dirs: List[Path]
) -> List[Dict[str, str]]:
    name = _package_name_folder(spec, specification_dirs)
    result = EMITTER_OPTIONS.get(name, [])
    if isinstance(result, dict):
        return [result]
    return result


def _add_options(
    spec: Path,
    specification_dirs: List[Path],
    generated_foder: Path,
    special_flags: Dict[str, Any],
    debug=False,
) -> List[str]:
    # if debug:
    #   options["debug"] = "true"
    result = []
    for config in _get_emitter_option(spec, specification_dirs):
        config_copy = copy.copy(config)
        config_copy[
            "emitter-output-dir"
        ] = f"{generated_foder}/{config['package-name']}"
        result.append(config_copy)
    if not result:
        result.append(
            {
                "emitter-output-dir": f"{generated_foder}/{_default_package_name(spec, specification_dirs)}"
            }
        )
    emitter_configs = []
    for options in result:
        emitter_option = ""
        for item in [options, special_flags]:
            for k, v in item.items():
                emitter_option += f" --option @azure-tools/typespec-python.{k}={v}"
        emitter_configs.append(emitter_option)
    return emitter_configs


def _entry_file_name(path: Path) -> Path:
    if path.is_file():
        return path
    return (
        (path / "client.tsp") if (path / "client.tsp").exists() else (path / "main.tsp")
    )


def all_specification_folders(specification_dirs: List[Path]) -> List[Path]:
    return [s for item in specification_dirs for s in item.glob("**/*") if s.is_dir()]


def _regenerate(
    c,
    name=None,
    debug=False,
    generated_sub_folder="azure",
    skip_folders=[],
    special_flags={},
):
    local_specification_folder = Path(f"test/{generated_sub_folder}/specification")
    specification_dirs = (
        [CADL_RANCH_DIR, local_specification_folder]
        if local_specification_folder.exists()
        else [CADL_RANCH_DIR]
    )
    generated_folder = Path(f"{PLUGIN_DIR}/test/{generated_sub_folder}/generated")

    specs = [
        s
        for s in all_specification_folders(specification_dirs)
        if any(f for f in s.iterdir() if f.name == "main.tsp")
        and not any(
            _package_name_folder(s, specification_dirs).startswith(item)
            for item in skip_folders
        )
    ]
    if name:
        specs = [s for s in specs if name.lower() in str(s)]
    if not name or name in "resiliency/srv-driven":
        specs.extend(
            [
                s / "old.tsp"
                for s in all_specification_folders(specification_dirs)
                if s.is_dir() and any(f for f in s.iterdir() if f.name == "old.tsp")
            ]
        )
    for spec in specs:
        for pacakge_name in _get_package_names(spec, specification_dirs):
            (generated_folder / pacakge_name).mkdir(parents=True, exist_ok=True)
    _run_cadl(
        [
            f"tsp compile {_entry_file_name(spec)} --emit={PLUGIN_DIR} {option}"
            for spec in specs
            for option in _add_options(
                spec, specification_dirs, generated_folder, special_flags, debug
            )
        ]
    )


@task
def regenerate_azure(c, name=None, debug=False):
    _regenerate(c, name, debug)


@task
def regenerate_unbranded(c, name=None, debug=False):
    skip_folders = ["azure/", "mgmt/sphere", "special-headers/client-request-id"]
    special_flags = {"unbranded": "true", "company-name": "Unbranded"}
    _regenerate(
        c,
        name=name,
        debug=debug,
        generated_sub_folder="unbranded",
        skip_folders=skip_folders,
        special_flags=special_flags,
    )


@task
def regenerate(c, name=None, debug=False):
    regenerate_azure(c, name, debug)
    regenerate_unbranded(c, name, debug)
    regenerate_unittests(c)
    regenerate_test_file(c)


@task
def regenerate_unittests(c):
    shutil.copyfile(
        "test/azure/generated/special-words/specialwords/_model_base.py",
        "test/azure/unittests/generated/model_base.py",
    )


@task
def regenerate_test_file(c):
    source_folder = Path("test/azure/mock_api_tests")
    target_folder = Path("test/unbranded/mock_api_tests")
    skip_test_files = [
        "conftest.py",
        # azure test case
        "test_azure_client_generator_core_access.py",
        "test_azure_client_generator_core_usage.py",
        "test_azure_core_basic.py",
        "test_azure_core_traits.py",
        # LRO
        "test_lro_rpc_legacy.py",
        "test_lro_rpc.py",
        "test_lro_standard.py",
        # ARM
        "test_mgmt_models_mode.py",
        # RequestId Policy
        "test_special_headers_client_request_id.py",
        # Customhook Policy
        "test_special_headers_repeatability.py",
        "test_typetest_model_visibility.py",
        # corehttp don't support ODataV4Format
        "test_stream.py",
    ]
    source_test_files = [
        item
        for item in source_folder.glob("**/*")
        if item.is_file()
        and "__pycache__" not in item.parts
        and ".pytest_cache" not in item.parts
    ]
    for source_file in source_test_files:
        if source_file.name.replace("_async", "") in skip_test_files:
            continue
        target_file = target_folder / source_file.relative_to(source_folder)
        target_file.parent.mkdir(parents=True, exist_ok=True)
        if source_file.suffix != ".py":
            shutil.copyfile(source_file, target_file)
        else:
            with open(source_file, "r", encoding="utf-8") as f_in:
                content = f_in.read()
            content = content.replace("azure.core", "corehttp")
            content = content.replace("AzureKeyCredential", "ServiceKeyCredential")
            with open(target_file, "w", encoding="utf-8") as f_out:
                f_out.write(content)


def _get_package_names(spec: Path, specification_dirs: List[Path]) -> List[str]:
    result = [
        config["package-name"]
        for config in _get_emitter_option(spec, specification_dirs)
    ]
    if not result:
        result.append(_default_package_name(spec, specification_dirs))
    return result


def _run_cadl(cmds):
    if len(cmds) == 1:
        success = _run_single_tsp(cmds[0])
    else:
        with Pool() as pool:
            result = pool.map(_run_single_tsp, cmds)
        success = all(result)
    if not success:
        raise SystemExit("Cadl generation fails")


def _run_single_tsp(cmd):
    result = run(cmd, warn=True)
    if result.ok:
        print(Fore.GREEN + f'Call "{cmd}" done with success')
        return True
    print(
        Fore.RED
        + f'Call "{cmd}" failed with {result.return_code}\n{result.stdout}\n{result.stderr}'
    )
    output_folder = re.findall(r"emitter-output-dir=([^\s]+)", cmd)[0]
    shutil.rmtree(output_folder, ignore_errors=True)
    return False
