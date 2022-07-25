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
from azure.packagemode.batch.head import HeadClient
from azure.packagemode.batch.paging import PagingClient

class TestMultiClient(object):

    def test_head(self, credential, authentication_policy):

        with HeadClient(credential, authentication_policy=authentication_policy) as client:
            assert client.http_success.head200()
            assert client.http_success.head204()
            assert not client.http_success.head404()

    def test_paging(self, credential, authentication_policy):
        with PagingClient(credential, authentication_policy=authentication_policy) as client:
            pages = client.paging.get_no_item_name_pages()
            items = [i for i in pages]
            assert len(items) == 1
            assert items[0].properties.id == 1
            assert items[0].properties.name == "Product"
