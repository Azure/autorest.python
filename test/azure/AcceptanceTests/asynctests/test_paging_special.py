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
from azure.core.paging import BasicPagingMethod
import pytest

@pytest.fixture
@async_generator
async def client(credential, authentication_policy):
    async with AutoRestSpecialPagingTestService(credential, base_url="http://localhost:3000", authentication_policy=authentication_policy) as client:
        await yield_(client)


class TestPaging(object):
    @pytest.mark.asyncio
    async def test_next_link_in_response_headers(self, client):
        class MyPagingMethod(BasicPagingMethod):
            def get_continuation_token(self, pipeline_response, deserialized):
                return pipeline_response.http_response.headers.get('x-ms-nextLink', None)

        pages = client.next_link_in_response_headers(paging_method=MyPagingMethod())
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 10

    @pytest.mark.asyncio
    async def test_continuation_token(self, client):
        class MyPagingMethod(BasicPagingMethod):
            def mutate_next_request(self, continuation_token, next_request, initial_request):
                initial_request.headers["x-ms-token"] = continuation_token
                return initial_request

        pages = client.continuation_token(paging_method=MyPagingMethod())
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 10

    @pytest.mark.asyncio
    async def test_continuation_token_in_response_headers(self, client):
        class MyPagingMethod(BasicPagingMethod):
            def get_continuation_token(self, pipeline_response, deserialized):
                return pipeline_response.http_response.headers.get('x-ms-token', None)

            def mutate_next_request(self, continuation_token, next_request, initial_request):
                initial_request.headers["x-ms-token"] = continuation_token
                return initial_request

        pages = client.continuation_token_in_response_headers(paging_method=MyPagingMethod())
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 10

    @pytest.mark.asyncio
    async def test_token_with_metadata(self, client):
        class MyPagingMethod(BasicPagingMethod):
            def __init__(self):
                super(MyPagingMethod, self).__init__()
                self._count = None

            def get_continuation_token(self, pipeline_response, deserialized):
                token = deserialized.token
                if not token:
                    return None
                split_token = token.split(";")
                self._count = int(split_token[1])
                return split_token[0]

            def mutate_next_request(self, continuation_token, next_request, initial_request):
                initial_request.headers["x-ms-token"] = continuation_token
                return initial_request

        pages = client.token_with_metadata(paging_method=MyPagingMethod())
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 10
        assert pages.get_count() == 10

    @pytest.mark.asyncio
    async def test_next_link_and_continuation_token(self, client):
        class MyPagingMethod(BasicPagingMethod):
            def __init__(self):
                super(MyPagingMethod, self).__init__()
                self.token_to_pass_to_headers = None

            def get_continuation_token(self, pipeline_response, deserialized):
                token = deserialized.token
                if not token:
                    return None
                split_token = token.split(",")
                self.token_to_pass_to_headers = split_token[0]
                return split_token[1]

            def mutate_next_request(self, continuation_token, next_request, initial_request):
                next_request.headers["x-ms-token"] = self.token_to_pass_to_headers
                return next_request

        pages = client.next_link_and_continuation_token(paging_method=MyPagingMethod())
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 10

    @pytest.mark.asyncio
    async def test_continuation_token_with_separate_next_operation(self, client):
        class MyPagingMethod(BasicPagingMethod):
            def mutate_next_request(self, continuation_token, next_request, initial_request):
                next_request.headers["x-ms-token"] = continuation_token
                return next_request

        pages = client.continuation_token_initial_operation(paging_method=MyPagingMethod())
        items = []
        async for item in pages:
            items.append(item)
        assert len(items) == 10
