#!/usr/bin/env python

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import sys

if not sys.version_info >= (3, 8, 0):
    raise Exception("Autorest for Python extension requires Python 3.8 at least")

try:
    import pip
except ImportError:
    raise Exception("Your Python installation doesn't have pip available")

try:
    import venv
except ImportError:
    raise Exception("Your Python installation doesn't have venv available")


# Now we have pip and Py >= 3.8, go to work

from pathlib import Path
import shutil

from venvtools import python_run

_ROOT_DIR = Path(__file__).parent.parent


def ignore_node_modules(dirname, filenames):
    return ["node_modules"] if "node_modules" in filenames else []


def main():
    # Define the source and destination directories
    source_dir = _ROOT_DIR.parent / "pygen"
    dest_dir = _ROOT_DIR / "node_modules" / "pygen"

    # Copy the source directory to the destination directory
    shutil.copytree(source_dir, dest_dir, dirs_exist_ok=True, ignore=ignore_node_modules)

    # we use pygen's venv
    venv_path = dest_dir / "venv"
    assert venv_path.exists()  # Otherwise install was not done

    env_builder = venv.EnvBuilder(with_pip=True)
    venv_context = env_builder.ensure_directories(venv_path)
    # install autorest.python specific stuff into it
    python_run(venv_context, "pip", ["install", "-r", "requirements.txt"])
    python_run(venv_context, "pip", ["install", "-e", str(_ROOT_DIR)])


if __name__ == "__main__":
    main()
