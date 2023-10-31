# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import os
import subprocess
import signal
import pytest
import re
from typing import Literal
from pathlib import Path

def start_server_process():
    path = Path(os.path.dirname(__file__)) / Path("../../../node_modules/@azure-tools/cadl-ranch-specs")
    os.chdir(path.resolve())
    cmd = "cadl-ranch serve ./http"
    if os.name == "nt":
        return subprocess.Popen(cmd, shell=True)
    return subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid)

def terminate_server_process(process):
    if os.name == 'nt':
        process.kill()
    else:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)  # Send the signal to all the process groups

@pytest.fixture(scope="session", autouse=True)
def testserver():
    """Start cadl ranch mock api tests"""
    server = start_server_process()
    yield
    terminate_server_process(server)


_VALID_UUID = re.compile(r"^[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$")
_VALID_RFC7231 = re.compile(
    r"^(Mon|Tue|Wed|Thu|Fri|Sat|Sun),\s\d{2}\s"
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}\s\d{2}:\d{2}:\d{2}\sGMT$"
)

def validate_format(value: str, format: Literal["uuid", "rfc7231"]):
    if format == "uuid":
        assert _VALID_UUID.match(value)
    elif format == "rfc7231":
        assert _VALID_RFC7231.match(value)
    else:
        raise ValueError("Unknown format")

@pytest.fixture
def check_repeatability_header():
    def func(request):
        validate_format(
            request.http_request.headers["Repeatability-Request-ID"], "uuid"
        )
        validate_format(
            request.http_request.headers["Repeatability-First-Sent"], "rfc7231"
        )
    return func

@pytest.fixture
def check_client_request_id_header():
    def func(request, header: str, checked: dict):
        validate_format(request.http_request.headers[header], "uuid")
        checked[header] = request.http_request.headers[header]
    return func
