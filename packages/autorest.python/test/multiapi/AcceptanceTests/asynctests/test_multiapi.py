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
from async_generator import yield_, async_generator
import pytest
import inspect
import json
from azure.profiles import KnownProfiles
from azure.mgmt.core import AsyncARMPipelineClient
from azure.mgmt.core.policies import ARMHttpLoggingPolicy
from .multiapi_base import NotTested


@pytest.fixture
@async_generator
async def default_client(credential, authentication_policy):
    from multiapi.aio import MultiapiServiceClient

    async with MultiapiServiceClient(
        base_url="http://localhost:3000", credential=credential, authentication_policy=authentication_policy
    ) as default_client:
        await yield_(default_client)


@pytest.fixture
@async_generator
async def client(credential, authentication_policy, api_version):
    from multiapi.aio import MultiapiServiceClient

    async with MultiapiServiceClient(
        base_url="http://localhost:3000",
        api_version=api_version,
        credential=credential,
        authentication_policy=authentication_policy,
    ) as client:
        await yield_(client)


@pytest.fixture
def namespace_models():
    from multiapi import models

    return models


@pytest.mark.parametrize("api_version", ["2.0.0"])
def test_specify_api_version_multiapi_client(client):
    assert client.profile.label == "multiapi.MultiapiServiceClient 2.0.0"


def test_configuration_kwargs(default_client):
    # making sure that the package name is correct in the sdk moniker
    assert default_client._config.user_agent_policy._user_agent.startswith("azsdk-python-multiapi/")


def test_pipeline_client(default_client):
    # assert the pipeline client is AsyncARMPipelineClient from azure.mgmt.core, since this is mgmt plane
    assert type(default_client._client) == AsyncARMPipelineClient


def test_arm_http_logging_policy_default(default_client):
    assert isinstance(default_client._config.http_logging_policy, ARMHttpLoggingPolicy)
    assert (
        default_client._config.http_logging_policy.allowed_header_names
        == ARMHttpLoggingPolicy.DEFAULT_HEADERS_WHITELIST
    )


@pytest.mark.asyncio
async def test_arm_http_logging_policy_custom(credential):
    from multiapi.aio import MultiapiServiceClient

    http_logging_policy = ARMHttpLoggingPolicy(base_url="test")
    http_logging_policy = ARMHttpLoggingPolicy()
    http_logging_policy.allowed_header_names.update({"x-ms-added-header"})
    async with MultiapiServiceClient(
        base_url="http://localhost:3000", credential=credential, http_logging_policy=http_logging_policy
    ) as default_client:
        assert isinstance(default_client._config.http_logging_policy, ARMHttpLoggingPolicy)
        assert (
            default_client._config.http_logging_policy.allowed_header_names
            == ARMHttpLoggingPolicy.DEFAULT_HEADERS_WHITELIST.union({"x-ms-added-header"})
        )


@pytest.mark.asyncio
async def test_credential_scopes_default(credential):
    from multiapi.aio import MultiapiServiceClient

    async with MultiapiServiceClient(credential=credential) as client:
        assert client._config.credential_scopes == ["https://management.azure.com/.default"]


@pytest.mark.asyncio
async def test_credential_scopes_override(credential):
    from multiapi.aio import MultiapiServiceClient

    async with MultiapiServiceClient(
        credential=credential, credential_scopes=["http://i-should-be-the-only-credential"]
    ) as client:
        assert client._config.credential_scopes == ["http://i-should-be-the-only-credential"]


@pytest.mark.parametrize("api_version", ["0.0.0"])
@pytest.mark.asyncio
async def test_only_operation_groups(client):
    assert client.operation_group_one.test_two  # this is the only function it has access to.
    with pytest.raises(ValueError):
        # make sure it doesn't have access to the other operation group
        client.operation_group_two
    # check that it doesn't have access to a mixin operation
    with pytest.raises(ValueError):
        await client.test_one("1", "hello")


class TestMultiapiClient(NotTested.TestMultiapiBase):
    pass
