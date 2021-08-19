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
from bodybytelowlevel import AutoRestSwaggerBATByteService
from bodybytelowlevel.rest import byte
from base64 import b64encode, b64decode
import pytest

@pytest.fixture
def client():
    with AutoRestSwaggerBATByteService(endpoint="http://localhost:3000") as client:
        yield client

@pytest.fixture
def send_request(client, base_send_request):
    def _send_request(request):
        return base_send_request(client, request)
    return _send_request

def test_non_ascii(send_request):
    def deserialize_base64(attr):
        padding = '=' * (3 - (len(attr) + 3) % 4)
        attr = attr + padding
        encoded = attr.replace('-', '+').replace('_', '/')
        return b64decode(encoded)
    tests = bytearray([0x0FF, 0x0FE, 0x0FD, 0x0FC, 0x0FB, 0x0FA, 0x0F9, 0x0F8, 0x0F7, 0x0F6])
    request = byte.build_put_non_ascii_request(json=b64encode(tests).decode())
    send_request(request)

    request = byte.build_get_non_ascii_request()
    assert tests == deserialize_base64(send_request(request).text)

def test_get_null(send_request):
    request = byte.build_get_null_request()
    assert send_request(request).text == ''

def test_get_empty(send_request):
    request = byte.build_get_empty_request()
    assert b'""' == send_request(request).content  # in convenience layer, we deserialize as bytearray specif

def test_get_invalid(send_request):
    request = byte.build_get_invalid_request()
    assert send_request(request).content == b'"::::SWAGGER::::"'
