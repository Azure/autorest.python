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
from bodybooleanlowlevel import AutoRestBoolTestService
from bodybooleanlowlevel.rest import bool
import pytest
from azure.core.exceptions import DecodeError

@pytest.fixture
def client():
    with AutoRestBoolTestService(base_url="http://localhost:3000") as client:
        yield client

@pytest.fixture
def send_request(client, base_send_request):
    def _send_request(request):
        return base_send_request(client, request)
    return _send_request

@pytest.fixture
def send_request_json_response(client, base_send_request_json_response):
    def _send_request(request):
        return base_send_request_json_response(client, request)
    return _send_request

def test_model_get_true(send_request_json_response):
    request = bool.build_get_true_request()
    assert send_request_json_response(request) == True

def test_model_get_false(send_request_json_response):
    request = bool.build_get_false_request()
    assert not send_request_json_response(request)

def test_model_get_null(send_request):
    request = bool.build_get_null_request()
    assert send_request(request).text == ''

def test_model_put_false(send_request):
    request = bool.build_put_false_request(json=False)  # have to pass in bc we don't do constant bodies in request builders
    send_request(request)

def test_model_put_true(send_request):
    request = bool.build_put_true_request(json=True)  # have to pass in bc we don't do constant bodies in request builders
    send_request(request)

def test_model_get_invalid(send_request):
    request = bool.build_get_invalid_request()
    assert send_request(request).text == "true1"
