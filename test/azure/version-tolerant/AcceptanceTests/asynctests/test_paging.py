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

from pagingversiontolerant.aio import AutoRestPagingTestService
from custombaseurlpagingversiontolerant.aio import AutoRestParameterizedHostTestPagingClient

from azure.core.exceptions import HttpResponseError
from azure.core.pipeline.policies import ContentDecodePolicy, AsyncRetryPolicy, HeadersPolicy, RequestIdPolicy

import pytest

@pytest.fixture
@async_generator
async def client(cookie_policy):
    policies = [
        RequestIdPolicy(),
        HeadersPolicy(),
        ContentDecodePolicy(),
        AsyncRetryPolicy(),
        cookie_policy
    ]
    async with AutoRestPagingTestService(endpoint="http://localhost:3000", policies=policies) as client:
        await yield_(client)

@pytest.fixture
@async_generator
async def custom_url_client():
    async with AutoRestParameterizedHostTestPagingClient(host="host:3000") as client:
        await yield_(client)

class TestPaging(object):
    @pytest.mark.asyncio
    async def test_get_no_item_name_pages(self, client):
        pages = client.paging.get_no_item_name_pages()
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 1
        assert items[0]["properties"]["id"] == 1
        assert items[0]["properties"]["name"] == "Product"

    @pytest.mark.asyncio
    async def test_get_null_next_link_name_pages(self, client):
        pages = client.paging.get_null_next_link_name_pages()
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 1
        assert items[0]["properties"]["id"] == 1
        assert items[0]["properties"]["name"] == "Product"

    @pytest.mark.asyncio
    async def test_get_single_pages_with_cb(self, client):
        def cb(list_of_obj):
            for obj in list_of_obj:
                obj["marked"] = True
            return list_of_obj
        async for obj in client.paging.get_single_pages(cls=cb):
            assert obj["marked"]

    @pytest.mark.asyncio
    async def test_get_single_pages(self, client):
        pages = client.paging.get_single_pages()
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 1
        assert items[0]["properties"]["id"] == 1
        assert items[0]["properties"]["name"] == "Product"

    @pytest.mark.asyncio
    async def test_get_multiple_pages(self, client):
        pages = client.paging.get_multiple_pages()
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 10

    @pytest.mark.asyncio
    async def test_query_params(self, client):
        pages = client.paging.get_with_query_params(required_query_parameter='100')
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 2

    @pytest.mark.asyncio
    async def test_get_odata_multiple_pages(self, client):
        pages = client.paging.get_odata_multiple_pages()
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 10

    @pytest.mark.asyncio
    async def test_get_multiple_pages_retry_first(self, client):
        pages = client.paging.get_multiple_pages_retry_first()
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 10

    @pytest.mark.asyncio
    async def test_get_multiple_pages_retry_second(self, client):
        pages = client.paging.get_multiple_pages_retry_second()
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 10

    @pytest.mark.asyncio
    async def test_get_multiple_pages_with_offset(self, client):
        pages = client.paging.get_multiple_pages_with_offset(offset=100)
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 10
        assert items[-1]["properties"]["id"] == 110

    @pytest.mark.asyncio
    async def test_get_single_pages_failure(self, client):
        pages = client.paging.get_single_pages_failure()
        with pytest.raises(HttpResponseError):
            async for i in pages:
                ...

    @pytest.mark.asyncio
    async def test_get_multiple_pages_failure(self, client):
        pages = client.paging.get_multiple_pages_failure()
        with pytest.raises(HttpResponseError):
            async for i in pages:
                ...

    @pytest.mark.asyncio
    async def test_get_multiple_pages_failure_uri(self, client):
        pages = client.paging.get_multiple_pages_failure_uri()
        with pytest.raises(HttpResponseError):
            async for i in pages:
                ...

    @pytest.mark.asyncio
    async def test_paging_fragment_path(self, client):

        pages = client.paging.get_multiple_pages_fragment_next_link(api_version="1.6", tenant="test_user")
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 10

        with pytest.raises(AttributeError):
            # Be sure this method is not generated (Transform work)
            await client.paging.get_multiple_pages_fragment_next_link_next()  # pylint: disable=E1101

    @pytest.mark.asyncio
    async def test_custom_url_get_pages_partial_url(self, custom_url_client):
        pages = custom_url_client.paging.get_pages_partial_url("local")
        items = []
        async for item in pages:
            items.append(item)

        assert len(items) == 2
        assert items[0]["properties"]["id"] == 1
        assert items[1]["properties"]["id"] == 2

    @pytest.mark.asyncio
    async def test_custom_url_get_pages_partial_url_operation(self, custom_url_client):
        pages = custom_url_client.paging.get_pages_partial_url_operation("local")
        items = []
        async for item in pages:
            items.append(item)

        assert len(items) == 2
        assert items[0]["properties"]["id"] == 1
        assert items[1]["properties"]["id"] == 2

    @pytest.mark.asyncio
    async def test_get_multiple_pages_lro(self, client):
        """LRO + Paging at the same time.
        """
        from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling
        poller = await client.paging.begin_get_multiple_pages_lro(polling=AsyncARMPolling(timeout=0))
        pager = await poller.result()
        items = []
        async for item in pager:
            items.append(item)

        assert len(items) == 10
        assert items[0]["properties"]["id"] == 1
        assert items[1]["properties"]["id"] == 2

    @pytest.mark.asyncio
    async def test_initial_response_no_items(self, client):
        pages = client.paging.first_response_empty()
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 1

    @pytest.mark.asyncio
    async def test_item_name_with_xms_client_name(self, client):
        pages = client.paging.get_paging_model_with_item_name_with_xms_client_name()
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 1
