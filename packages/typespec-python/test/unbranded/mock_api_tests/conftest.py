# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import os
import subprocess
import signal
import pytest
from pathlib import Path

CURRENT_DIR = Path(os.path.dirname(__file__))


def start_server_process():
    path = CURRENT_DIR / Path(
        "../../../node_modules/@azure-tools/cadl-ranch-specs"
    )
    os.chdir(path.resolve())
    cmd = f"cadl-ranch serve ./http --config {CURRENT_DIR}/cadl-ranch-config.yaml"
    if os.name == "nt":
        return subprocess.Popen(cmd, shell=True)
    return subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid)


def terminate_server_process(process):
    if os.name == "nt":
        process.kill()
    else:
        os.killpg(
            os.getpgid(process.pid), signal.SIGTERM
        )  # Send the signal to all the process groups


@pytest.fixture(scope="session", autouse=True)
def testserver():
    """Start cadl ranch mock api tests"""
    server = start_server_process()
    yield
    terminate_server_process(server)
