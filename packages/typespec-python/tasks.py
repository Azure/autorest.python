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
PYTHON_TPYESPEC_DIR = PLUGIN_DIR / Path("test/python_typespec")
EMITTER_OPTIONS = {
    "hello": {
        "package-name": "azure-hello",
        "package-mode": "dataplane",
        "package-pprint-name": "Hello",
    }
}


def _add_options(spec, debug=False):
    name = spec.stem.lower()
    options = {"emitter-output-dir": f"{PLUGIN_DIR}/test/generated/{_get_package_name(spec)}"}
    # if debug:
    #   options["debug"] = "true"
    options.update(EMITTER_OPTIONS.get(name, {}))
    return " --option ".join(
        [f"@azure-tools/typespec-python.{k}={v} " for k, v in options.items()]
    )


@task
def regenerate(c, name=None, debug=False):
    specs = [
        s for dir in (CADL_RANCH_DIR, PYTHON_TPYESPEC_DIR) for s in dir.glob("**/*")
        if s.is_dir() and any(f for f in s.iterdir() if f.name == "main.tsp")
    ]
    if name:
        specs = [s for s in specs if name.lower() in s.stem.lower()]
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
    prefix_path = str(spec.parent).replace(str(CADL_RANCH_DIR), "").replace(str(PYTHON_TPYESPEC_DIR), "")
    if prefix_path:
        return (
            "-".join(prefix_path.split(os.sep)[1:])
            + "-"
            + spec.name
        )
    else:
        return spec.name


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
