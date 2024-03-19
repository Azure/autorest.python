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
from typing import Dict, List, Any, Optional, Literal
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
    "type/model/inheritance/recursive": {
        "package-name": "typetest-model-recursive",
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
    "type/property/additional-properties": {
        "package-name": "typetest-property-additionalproperties",
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
        {"package-name": "azure-mgmt-spheredpg"},
        {"package-name": "azure-mgmt-spheremsrest", "models-mode": "msrest"},
    ],
}


def _package_name_folder(spec: Path, category: Literal["azure", "unbranded"]) -> str:
    for item in _get_specification_dirs(category):
        if item.as_posix() in spec.as_posix():
            return spec.relative_to(item).as_posix()
    raise ValueError(f"Cannot find package name for {spec}")


def _default_package_name(spec: Path, category: Literal["azure", "unbranded"]) -> str:
    return _package_name_folder(spec, category).replace("/", "-")


def _get_emitter_option(
    spec: Path, category: Literal["azure", "unbranded"]
) -> List[Dict[str, str]]:
    name = _package_name_folder(spec, category)
    result = EMITTER_OPTIONS.get(name, [])
    if isinstance(result, dict):
        return [result]
    return result


def _add_options(
    spec: Path,
    category: Literal["azure", "unbranded"],
    generated_foder: Path,
    special_flags: Dict[str, Any],
    debug=False,
) -> List[str]:
    result = []
    for config in _get_emitter_option(spec, category):
        config_copy = copy.copy(config)
        config_copy[
            "emitter-output-dir"
        ] = f"{generated_foder}/{config['package-name']}"
        result.append(config_copy)
    if not result:
        result.append(
            {
                "emitter-output-dir": f"{generated_foder}/{_default_package_name(spec, category)}"
            }
        )
    emitter_configs = []
    for options in result:
        emitter_option = ""
        if debug:
            emitter_option += " --option @azure-tools/typespec-python.debug=true"
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

def _get_specification_dirs(category: Literal["azure", "unbranded"]) -> List[Path]:
    # we should remove the need for this by removing our local definition of mgmt sphere
    local_specification_folder = Path(f"test/{category}/specification")
    return (
        [CADL_RANCH_DIR, local_specification_folder]
        if local_specification_folder.exists()
        else [CADL_RANCH_DIR]
    )

def _all_specification_folders(category: Literal["azure", "unbranded"], filename: str = "main.tsp") -> List[Path]:

    return [
        s
        for item in _get_specification_dirs(category)
        for s in item.glob("**/*")
        if s.is_dir() and any(f for f in s.iterdir() if f.name == filename)
    ]

def _regenerate(
    c,
    specs: List[Path],
    category: Literal["azure", "unbranded"],
    name: Optional[str] = None,
    debug: bool = False,
    special_flags={},
):
    generated_folder = Path(f"{PLUGIN_DIR}/test/{category}/generated")
    if name:
        specs = [s for s in specs if name.lower() in str(s)]
    if not name or name in "resiliency/srv-driven":
        specs.extend(
            s / "old.tsp" for s in _all_specification_folders(category, filename="old.tsp")
        )
    for spec in specs:
        for package_name in _get_package_names(spec, category):
            (generated_folder / package_name).mkdir(parents=True, exist_ok=True)
    _run_cadl(
        [
            f"tsp compile {_entry_file_name(spec)} --emit={PLUGIN_DIR} {option}"
            for spec in specs
            for option in _add_options(
                spec, category, generated_folder, special_flags, debug
            )
        ]
    )


def is_invalid_folder(s: Path, invalid_folders: List[str] = []) -> bool:
    if "sphere" in str(s) or len(invalid_folders) == 0:
        return False
    return any(n in s.relative_to(CADL_RANCH_DIR).as_posix() for n in invalid_folders)


@task
def regenerate_azure(c, name=None, debug=False):
    specs = [
        s
        for s in _all_specification_folders("azure")
        if not is_invalid_folder(s)
    ]
    special_flags = {"flavor": "azure"}
    _regenerate(
        c,
        specs,
        "azure",
        name,
        debug,
        special_flags=special_flags,
    )




@task
def regenerate_unbranded(c, name=None, debug=False):
    specs = [
        s
        for s in _all_specification_folders("unbranded")
        if not is_invalid_folder(s, invalid_folders=["azure", "client-request-id"])
    ]
    special_flags = {"company-name": "Unbranded"}
    _regenerate(
        c,
        specs,
        "unbranded",
        name=name,
        debug=debug,
        special_flags=special_flags,
    )


@task
def regenerate(
    c,
    name=None,
    debug=False,
    flavor: Optional[Literal["azure", "unbranded"]] = None,
):  
    if flavor == "azure":
        return regenerate_azure(c, name, debug)
    if flavor == "unbranded":
        return regenerate_unbranded(c, name, debug)
    regenerate_azure(c, name, debug)
    regenerate_unbranded(c, name, debug)

def _get_package_names(spec: Path, category: Literal["azure", "unbranded"]) -> List[str]:
    result = [
        config["package-name"]
        for config in _get_emitter_option(spec, category)
    ]
    if not result:
        result.append(_default_package_name(spec, category))
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
