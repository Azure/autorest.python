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
from custompollerpager import AutoRestPagingTestService
from customdefinitions import CustomPager, CustomPoller

import pytest

@pytest.fixture
def client(credential, authentication_policy):
    with AutoRestPagingTestService(credential, base_url="http://localhost:3000", authentication_policy=authentication_policy) as client:
        yield client


@pytest.fixture
def custom_url_client(credential, authentication_policy):
    with AutoRestParameterizedHostTestPagingClient(credential, host="host:3000", authentication_policy=authentication_policy) as client:
        yield client

class TestPaging(object):
    def test_custom_pager(self, client):
        pager = client.paging.get_single_pages()
        assert isinstance(pager, CustomPager)

    def test_custom_poller(self, client):
        poller = client.paging.begin_get_multiple_pages_lro()
        assert isinstance(poller, CustomPoller)