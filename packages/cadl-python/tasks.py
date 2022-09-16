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

init()

PLUGIN_DIR = Path(os.path.dirname(__file__))
CADL_RANCH_DIR = PLUGIN_DIR / Path("node_modules/@azure-tools/cadl-ranch-specs")


@task
def regenerate(c, name=None, debug=False):
    specs = [
        s
        for s in CADL_RANCH_DIR.glob("**/*")
        if s.is_dir() and any(f for f in s.iterdir() if f.name == "main.cadl")
    ]
    if name:
        specs = [s for s in specs if name.lower() in s.stem.lower()]
    _run_cadl(
        [
            f"cadl compile {spec} --emit={PLUGIN_DIR}/dist/src/index.js --output-path={PLUGIN_DIR}/test/generated/{spec.name}{' --debug' if debug else ''}"
            for spec in specs
        ]
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
    if result.ok or result.return_code is None:
        print(Fore.GREEN + f'Call "{cmd}" done with success')
        return True
    print(
        Fore.RED
        + f'Call "{cmd}" failed with {result.return_code}\n{result.stdout}\n{result.stderr}'
    )
    output_folder = re.findall(r"--output-path=([^\s]+)", cmd)[0]
    shutil.rmtree(output_folder, ignore_errors=True)
    return False
