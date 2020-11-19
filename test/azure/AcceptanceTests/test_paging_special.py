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
from azure.core.paging_method import BasicPagingMethod, DifferentNextOperationPagingMethod
import pytest

@pytest.fixture
def client(credential, authentication_policy):
    with AutoRestSpecialPagingTestService(credential, base_url="http://localhost:3000", authentication_policy=authentication_policy) as client:
        yield client

class TestPaging(object):
    def test_next_link_in_response_headers(self, client):
        class MyPagingMethod(BasicPagingMethod):
            def get_continuation_token(self, pipeline_response, deserialized):
                try:
                    return pipeline_response.http_response.headers['x-ms-nextLink']
                except KeyError:
                    return None

        pages = client.next_link_in_response_headers(paging_method=MyPagingMethod())
        items = [i for i in pages]
        assert len(items) == 10

    def test_continuation_token(self, client):
        class MyPagingMethod(BasicPagingMethod):
            def get_next_request(self, continuation_token, initial_request):
                request = initial_request
                request.headers["x-ms-token"] = continuation_token
                return request

        pages = client.continuation_token(paging_method=MyPagingMethod())
        items = [i for i in pages]
        assert len(items) == 10

    def test_continuation_token_in_response_headers(self, client):
        class MyPagingMethod(BasicPagingMethod):
            def get_continuation_token(self, pipeline_response, deserialized):
                try:
                    return pipeline_response.http_response.headers['x-ms-token']
                except KeyError:
                    return None

            def get_next_request(self, continuation_token, initial_request):
                request = initial_request
                request.headers["x-ms-token"] = continuation_token
                return request

        pages = client.continuation_token_in_response_headers(paging_method=MyPagingMethod())
        items = [i for i in pages]
        assert len(items) == 10

    def test_token_with_metadata(self, client):
        class MyPagingMethod(BasicPagingMethod):
            def __init__(self):
                super(MyPagingMethod, self).__init__()
                self.count = None

            def get_continuation_token(self, pipeline_response, deserialized):
                token = deserialized.token
                if not token:
                    return None
                split_token = token.split(";")
                self.count = split_token[1]
                return split_token[0]

            def get_next_request(self, continuation_token, initial_request):
                request = initial_request
                request.headers["x-ms-token"] = continuation_token
                return request

        pages = client.token_with_metadata(paging_method=MyPagingMethod())
        items = [i for i in pages]
        assert len(items) == 10
        assert pages.get_count() == "10"

    def test_next_link_and_continuation_token(self, client):
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

            def get_next_request(self, continuation_token, initial_request):
                request = super(MyPagingMethod, self).get_next_request(continuation_token, initial_request)
                request.headers["x-ms-token"] = self.token_to_pass_to_headers
                return request

        pages = client.next_link_and_continuation_token(paging_method=MyPagingMethod())
        items = [i for i in pages]
        assert len(items) == 10

    def test_continuation_token_with_separate_next_operation(self, client):
        class MyPagingMethod(DifferentNextOperationPagingMethod):
            def get_next_request(self, continuation_token, initial_request):
                request = self._prepare_next_request()
                request.headers["x-ms-token"] = continuation_token
                return request

        pages = client.continuation_token_initial_operation(paging_method=MyPagingMethod())
        items = [i for i in pages]
        assert len(items) == 10
