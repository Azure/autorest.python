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

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "Paging"))
sys.path.append(join(tests, "CustomUrlPaging"))

from msrest.serialization import Deserializer
from msrest.authentication import BasicTokenAuthentication

from paging.aio import AutoRestPagingTestService
from paging.models import PagingGetMultiplePagesWithOffsetOptions
from custombaseurlpaging.aio import AutoRestParameterizedHostTestPagingClient

from azure.core.exceptions import HttpResponseError
from azure.core.pipeline.policies import ContentDecodePolicy, AsyncRetryPolicy, HeadersPolicy, RequestIdPolicy

import pytest

@pytest.fixture
async def client(cookie_policy):
    cred = BasicTokenAuthentication({"access_token" :str(uuid4())})
    policies = [
        RequestIdPolicy(),
        HeadersPolicy(),
        ContentDecodePolicy(),
        AsyncRetryPolicy(),
        cookie_policy
    ]
    async with AutoRestPagingTestService(cred, base_url="http://localhost:3000", policies=policies) as client:
        yield client

@pytest.fixture
async def custom_url_client():
    cred = BasicTokenAuthentication({"access_token" :str(uuid4())})
    async with AutoRestParameterizedHostTestPagingClient(cred, host="host:3000") as client:
        yield client

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
    items = [i async for i in pages]
    assert len(items) == 1
    assert items[0].properties.id == 1
    assert items[0].properties.name == "Product"

@pytest.mark.asyncio
async def test_get_multiple_pages(client):
    pages = client.paging.get_multiple_pages()
    items = [i async for i in pages]
    assert len(items) == 10

@pytest.mark.asyncio
async def test_get_odata_multiple_pages(client):
    pages = client.paging.get_odata_multiple_pages()
    items = [i async for i in pages]
    assert len(items) == 10

@pytest.mark.asyncio
async def test_get_multiple_pages_retry_first(client):
    pages = client.paging.get_multiple_pages_retry_first()
    items = [i async for i in pages]
    assert len(items) == 10

@pytest.mark.asyncio
async def test_get_multiple_pages_retry_second(client):
    pages = client.paging.get_multiple_pages_retry_second()
    items = [i async for i in pages]
    assert len(items) == 10

@pytest.mark.asyncio
async def test_get_multiple_pages_with_offset(client):
    options = PagingGetMultiplePagesWithOffsetOptions(offset=100)
    pages = client.paging.get_multiple_pages_with_offset(paging_get_multiple_pages_with_offset_options=options)
    items = [i async for i in pages]
    assert len(items) == 10
    assert items[-1].properties.id == 110


@pytest.mark.asyncio
async def test_get_single_pages_failure(client):
    pages = client.paging.get_single_pages_failure()
    with pytest.raises(HttpResponseError):
        [i async for i in pages]

@pytest.mark.asyncio
async def test_get_multiple_pages_failure(client):
    pages = client.paging.get_multiple_pages_failure()
    with pytest.raises(HttpResponseError):
        [i async for i in pages]

@pytest.mark.asyncio
async def test_get_multiple_pages_failure_uri(client):
    pages = client.paging.get_multiple_pages_failure_uri()
    with pytest.raises(HttpResponseError):
        [i async for i in pages]

@pytest.mark.asyncio
async def test_paging_fragment_path(client):

    pages = client.paging.get_multiple_pages_fragment_next_link("1.6", "test_user")
    items = [i async for i in pages]
    assert len(items) == 10

    with pytest.raises(AttributeError):
        # Be sure this method is not generated (Transform work)
        await client.paging.get_multiple_pages_fragment_next_link_next()  # pylint: disable=E1101

@pytest.mark.asyncio
async def test_custom_url_get_pages_partial_url(custom_url_client):
    pages = custom_url_client.paging.get_pages_partial_url("local")
    paged = [i async for i in pages]

    assert len(paged) == 2
    assert paged[0].properties.id == 1
    assert paged[1].properties.id == 2

@pytest.mark.asyncio
async def test_custom_url_get_pages_partial_url_operation(custom_url_client):
    pages = custom_url_client.paging.get_pages_partial_url_operation("local")
    paged = [i async for i in pages]

    assert len(paged) == 2
    assert paged[0].properties.id == 1
    assert paged[1].properties.id == 2
