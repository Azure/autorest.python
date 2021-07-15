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

from base64 import b64encode
from msrest.exceptions import DeserializationError
from bodybyteversiontolerant import AutoRestSwaggerBATByteService
from .serializer import deserialize_base64, serialize_bytearray, deserialize_bytearray

import pytest

@pytest.fixture
def client():
    with AutoRestSwaggerBATByteService(base_url="http://localhost:3000") as client:
        yield client


def test_non_ascii(client):
    tests = bytearray([0x0FF, 0x0FE, 0x0FD, 0x0FC, 0x0FB, 0x0FA, 0x0F9, 0x0F8, 0x0F7, 0x0F6])
    client.byte.put_non_ascii(serialize_bytearray(tests))
    assert tests == deserialize_bytearray(client.byte.get_non_ascii())

def test_get_null(client):
    assert client.byte.get_null() is None

def test_get_empty(client):
    assert bytearray() == deserialize_base64(client.byte.get_empty())

def test_get_invalid(client):
    assert client.byte.get_invalid() == "::::SWAGGER::::"
