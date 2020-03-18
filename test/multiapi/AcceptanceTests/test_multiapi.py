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
import requests
from azure.core.pipeline.policies import SansIOHTTPPolicy
from multiapi.models import *
from multiapi import MultiapiTest

@pytest.fixture
def credential():
    class FakeCredential:
        pass
    return FakeCredential()

@pytest.fixture
def authentication_policy():
    return SansIOHTTPPolicy()

@pytest.fixture
def default_client(credential, authentication_policy):
    with MultiapiTest(
		base_url="http://localhost:3000",
        credential=credential,
        authentication_policy=authentication_policy
    ) as default_client:
        yield default_client

@pytest.fixture
def client(credential, authentication_policy, api_version):
    with MultiapiTest(
		base_url="http://localhost:3000",
        api_version=api_version,
        credential=credential,
        authentication_policy=authentication_policy
    ) as client:
        yield client

class TestMultiapiClient(object):

    def test_default_api_version_of_multiapi_client(self, default_client):
        assert default_client.DEFAULT_API_VERSION == "3.0.0"

    # operation mixins

    def test_default_operation_mixin(self, default_client):
        response = default_client.test_one(id=1)
        assert response == ModelTwo(id=1, message="This was called with api-version 2.0.0")

    @pytest.mark.parametrize('api_version', ["1.0.0"])
    def test_specificy_api_version_operation_mixin(self, client):
        response = client.test_one(id=1)
        assert response is None

    @pytest.mark.parametrize('api_version', ["3.0.0"])
    def test_specify_api_version_with_no_mixin(self, client):
        with pytest.raises(NotImplementedError):
            client.test_one(id=1)
