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
import inspect
import json
from azure.profiles import KnownProfiles

from .multiapi_base import NotTested


@pytest.fixture
def default_client(credential, authentication_policy):
    from multiapiwithsubmodule.submodule import MultiapiServiceClient
    with MultiapiServiceClient(
		base_url="http://localhost:3000",
        credential=credential,
        authentication_policy=authentication_policy
    ) as default_client:
        yield default_client

@pytest.fixture
def client(credential, authentication_policy, api_version):
    from multiapiwithsubmodule.submodule import MultiapiServiceClient
    with MultiapiServiceClient(
		base_url="http://localhost:3000",
        api_version=api_version,
        credential=credential,
        authentication_policy=authentication_policy
    ) as client:
        yield client

@pytest.fixture
def namespace_models():
    from multiapiwithsubmodule.submodule import models
    return models


@pytest.mark.parametrize('api_version', ["2.0.0"])
def test_specify_api_version_multiapi_client(client):
    assert client.profile.label == "multiapiwithsubmodule.MultiapiServiceClient 2.0.0"

def test_configuration_kwargs(default_client):
    # making sure that the package name is correct in the sdk moniker
    assert default_client._config.user_agent_policy._user_agent.startswith("azsdk-python-multiapiwithsubmodule/")

class TestMultiapiSubmodule(NotTested.TestMultiapiBase):
    pass