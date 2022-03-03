# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import sys
import subprocess
import os
import signal
from os.path import dirname, realpath
from azure.core.pipeline.policies import SansIOHTTPPolicy
from msrest import Serializer, Deserializer
import pytest


cwd = dirname(realpath(__file__))

#Ideally this would be in a common helper library shared between the tests
def start_server_process():
    cmd = "node {}/../../../../node_modules/@microsoft.azure/autorest.testserver/dist/cli/cli.js run --appendCoverage".format(cwd)
    if os.name == 'nt': #On windows, subprocess creation works without being in the shell
        return subprocess.Popen(cmd)

    return subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid) #On linux, have to set shell=True

#Ideally this would be in a common helper library shared between the tests
def terminate_server_process(process):
    if os.name == 'nt':
        process.kill()
    else:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)  # Send the signal to all the process groups

@pytest.fixture(scope="session")
def testserver():
    """Start the Autorest testserver."""
    server = start_server_process()
    yield
    terminate_server_process(server)

@pytest.fixture()
def base_send_request():
    def send_request(client, request, **kwargs):
        response = client.send_request(request, **kwargs)
        response.raise_for_status()
        return response
    return send_request

@pytest.fixture()
def base_send_request_json_response():
    def send_request_json_response(client, request, **kwargs):
        response = client.send_request(request, **kwargs)
        response.raise_for_status()
        return response.json()
    return send_request_json_response

class CookiePolicy(SansIOHTTPPolicy):
    def __init__(self, *args, **kwargs):
        self._current_cookie = None

    def on_request(self, request, **kwargs):
        http_request = request.http_request
        if self._current_cookie:
            http_request.headers["Cookie"] = self._current_cookie
            self._current_cookie = None

    def on_response(self, request, response, **kwargs):
        http_response = response.http_response

        if "Set-Cookie" in http_response.headers:
            self._current_cookie = http_response.headers["Set-Cookie"]

@pytest.fixture()
def cookie_policy():
    return CookiePolicy()


@pytest.fixture()
def credential():
    """I actually don't need anything, since the authentication policy
    will bypass it.
    """
    class FakeCredential:
        pass
    return FakeCredential()

@pytest.fixture()
def authentication_policy():
    return SansIOHTTPPolicy()

@pytest.fixture()
def serializer():
    return Serializer()

@pytest.fixture()
def deserializer():
    return Deserializer()
