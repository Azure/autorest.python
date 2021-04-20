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

from uuid import uuid4

from msrest.exceptions import (
    ValidationError
)

from azure.core.exceptions import ServiceRequestError

from custombaseurl import AutoRestParameterizedHostTestClient
from custombaseurl._rest import paths

import pytest

@pytest.fixture
def client():
    with AutoRestParameterizedHostTestClient(host="host:3000") as client:
        client._config.retry_policy.retries = 0
        yield client

@pytest.fixture
def make_request(client, base_make_request):
    def _make_request(request):
        return base_make_request(client, request)
    return _make_request

def test_custom_base_uri_positive(make_request):
    request = paths.build_get_empty_request("local")
    make_request(request)

def test_custom_base_uri_get_empty(make_request):
    request = paths.build_get_empty_request("bad")
    make_request(request)

def test_custom_base_uri_get_none(make_request):
    request = paths.build_get_empty_request(None)
    make_request(request)

def test_custom_base_uri_bad_host(make_request):
    client._config.host = "badhost:3000"
    request = paths.build_get_empty_request("local")
    make_request(request)
