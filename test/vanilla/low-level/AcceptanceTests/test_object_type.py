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

from objecttypelowlevel import ObjectTypeClient
from objecttypelowlevel.rest import build_get_request, build_put_request
from azure.core.exceptions import HttpResponseError

import pytest

@pytest.fixture
def client():
    with ObjectTypeClient(base_url="http://localhost:3000") as client:
        yield client

@pytest.fixture
def make_request(client, base_make_request):
    def _make_request(request):
        return base_make_request(client, request)
    return _make_request

def test_get_object(make_request):
    request = build_get_request()
    assert make_request(request).json() == {"message": "An object was successfully returned"}

def test_put_object_success(make_request):
    request = build_put_request(json={"foo": "bar"})
    assert make_request(request).text == ''

def test_put_object_fail(make_request):
    request = build_put_request(json={"should": "fail"})
    with pytest.raises(HttpResponseError) as ex:
        make_request(request)
    assert ex.value.response.json()['message'] == 'The object you passed was incorrect'