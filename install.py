#!/usr/bin/env python

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import sys
if not sys.version_info >= (3, 6, 0):
    raise Exception("Autorest for Python extension requires Python 3.6 at least")

try:
    import pip
except ImportError:
    raise Exception("Your Python installation doesn't have pip available")

try:
    import venv
except ImportError:
    raise Exception("Your Python installation doesn't have venv available")


# Now we have pip and Py >= 3.6, go to work

import os.path
import subprocess
from pathlib import Path

from venvtools import create

_ROOT_DIR = Path(__file__).parent


def python_run(venv_context, module, command, *, additional_dir=".", error_ok=False):
    try:
        print("Executing: {} from {}".format(command, additional_dir))
        subprocess.run(
            [
                venv_context.env_exe,
                "-m", module
            ] + command.split(),
            cwd=_ROOT_DIR / additional_dir,
        )
        print()
    except subprocess.CalledProcessError as err:
        print(err, file=sys.stderr)
        if not error_ok:
            sys.exit(1)


def main():
    venv = _ROOT_DIR / "venv"
    venv_prexists = venv.exists()

    # Run the venv creation nonetheless, since it's fast if it already exists and is the best way to
    # get the executable path cross-platform
    venv = create(venv, with_pip=True)
    if not venv_prexists:
        python_run(venv, "pip", "-U pip")
        python_run(venv, "pip", "install {}".format(_ROOT_DIR))

if __name__ == "__main__":
    main()
