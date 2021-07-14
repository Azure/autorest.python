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
from lrowithparameterizedendpoints.aio import LROWithParamaterizedEndpoints
from async_generator import yield_, async_generator

@pytest.fixture
@async_generator
async def client(credential):
    async with LROWithParamaterizedEndpoints(credential=credential, host="host:3000") as client:
        await yield_(client)

@pytest.mark.asyncio
async def test_poll_with_parameterized_endpoints(client):
    poller = await client.begin_poll_with_parameterized_endpoints(account_name='local', polling_interval=0)
    assert (await poller.result()) == 'success'

@pytest.mark.asyncio
async def test_poll_with_constant_parameterized_endpoints(client):
    poller = await client.begin_poll_with_constant_parameterized_endpoints(account_name='local', polling_interval=0)
    assert (await poller.result()) == 'success'
