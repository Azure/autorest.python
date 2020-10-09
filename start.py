#!/usr/bin/env python

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import sys
if not sys.version_info >= (3, 6, 0):
    raise Exception("Autorest for Python extension requires Python 3.6 at least")

from pathlib import Path
import venv

from venvtools import python_run

_ROOT_DIR = Path(__file__).parent


def main():
    venv_path = _ROOT_DIR / "venv"
    venv_prexists = venv_path.exists()

    assert venv_prexists  # Otherwise install was not done

    env_builder = venv.EnvBuilder(with_pip=True)
    venv_context = env_builder.ensure_directories(venv_path)
    command = "debug" if (len(sys.argv) > 1 and sys.argv[1] == 'debug') else None

    python_run(venv_context, "autorest.jsonrpc.server", command=command)

if __name__ == "__main__":
    main()
