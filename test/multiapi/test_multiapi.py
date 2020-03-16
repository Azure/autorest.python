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
import pytest
from autorest.multiapi import MultiapiTest
from wiremock.constants import Config
from wiremock.client import *
from wiremock_mappings import mapping

@pytest.fixture()
def credential():
    """I actually don't need anything, since the authentication policy
    will bypass it.
    """
    class FakeCredential:
        pass
    return FakeCredential()

@pytest.fixture
def client(credential):
    with MultiapiTest(credential, base_url="http://localhost:3000") as client:
        yield client

@pytest.fixture
def wm():
    with WireMockServer() as wm:
        Config.base_url = "http://localhost:3000"
        Mappings.create_mapping(mapping)
        yield wm

def test_api_version_of_multiapi_client(client):
        assert client.DEFAULT_API_VERSION == "3.0.0"