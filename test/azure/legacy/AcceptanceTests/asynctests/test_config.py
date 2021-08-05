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
from azure.mgmt.core.policies import ARMHttpLoggingPolicy, AsyncARMChallengeAuthenticationPolicy
# Head is azure-arm
from head.aio import AutoRestHeadTestService

class TestConfig(object):
    @pytest.mark.asyncio
    async def test_arm_http_logging_policy_default(self, credential):
        async with AutoRestHeadTestService(credential, base_url="http://localhost:3000") as client:
            assert isinstance(client._config.http_logging_policy, ARMHttpLoggingPolicy)
            assert client._config.http_logging_policy.allowed_header_names == ARMHttpLoggingPolicy.DEFAULT_HEADERS_WHITELIST

    @pytest.mark.asyncio
    async def test_arm_http_logging_policy_custom(self, credential):
        http_logging_policy = ARMHttpLoggingPolicy(base_url="test")
        http_logging_policy = ARMHttpLoggingPolicy()
        http_logging_policy.allowed_header_names.update(
            {"x-ms-added-header"}
        )
        async with AutoRestHeadTestService(credential, base_url="http://localhost:3000", http_logging_policy=http_logging_policy) as client:
            assert isinstance(client._config.http_logging_policy, ARMHttpLoggingPolicy)
            assert client._config.http_logging_policy.allowed_header_names == ARMHttpLoggingPolicy.DEFAULT_HEADERS_WHITELIST.union({"x-ms-added-header"})

    @pytest.mark.asyncio
    async def test_credential_scopes_default(self, credential):
        async with AutoRestHeadTestService(credential) as client:
            assert client._config.credential_scopes == ['https://management.azure.com/.default']

    @pytest.mark.asyncio
    async def test_credential_scopes_override(self, credential):
        async with AutoRestHeadTestService(credential, credential_scopes=["http://i-should-be-the-only-credential"]) as client:
            assert client._config.credential_scopes == ["http://i-should-be-the-only-credential"]

    @pytest.mark.asyncio
    async def test_arm_authentication_policy_default(self, credential):
        async with AutoRestHeadTestService(credential, base_url="http://localhost:3000") as client:
            assert isinstance(client._config.authentication_policy, AsyncARMChallengeAuthenticationPolicy)