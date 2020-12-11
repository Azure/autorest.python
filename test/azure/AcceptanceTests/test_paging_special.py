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

from pagingspecial import AutoRestSpecialPagingTestService
from async_generator import yield_, async_generator
from azure.core.paging import BasicPagingMethod, TokenToHeader, TokenToCallback, TokenToNextLink
import pytest

@pytest.fixture
def client(credential, authentication_policy):
    with AutoRestSpecialPagingTestService(credential, base_url="http://localhost:3000", authentication_policy=authentication_policy) as client:
        yield client

class TestPaging(object):
    def test_next_link_in_response_headers(self, client):
        class MyPagingMethod(BasicPagingMethod):
            def get_continuation_token(self, pipeline_response, deserialized):
                return pipeline_response.http_response.headers.get('x-ms-nextLink', None)

        pages = client.next_link_in_response_headers(paging_method=MyPagingMethod(next_request_algorithm=TokenToNextLink()))
        items = [i for i in pages]
        assert len(items) == 10

    def test_continuation_token(self, client):
        next_request_algorithm = TokenToHeader(header_name="x-ms-token")
        pages = client.continuation_token(paging_method=BasicPagingMethod(next_request_algorithm=next_request_algorithm))
        items = [i for i in pages]
        assert len(items) == 10

    def test_continuation_token_in_response_headers(self, client):
        class MyPagingMethod(BasicPagingMethod):
            def get_continuation_token(self, pipeline_response, deserialized):
                return pipeline_response.http_response.headers.get('x-ms-token', None)

        next_request_algorithm = TokenToHeader(header_name="x-ms-token")
        paging_method = MyPagingMethod(next_request_algorithm=next_request_algorithm)
        pages = client.continuation_token_in_response_headers(paging_method=paging_method)
        items = [i for i in pages]
        assert len(items) == 10

    def test_token_with_metadata(self, client):
        class MyPagingMethod(BasicPagingMethod):
            def __init__(self, next_request_algorithm):
                super(MyPagingMethod, self).__init__(next_request_algorithm)
                self._count = None

            def get_continuation_token(self, pipeline_response, deserialized):
                token = deserialized.token
                if not token:
                    return None
                split_token = token.split(";")
                self._count = int(split_token[1])
                return split_token[0]

        paging_method = MyPagingMethod(next_request_algorithm=TokenToHeader(header_name="x-ms-token"))

        pages = client.token_with_metadata(paging_method=paging_method)
        items = [i for i in pages]
        assert len(items) == 10
        assert pages.get_count() == 10

    def test_next_link_and_continuation_token(self, client):
        class TokenToHeaderAndNextLink(TokenToHeader):
            def get_next_request(self, continuation_token, initial_request):
                split_token = continuation_token.split(",")
                token_to_pass_to_headers = split_token[0]
                request = super(TokenToHeaderAndNextLink, self).get_next_request(token_to_pass_to_headers, initial_request)
                request.url = split_token[1]
                return request

        paging_method = BasicPagingMethod(next_request_algorithm=TokenToHeaderAndNextLink(header_name="x-ms-token"))

        pages = client.next_link_and_continuation_token(paging_method=paging_method)
        items = [i for i in pages]
        assert len(items) == 10

    def test_continuation_token_with_separate_next_operation(self, client):

        def _my_callback(continuation_token):
            generated_request = client._continuation_token_initial_operation_next(continuation_token)
            generated_request.headers['x-ms-token'] = continuation_token
            return generated_request

        next_request_algorithm = TokenToCallback(next_request_callback=_my_callback)
        pages = client.continuation_token_initial_operation(paging_method=BasicPagingMethod(next_request_algorithm=next_request_algorithm))
        items = [i for i in pages]
        assert len(items) == 10
