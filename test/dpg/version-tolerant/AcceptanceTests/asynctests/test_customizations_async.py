
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
from dpgcustomizationinitialversiontolerant.aio import DPGClient as DPGClientInitial
from dpgcustomizationcustomizedversiontolerant.aio import DPGClient as DPGClientCustomized
from dpgcustomizationcustomizedversiontolerant.models import *

@pytest.fixture
async def client(client_cls):
    async with client_cls() as client:
        yield client


CLIENTS = [DPGClientInitial, DPGClientCustomized]

@pytest.mark.asyncio
@pytest.mark.parametrize("client_cls", CLIENTS)
async def test_get_raw_model(client):
    assert await client.get_model(mode="raw") == {"received": "raw"}

@pytest.mark.asyncio
@pytest.mark.parametrize("client_cls", [DPGClientCustomized])
async def test_get_customized_model(client):
    assert (await client.get_model("model")).received == "model"

@pytest.mark.asyncio
@pytest.mark.parametrize("client_cls", CLIENTS)
async def test_post_raw_model(client):
    assert (await client.post_model("raw", {"hello": "world!"}))["received"] == "raw"

@pytest.mark.asyncio
@pytest.mark.parametrize("client_cls", [DPGClientCustomized])
async def test_post_customized_model(client):
    assert (await client.post_model("model", Input(hello="world!"))).received == "model"

@pytest.mark.asyncio
@pytest.mark.parametrize("client_cls", CLIENTS)
async def test_get_raw_pages(client):
    assert [p async for p in client.get_pages("raw")] == [{'received': 'raw'}, {'received': 'raw'}]

@pytest.mark.asyncio
@pytest.mark.parametrize("client_cls", [DPGClientCustomized])
async def test_get_customized_pages(client):
    pages = [p async for p in client.get_pages("model")]
    assert all(p for p in pages if isinstance(p, Product))
    assert all(p for p in pages if p.received == "model")

@pytest.mark.asyncio
@pytest.mark.parametrize("client_cls", CLIENTS)
async def test_raw_lro(client):
    poller = await client.begin_lro(mode="raw")
    assert await poller.result() == {'provisioningState': 'Succeeded', 'received': 'raw'}

@pytest.mark.asyncio
@pytest.mark.parametrize("client_cls", [DPGClientCustomized])
async def test_customized_lro(client):
    poller = await client.begin_lro(mode="model")
    product = await poller.result()
    assert isinstance(product, LROProduct)
    assert product.received == "model"
    assert product.provisioning_state == "Succeeded"
