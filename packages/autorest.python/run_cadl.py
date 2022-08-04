# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import sys
import venv
from pathlib import Path
from venvtools import python_run

_ROOT_DIR = Path(__file__).parent

if __name__ == "__main__":
    venv_path = _ROOT_DIR / "venv"
    venv_prexists = venv_path.exists()

    assert venv_prexists  # Otherwise install was not done

    env_builder = venv.EnvBuilder(with_pip=True)
    venv_context = env_builder.ensure_directories(venv_path)

    # run m2r
    python_run(venv_context, "autorest.m2r.__init__", command=sys.argv[1:])
    python_run(venv_context, "autorest.preprocess.__init__", command=sys.argv[1:])
    python_run(venv_context, "autorest.cadlflags.__init__", command=sys.argv[1:])
    python_run(venv_context, "autorest.codegen.__init__", command=sys.argv[1:])
    python_run(venv_context, "autorest.black.__init__", command=sys.argv[1:])
