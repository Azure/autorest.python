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

from pathlib import Path
import venv

from venvtools import python_run


def main(root_dir):
    venv_path = root_dir / "venv"
    venv_prexists = venv_path.exists()

    assert venv_prexists  # Otherwise install was not done

    env_builder = venv.EnvBuilder(with_pip=True)
    venv_context = env_builder.ensure_directories(venv_path)
    requirements_path = root_dir / "dev_requirements.txt"
    try:
        python_run(venv_context, "pip", ["install", "-r", str(requirements_path)])
    except FileNotFoundError as e:
        raise ValueError(e.filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run emitter build commands.")
    parser.add_argument("--root", help="Path to the virtual environment")
    args = parser.parse_args()
    main(Path(args.root or Path(__file__).parent))
