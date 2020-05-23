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
import unittest
import subprocess
import sys
import isodate
import tempfile
import json
from uuid import uuid4
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

from paging.aio import AutoRestPagingTestService
from custombaseurlpaging.aio import AutoRestParameterizedHostTestPagingClient

from azure.core.exceptions import HttpResponseError
from azure.core.pipeline.policies import ContentDecodePolicy, AsyncRetryPolicy, HeadersPolicy, RequestIdPolicy

import pytest

@pytest.fixture
@async_generator
async def client(cookie_policy, credential):
    policies = [
        RequestIdPolicy(),
        HeadersPolicy(),
        ContentDecodePolicy(),
        AsyncRetryPolicy(),
        cookie_policy
    ]
    async with AutoRestPagingTestService(credential, base_url="http://localhost:3000", policies=policies) as client:
        await yield_(client)

@pytest.fixture
@async_generator
async def custom_url_client(credential, authentication_policy):
    async with AutoRestParameterizedHostTestPagingClient(credential, host="host:3000", authentication_policy=authentication_policy) as client:
        await yield_(client)

@pytest.mark.asyncio
async def test_get_no_item_name_pages(client):
    pages = client.paging.get_no_item_name_pages()
    items = []
    async for item in pages:
        items.append(item)
    assert len(items) == 1
    assert items[0].properties.id == 1
    assert items[0].properties.name == "Product"

@pytest.mark.asyncio
async def test_get_null_next_link_name_pages(client):
    pages = client.paging.get_null_next_link_name_pages()
    items = []
    async for item in pages:
        items.append(item)
    assert len(items) == 1
    assert items[0].properties.id == 1
    assert items[0].properties.name == "Product"

@pytest.mark.asyncio
async def test_get_single_pages_with_cb(client):
    def cb(list_of_obj):
        for obj in list_of_obj:
            obj.marked = True
        return list_of_obj
    async for obj in client.paging.get_single_pages(cls=cb):
        assert obj.marked

@pytest.mark.asyncio
async def test_get_single_pages(client):
    pages = client.paging.get_single_pages()
    items = []
    async for item in pages:
        items.append(item)
    assert len(items) == 1
    assert items[0].properties.id == 1
    assert items[0].properties.name == "Product"

@pytest.mark.asyncio
async def test_get_multiple_pages(client):
    pages = client.paging.get_multiple_pages()
    items = []
    async for item in pages:
        items.append(item)
    assert len(items) == 10

@pytest.mark.asyncio
async def test_query_params(client):
    pages = client.paging.get_with_query_params(required_query_parameter='100')
    items = []
    async for item in pages:
        items.append(item)
    assert len(items) == 2

@pytest.mark.asyncio
async def test_get_odata_multiple_pages(client):
    pages = client.paging.get_odata_multiple_pages()
    items = []
    async for item in pages:
        items.append(item)
    assert len(items) == 10

@pytest.mark.asyncio
async def test_get_multiple_pages_retry_first(client):
    pages = client.paging.get_multiple_pages_retry_first()
    items = []
    async for item in pages:
        items.append(item)
    assert len(items) == 10

@pytest.mark.asyncio
async def test_get_multiple_pages_retry_second(client):
    pages = client.paging.get_multiple_pages_retry_second()
    items = []
    async for item in pages:
        items.append(item)
    assert len(items) == 10

@pytest.mark.asyncio
async def test_get_multiple_pages_with_offset(client):
    from paging.models import PagingGetMultiplePagesWithOffsetOptions
    options = PagingGetMultiplePagesWithOffsetOptions(offset=100)
    pages = client.paging.get_multiple_pages_with_offset(paging_get_multiple_pages_with_offset_options=options)
    items = []
    async for item in pages:
        items.append(item)
    assert len(items) == 10
    assert items[-1].properties.id == 110

@pytest.mark.asyncio
async def test_get_single_pages_failure(client):
    pages = client.paging.get_single_pages_failure()
    with pytest.raises(HttpResponseError):
        async for i in pages:
            ...

@pytest.mark.asyncio
async def test_get_multiple_pages_failure(client):
    pages = client.paging.get_multiple_pages_failure()
    with pytest.raises(HttpResponseError):
        async for i in pages:
            ...

@pytest.mark.asyncio
async def test_get_multiple_pages_failure_uri(client):
    pages = client.paging.get_multiple_pages_failure_uri()
    with pytest.raises(HttpResponseError):
        async for i in pages:
            ...

@pytest.mark.asyncio
async def test_paging_fragment_path(client):

    pages = client.paging.get_multiple_pages_fragment_next_link("1.6", "test_user")
    items = []
    async for item in pages:
        items.append(item)
    assert len(items) == 10

    with pytest.raises(AttributeError):
        # Be sure this method is not generated (Transform work)
        await client.paging.get_multiple_pages_fragment_next_link_next()  # pylint: disable=E1101

@pytest.mark.asyncio
async def test_custom_url_get_pages_partial_url(custom_url_client):
    pages = custom_url_client.paging.get_pages_partial_url("local")
    items = []
    async for item in pages:
        items.append(item)

    assert len(items) == 2
    assert items[0].properties.id == 1
    assert items[1].properties.id == 2

@pytest.mark.asyncio
async def test_custom_url_get_pages_partial_url_operation(custom_url_client):
    pages = custom_url_client.paging.get_pages_partial_url_operation("local")
    items = []
    async for item in pages:
        items.append(item)

    assert len(items) == 2
    assert items[0].properties.id == 1
    assert items[1].properties.id == 2

@pytest.mark.asyncio
async def test_get_multiple_pages_lro(client):
    """LRO + Paging at the same time.

    Python decides to poll, but not follow paging. Check that at least you get read the first page.
    """
    from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling
    polling = AsyncARMPolling(0, lro_options={'final-state-via': 'location'})
    # FIXME Location should be the default once 1.0.0b2 is out

    poller = await client.paging.begin_get_multiple_pages_lro(polling=polling)
    page1 = await poller.result()
    assert len(page1.values) == 1
    assert page1.values[0].properties.id == 1
    assert page1.next_link.endswith("paging/multiple/page/2")
