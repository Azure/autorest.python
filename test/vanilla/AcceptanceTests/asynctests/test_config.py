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
from azure.core.pipeline.policies import HttpLoggingPolicy
from bodystring.aio import AutoRestSwaggerBATService
from bodybytewithclientsidevalidation.aio import AutoRestSwaggerBATByteService

class TestConfig(object):
    @pytest.mark.asyncio
    async def test_http_logging_policy_default(self):
        async with AutoRestSwaggerBATService(base_url="http://localhost:3000") as client:
            assert isinstance(client._config.http_logging_policy, HttpLoggingPolicy)
            assert client._config.http_logging_policy.allowed_header_names == HttpLoggingPolicy.DEFAULT_HEADERS_WHITELIST

    @pytest.mark.asyncio
    async def test_http_logging_policy_custom(self):
        http_logging_policy = HttpLoggingPolicy(base_url="test")
        http_logging_policy = HttpLoggingPolicy()
        http_logging_policy.allowed_header_names.update(
            {"x-ms-added-header"}
        )
        async with AutoRestSwaggerBATService(base_url="http://localhost:3000", http_logging_policy=http_logging_policy) as client:
            assert isinstance(client._config.http_logging_policy, HttpLoggingPolicy)
            assert client._config.http_logging_policy.allowed_header_names == HttpLoggingPolicy.DEFAULT_HEADERS_WHITELIST.union({"x-ms-added-header"})

    @pytest.mark.asyncio
    async def test_client_side_validation(self):
        async with AutoRestSwaggerBATByteService(base_url="http://localhost:3000") as client:
            assert client._serialize.client_side_validation == True
