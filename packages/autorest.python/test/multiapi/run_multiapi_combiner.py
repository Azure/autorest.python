# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
# coding: utf-8
import sys
import os
from pathlib import Path
from subprocess import check_call, call
import tempfile
import venv

def main():
    test_root = Path(os.getcwd()) / "test/multiapi"
    # clone subfolder of azure-sdk-for-python
    os.chdir(test_root)
    call("git clone --filter=blob:none --sparse https://github.com/Azure/azure-sdk-for-python.git", shell=True)
    os.chdir("azure-sdk-for-python")
    check_call("git sparse-checkout add tools/azure-sdk-tools", shell=True)
    check_call("git pull origin main", shell=True)

    with tempfile.TemporaryDirectory() as temp_dir:
        # install multiapi_combiner in venv
        env_builder = venv.EnvBuilder(with_pip=True)
        env_builder.create(temp_dir)
        venv_context = env_builder.ensure_directories(temp_dir)

        os.chdir(Path("tools/azure-sdk-tools"))
        check_call([venv_context.env_exe, "-m", "pip", "install", "-e", "."])

        # install test module and run multiapi_combiner
        for test_module in sys.argv[1:]:
            os.chdir(test_root / f"Expected/AcceptanceTests/{test_module}")
            check_call([venv_context.env_exe, "-m", "pip", "install", "-e", "."])
            check_call([venv_context.env_exe, "-m", "packaging_tools.multiapi_combiner", "--pkg-path", os.getcwd()])

if __name__ == '__main__':
    main()
