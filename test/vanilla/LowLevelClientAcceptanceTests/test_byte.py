﻿# --------------------------------------------------------------------------
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
from bodybyte import AutoRestSwaggerBATByteService
from bodybyte._rest import *

import pytest

@pytest.fixture
def client():
    with AutoRestSwaggerBATByteService(base_url="http://localhost:3000") as client:
        yield client

@pytest.fixture
def make_request(client, base_make_request):
    def _make_request(request):
        return base_make_request(client, request)
    return _make_request

def test_non_ascii(make_request):
    tests = bytearray([0x0FF, 0x0FE, 0x0FD, 0x0FC, 0x0FB, 0x0FA, 0x0F9, 0x0F8, 0x0F7, 0x0F6])
    request = build_byte_put_non_ascii_request(content=tests)
    make_request(request)

    request = build_byte_get_non_ascii_request()
    response = make_request(request)

def test_get_null(make_request):
    request = build_byte_get_null_request()
    assert make_request(request).text == ''

def test_get_empty(make_request):
    request = build_byte_get_empty_request()
    assert b'""' == make_request(request).content  # in convenience layer, we deserialize as bytearray specif

def test_get_invalid(make_request):
    request = build_byte_get_invalid_request()
    assert make_request(request).content == b'"::::SWAGGER::::"'
