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
from typing import Optional, Dict

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
EMITTER_OPTIONS = {
    "resiliency/srv-driven/old.tsp": {
        "package-name": "resiliency-srv-driven1",
        "package-mode": "dataplane",
        "package-pprint-name": "ResiliencySrvDriven1",
    },
    "resiliency/srv-driven/main.tsp": {
        "package-name": "resiliency-srv-driven2",
        "package-mode": "dataplane",
        "package-pprint-name": "ResiliencySrvDriven2",
    },
    "authentication/union/main.tsp": {
        "package-name": "authentication-union",
    },
    "type/array/main.tsp": {
        "package-name": "typetest-array",
    },
    "type/dictionary/main.tsp": {
        "package-name": "typetest-dictionary",
    },
    "type/enum/extensible/main.tsp": {
        "package-name": "typetest-enum-extensible",
    },
    "type/enum/fixed/main.tsp": {
        "package-name": "typetest-enum-fixed",
    },
    "type/model/inheritance/main.tsp": {
        "package-name": "typetest-model-inheritance",
    },
    "type/model/usage/main.tsp": {
        "package-name": "typetest-model-usage",
    },
    "type/model/visibility/main.tsp": {
        "package-name": "typetest-model-visibility",
    },
    "type/property/nullable/main.tsp": {
        "package-name": "typetest-property-nullable",
    },
    "type/property/optional/main.tsp": {
        "package-name": "typetest-property-optional",
    },
    "type/property/value-types/main.tsp": {
        "package-name": "typetest-property-valuetypes",
    },
    "type/union/main.tsp": {
        "package-name": "typetest-union",
    },
}


def _get_emitter_option(spec: Path) -> Dict[str, str]:
    name = str(spec.relative_to(CADL_RANCH_DIR)).replace(os.sep, "/")
    return EMITTER_OPTIONS.get(name, {})


def _add_options(spec: Path, debug=False) -> str:
    options = {
        "emitter-output-dir": f"{PLUGIN_DIR}/test/generated/{_get_package_name(spec)}"
    }
    # if debug:
    #   options["debug"] = "true"
    options.update(_get_emitter_option(spec))
    return " --option ".join(
        [f"@azure-tools/typespec-python.{k}={v} " for k, v in options.items()]
    )


@task
def regenerate(c, name=None, debug=False):
    specs = [
        s / "main.tsp"
        for s in CADL_RANCH_DIR.glob("**/*")
        if s.is_dir()
        and any(f for f in s.iterdir() if f.name == "main.tsp")
        and "internal" not in s.name.lower()
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
        Path(f"{PLUGIN_DIR}/test/generated/{_get_package_name(spec)}").mkdir(
            parents=True, exist_ok=True
        )
    _run_cadl(
        [
            f"tsp compile {spec} --emit={PLUGIN_DIR} --option {_add_options(spec, debug)}"
            for spec in specs
        ]
    )


def _get_package_name(spec: Path):
    if _get_emitter_option(spec).get("package-name"):
        return _get_emitter_option(spec)["package-name"]
    return (
        str(spec.relative_to(CADL_RANCH_DIR))
        .replace(f"{os.sep}main.tsp", "")
        .replace(os.sep, "-")
    )


def _run_cadl(cmds):
    if len(cmds) == 1:
        success = _run_single_cadl(cmds[0])
    else:
        with Pool() as pool:
            result = pool.map(_run_single_cadl, cmds)
        success = all(result)
    if not success:
        raise SystemExit("Cadl generation fails")


def _run_single_cadl(cmd):
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
