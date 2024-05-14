#!/usr/bin/env python

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import sys
import argparse

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

import subprocess
from pathlib import Path

from venvtools import ExtendedEnvBuilder, python_run


def main(root_dir):
    venv_path = root_dir / "venv"
    if venv_path.exists():
        env_builder = venv.EnvBuilder(with_pip=True)
        venv_context = env_builder.ensure_directories(venv_path)
    else:
        env_builder = ExtendedEnvBuilder(with_pip=True, upgrade_deps=True)
        env_builder.create(venv_path)
        venv_context = env_builder.context

        python_run(venv_context, "pip", ["install", "-U", "pip"])
        python_run(venv_context, "pip", ["install", "-r", "requirements.txt"])
        python_run(venv_context, "pip", ["install", "-e", str(root_dir)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run emitter build commands.")
    parser.add_argument('--root', help='Path to the virtual environment')

    args = parser.parse_args()
    main(Path(args.root or Path(__file__).parent))
