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

import glob
import sys
import subprocess
import os
import signal
from os.path import dirname, realpath
from unittest import TestLoader, TextTestRunner

from os.path import dirname, pardir, join, realpath

from azure.core.pipeline.policies import SansIOHTTPPolicy
from azure.core.credentials import AccessToken

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

class CookiePolicy(SansIOHTTPPolicy):
    def __init__(self, *args, **kwargs):
        self._current_cookie = None

    def on_request(self, request, **kwargs):
        # type: (PipelineRequest, Any) -> None
        http_request = request.http_request
        if self._current_cookie:
            http_request.headers["Cookie"] = self._current_cookie
            self._current_cookie = None

    def on_response(self, request, response, **kwargs):
        # type: (PipelineRequest, PipelineResponse, Any) -> None
        http_response = response.http_response

        if "Set-Cookie" in http_response.headers:
            self._current_cookie = http_response.headers["Set-Cookie"]

@pytest.fixture()
def cookie_policy():
    return CookiePolicy()

# the token value shall keep same with https://github.com/Azure/autorest.testserver/tree/main/src/test-routes/security.ts
def generate_token(*scopes) -> AccessToken:
    return AccessToken(token=''.join(scopes), expires_on=1800)

@pytest.fixture()
def credential():
    class FakeCredential:
        @staticmethod
        def get_token(*scopes) -> AccessToken:
            return generate_token(*scopes)
    return FakeCredential()

@pytest.fixture()
def credential_async():
    class FakeCredentialAsync:
        @staticmethod
        async def get_token(*scopes) -> AccessToken:
            return generate_token(*scopes)
    return FakeCredentialAsync()
