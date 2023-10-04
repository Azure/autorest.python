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
from typing import Dict, List
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
LOCAL_SPECIFICATION_DIR = PLUGIN_DIR / Path("test/specification")
ALL_SPECIFICATION_DIRS = [CADL_RANCH_DIR] #, LOCAL_SPECIFICATION_DIR]
SKIP_FOLDERS = ["type/model/inheritance/enum-discriminator"]
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
        {"package-name": "azure-mgmt-spheredpg", "models-mode": "dpg"},
        {"package-name": "azure-mgmt-spheremsrest"},
    ]
}

def _package_name_folder(spec: Path) -> str:
    for item in ALL_SPECIFICATION_DIRS:
        if item.as_posix() in spec.as_posix():
            return spec.relative_to(item).as_posix()
    raise ValueError(f"Cannot find package name for {spec}")

def _default_package_name(spec: Path) -> str:
    return _package_name_folder(spec).replace("/", "-")

def _get_emitter_option(spec: Path) -> List[Dict[str, str]]:
    name = _package_name_folder(spec)
    result = EMITTER_OPTIONS.get(name, [])
    if isinstance(result, dict):
        return [result]
    return result


def _add_options(spec: Path, debug=False) -> List[str]:
    # if debug:
    #   options["debug"] = "true"
    result = []
    for config in _get_emitter_option(spec):
        config_copy = copy.copy(config)
        config_copy["emitter-output-dir"] = f"{PLUGIN_DIR}/test/generated/{config['package-name']}"
        result.append(config_copy)
    if not result:
        result.append({"emitter-output-dir": f"{PLUGIN_DIR}/test/generated/{_default_package_name(spec)}"})
    return [" --option ".join(
        [f"@azure-tools/typespec-python.{k}={v} " for k, v in options.items()]
    ) for options in result]


def _entry_file_name(path: Path) -> Path:
    if path.is_file():
        return path
    return (path / "client.tsp") if (path / "client.tsp").exists() else (path / "main.tsp")

def all_specification_folders() -> List[Path]:
    return [s for item in ALL_SPECIFICATION_DIRS for s in item.glob("**/*") if s.is_dir()]

@task
def regenerate(c, name=None, debug=False):
    specs = [
        s for s in all_specification_folders()
        if any(f for f in s.iterdir() if f.name == "main.tsp") and not any(item in s.as_posix() for item in SKIP_FOLDERS)
    ]
    if name:
        specs = [s for s in specs if name.lower() in str(s)]
    if not name or name in "resiliency/srv-driven":
        specs.extend(
            [
                s / "old.tsp"
                for s in CADL_RANCH_DIR.glob("**/*")
                if s.is_dir() and any(f for f in s.iterdir() if f.name == "old.tsp")
            ]
        )
    for spec in specs:
        for pacakge_name in _get_package_names(spec):
            Path(f"{PLUGIN_DIR}/test/generated/{pacakge_name}").mkdir(
                parents=True, exist_ok=True
            )
    _run_cadl(
        [
            f"tsp compile {_entry_file_name(spec)} --emit={PLUGIN_DIR} --option {option}"
            for spec in specs for option in _add_options(spec, debug)
        ]
    )

    regenerate_unittests(c)


@task
def regenerate_unittests(c):
    shutil.copyfile(
        "../autorest.python/autorest/codegen/templates/model_base.py.jinja2",
        "test/unittests/generated/model_base.py"
    )


def _get_package_names(spec: Path) -> List[str]:
    result = [config["package-name"] for config in _get_emitter_option(spec)]
    if not result:
        result.append(_default_package_name(spec))
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
