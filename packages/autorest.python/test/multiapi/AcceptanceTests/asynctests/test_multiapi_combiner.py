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
from .multiapi_base import NotTested


@pytest.fixture
@async_generator
async def default_client(credential, authentication_policy):
    from multiapicombiner.aio import MultiapiServiceClient
    async with MultiapiServiceClient(
		base_url="http://localhost:3000",
        credential=credential,
        authentication_policy=authentication_policy
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
        authentication_policy=authentication_policy
    ) as client:
        await yield_(client)

@pytest.fixture
def namespace_models():
    from multiapicombiner import models
    return models

class TestMultiapiCombinerClient(NotTested.TestMultiapiBase):
    @pytest.mark.asyncio
    async def test_default_models(self, default_client):
        pass

    @pytest.mark.asyncio
    async def test_specify_api_version_models(self, default_client):
        pass

    @pytest.mark.asyncio
    async def test_default_models_from_operation_group(self, default_client):
        pass

    @pytest.mark.parametrize('api_version', ["1.0.0"])
    @pytest.mark.asyncio
    async def test_lro_and_paging(self, client, namespace_models):
        pass

    @pytest.mark.parametrize('api_version', ["2.0.0"])
    @pytest.mark.asyncio
    async def test_version_two_operation_group_one(self, client, namespace_models):
        pass
