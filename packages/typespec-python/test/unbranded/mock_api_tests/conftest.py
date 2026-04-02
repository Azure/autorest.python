# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import os
import subprocess
import signal
import time
import urllib.request
import urllib.error
import pytest
import re
from pathlib import Path
from typing import List

FILE_FOLDER = Path(__file__).parent
# Root of the typespec-python package
PACKAGE_ROOT = FILE_FOLDER.parent.parent.parent

# Server configuration
SERVER_HOST = "localhost"
SERVER_PORT = 3000
SERVER_URL = f"http://{SERVER_HOST}:{SERVER_PORT}"


def wait_for_server(url: str, timeout: int = 60, interval: float = 0.5) -> bool:
    """Wait for the server to be ready by polling the URL."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            urllib.request.urlopen(url, timeout=1)
            return True
        except (urllib.error.URLError, urllib.error.HTTPError, OSError):
            time.sleep(interval)
    return False


def start_server_process():
    """Start the tsp-spector mock API server."""
    http_path = PACKAGE_ROOT / "node_modules/@typespec/http-specs"
    cwd = http_path.resolve()
    cmd = "npx tsp-spector serve ./specs"

    # Add node_modules/.bin to PATH
    env = os.environ.copy()
    node_bin = str(PACKAGE_ROOT / "node_modules" / ".bin")
    env["PATH"] = f"{node_bin}{os.pathsep}{env.get('PATH', '')}"

    if os.name == "nt":
        return subprocess.Popen(cmd, shell=True, cwd=cwd, env=env)
    return subprocess.Popen(cmd, shell=True, cwd=cwd, env=env, preexec_fn=os.setsid)


def terminate_server_process(process):
    if os.name == "nt":
        process.kill()
    else:
        try:
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        except ProcessLookupError:
            pass  # Process already terminated


@pytest.fixture(scope="session", autouse=True)
def testserver():
    """Start spector mock api tests."""
    server = start_server_process()

    # Wait for server to be ready
    if not wait_for_server(SERVER_URL, timeout=60):
        terminate_server_process(server)
        pytest.fail(f"Mock API server failed to start within 60 seconds at {SERVER_URL}")

    yield
    terminate_server_process(server)


SPECIAL_WORDS = [
    "and",
    "as",
    "assert",
    "async",
    "await",
    "break",
    "class",
    "constructor",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "exec",
    "finally",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "try",
    "while",
    "with",
    "yield",
]


@pytest.fixture
def special_words() -> List[str]:
    return SPECIAL_WORDS


@pytest.fixture
def png_data() -> bytes:
    with open(str(FILE_FOLDER / "data/image.png"), "rb") as file_in:
        return file_in.read()


@pytest.fixture
def jpg_data() -> bytes:
    with open(str(FILE_FOLDER / "data/image.jpg"), "rb") as file_in:
        return file_in.read()
