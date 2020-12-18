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
from pagingspecial.aio import AutoRestSpecialPagingTestService
from azure.core.paging import HeaderPagingMethod, CallbackPagingMethod, NextLinkPagingMethod
import pytest

@pytest.fixture
@async_generator
async def client(credential, authentication_policy):
    async with AutoRestSpecialPagingTestService(credential, base_url="http://localhost:3000", authentication_policy=authentication_policy) as client:
        await yield_(client)


class TestPaging(object):
    @pytest.mark.asyncio
    async def test_next_link_in_response_headers(self, client):
        class MyPagingMethod(NextLinkPagingMethod):
            def get_continuation_token(self, pipeline_response, deserialized, continuation_token_location=None):
                return pipeline_response.http_response.headers.get('x-ms-nextLink', None)

        pages = client.next_link_in_response_headers(paging_method=MyPagingMethod())
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 10

    @pytest.mark.asyncio
    async def test_continuation_token(self, client):
        paging_method = HeaderPagingMethod(header_name="x-ms-token")
        pages = client.continuation_token(paging_method=paging_method)
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 10

    @pytest.mark.asyncio
    async def test_continuation_token_in_response_headers(self, client):
        class MyPagingMethod(HeaderPagingMethod):
            def get_continuation_token(self, pipeline_response, deserialized, client):
                return pipeline_response.http_response.headers.get('x-ms-token', None)

        paging_method = MyPagingMethod(header_name="x-ms-token")
        pages = client.continuation_token_in_response_headers(paging_method=paging_method)
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 10

    @pytest.mark.asyncio
    async def test_token_with_metadata(self, client):
        class MyPagingMethod(HeaderPagingMethod):
            def __init__(self, header_name):
                super(MyPagingMethod, self).__init__(header_name=header_name)
                self._count = None

            def get_continuation_token(self, pipeline_response, deserialized, continuation_token_location=None):
                token = deserialized.token
                if not token:
                    return None
                split_token = token.split(";")
                self._count = int(split_token[1])
                return split_token[0]

        pages = client.token_with_metadata(paging_method=MyPagingMethod(header_name="x-ms-token"))
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 10
        assert pages.get_count() == 10

    @pytest.mark.asyncio
    async def test_next_link_and_continuation_token(self, client):
        class HeaderPagingMethodAndNextLink(NextLinkPagingMethod):
            def __init__(self, header_name):
                super(HeaderPagingMethodAndNextLink, self).__init__()
                self._header_name = header_name

            def get_next_request(self, continuation_token, initial_request, client):
                split_token = continuation_token.split(",")
                token_to_pass_to_headers = split_token[0]
                next_link = split_token[1]
                request = super(HeaderPagingMethodAndNextLink, self).get_next_request(next_link, initial_request, client=client)
                request.headers[self._header_name] = split_token[0]
                return request

        paging_method = HeaderPagingMethodAndNextLink(header_name="x-ms-token")

        pages = client.next_link_and_continuation_token(paging_method=paging_method)
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 10

    @pytest.mark.asyncio
    async def test_continuation_token_with_separate_next_operation(self, client):

        def _my_callback(continuation_token):
            generated_request = client._continuation_token_initial_operation_next(continuation_token)
            generated_request.headers['x-ms-token'] = continuation_token
            return generated_request

        paging_method = CallbackPagingMethod(next_request_callback=_my_callback)
        pages = client.continuation_token_initial_operation(paging_method=paging_method)
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 10
