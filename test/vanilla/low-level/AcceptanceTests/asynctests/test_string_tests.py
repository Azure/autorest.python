# coding=utf-8
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

from async_generator import yield_, async_generator
from azure.core.exceptions import HttpResponseError

from bodystringlowlevel.aio import AutoRestSwaggerBATService
from bodystringlowlevel.rest import string, enum
import pytest
from msrest import Serializer, Deserializer
from base64 import b64decode

@pytest.fixture
@async_generator
async def client():
    async with AutoRestSwaggerBATService(base_url="http://localhost:3000") as client:
        await yield_(client)

@pytest.fixture
def send_request(client, base_send_request):
    async def _send_request(request):
        return await base_send_request(client, request)
    return _send_request

@pytest.fixture
def send_request_json_response(client, base_send_request_json_response):
    async def _send_request(request):
        return await base_send_request_json_response(client, request)
    return _send_request

@pytest.mark.asyncio
async def test_null(send_request):
    request = string.build_get_null_request()
    assert (await send_request(request)).text == ''

    request = string.build_put_null_request(content=None)
    await send_request(request)

@pytest.mark.asyncio
async def test_empty(send_request, send_request_json_response):
    request = string.build_get_empty_request()
    assert "" == await send_request_json_response(request)
    # changing this behavior because of this pr being merged: https://github.com/Azure/autorest.testserver/pull/145/files
    request = string.build_put_empty_request()
    await send_request(request)

@pytest.mark.asyncio
async def test_mbcs(send_request, send_request_json_response):
    try:
        test_str = (
            "\xe5\x95\x8a\xe9\xbd\x84\xe4\xb8\x82\xe7\x8b\x9b\xe7\x8b"
            "\x9c\xef\xa7\xb1\xef\xa4\xac\xef\xa7\xb1\xef\xa8\x8c\xef"
            "\xa8\xa9\xcb\x8a\xe3\x80\x9e\xe3\x80\xa1\xef\xbf\xa4\xe2"
            "\x84\xa1\xe3\x88\xb1\xe2\x80\x90\xe3\x83\xbc\xef\xb9\xa1"
            "\xef\xb9\xa2\xef\xb9\xab\xe3\x80\x81\xe3\x80\x93\xe2\x85"
            "\xb0\xe2\x85\xb9\xe2\x92\x88\xe2\x82\xac\xe3\x88\xa0\xe3"
            "\x88\xa9\xe2\x85\xa0\xe2\x85\xab\xef\xbc\x81\xef\xbf\xa3"
            "\xe3\x81\x81\xe3\x82\x93\xe3\x82\xa1\xe3\x83\xb6\xce\x91"
            "\xef\xb8\xb4\xd0\x90\xd0\xaf\xd0\xb0\xd1\x8f\xc4\x81\xc9"
            "\xa1\xe3\x84\x85\xe3\x84\xa9\xe2\x94\x80\xe2\x95\x8b\xef"
            "\xb8\xb5\xef\xb9\x84\xef\xb8\xbb\xef\xb8\xb1\xef\xb8\xb3"
            "\xef\xb8\xb4\xe2\x85\xb0\xe2\x85\xb9\xc9\x91\xee\x9f\x87"
            "\xc9\xa1\xe3\x80\x87\xe3\x80\xbe\xe2\xbf\xbb\xe2\xba\x81"
            "\xee\xa1\x83\xe4\x9c\xa3\xee\xa1\xa4\xe2\x82\xac").decode('utf-8')

    except AttributeError:
        test_str = (
            b"\xe5\x95\x8a\xe9\xbd\x84\xe4\xb8\x82\xe7\x8b\x9b\xe7\x8b"
            b"\x9c\xef\xa7\xb1\xef\xa4\xac\xef\xa7\xb1\xef\xa8\x8c\xef"
            b"\xa8\xa9\xcb\x8a\xe3\x80\x9e\xe3\x80\xa1\xef\xbf\xa4\xe2"
            b"\x84\xa1\xe3\x88\xb1\xe2\x80\x90\xe3\x83\xbc\xef\xb9\xa1"
            b"\xef\xb9\xa2\xef\xb9\xab\xe3\x80\x81\xe3\x80\x93\xe2\x85"
            b"\xb0\xe2\x85\xb9\xe2\x92\x88\xe2\x82\xac\xe3\x88\xa0\xe3"
            b"\x88\xa9\xe2\x85\xa0\xe2\x85\xab\xef\xbc\x81\xef\xbf\xa3"
            b"\xe3\x81\x81\xe3\x82\x93\xe3\x82\xa1\xe3\x83\xb6\xce\x91"
            b"\xef\xb8\xb4\xd0\x90\xd0\xaf\xd0\xb0\xd1\x8f\xc4\x81\xc9"
            b"\xa1\xe3\x84\x85\xe3\x84\xa9\xe2\x94\x80\xe2\x95\x8b\xef"
            b"\xb8\xb5\xef\xb9\x84\xef\xb8\xbb\xef\xb8\xb1\xef\xb8\xb3"
            b"\xef\xb8\xb4\xe2\x85\xb0\xe2\x85\xb9\xc9\x91\xee\x9f\x87"
            b"\xc9\xa1\xe3\x80\x87\xe3\x80\xbe\xe2\xbf\xbb\xe2\xba\x81"
            b"\xee\xa1\x83\xe4\x9c\xa3\xee\xa1\xa4\xe2\x82\xac").decode('utf-8')

    request = string.build_get_mbcs_request()
    assert test_str == await send_request_json_response(request)

    request = string.build_put_mbcs_request()
    await send_request(request)

@pytest.mark.asyncio
async def test_whitespace(send_request, send_request_json_response):
    test_str = "    Now is the time for all good men to come to the aid of their country    "
    request = string.build_get_whitespace_request()
    assert test_str == await send_request_json_response(request)

    request = string.build_put_whitespace_request()
    await send_request(request)

@pytest.mark.asyncio
async def test_get_not_provided(send_request):
    request = string.build_get_not_provided_request()
    assert (await send_request(request)).text == ''

@pytest.mark.asyncio
async def test_enum_not_expandable(send_request, send_request_json_response):
    request = enum.build_get_not_expandable_request()
    assert "red color" == await send_request_json_response(request)

    request = enum.build_put_not_expandable_request(json='red color')
    await send_request(request)

    request = enum.build_put_not_expandable_request(json='red color')
    await send_request(request)
    # Autorest v3 is switching behavior here. Old Autorest would have thrown a serialization error,
    # but now we allow the user to pass strings as enums, so the raised exception is different.

    request = enum.build_put_not_expandable_request(json='not a color')
    with pytest.raises(HttpResponseError):
        await send_request(request)

@pytest.mark.asyncio
async def test_get_base64_encoded(send_request):
    request = string.build_get_base64_encoded_request()
    assert b64decode((await send_request(request)).text) == 'a string that gets encoded with base64'.encode()

@pytest.mark.asyncio
async def test_base64_url_encoded(send_request):
    # the b64 encoding and decoding is taken from msrest
    request = string.build_get_base64_url_encoded_request()
    response = (await send_request(request)).text
    response = Deserializer.deserialize_base64(response)
    assert response == 'a string that gets encoded with base64url'.encode()

    content = Serializer.serialize_base64('a string that gets encoded with base64url'.encode())
    request = string.build_put_base64_url_encoded_request(json=content)
    await send_request(request)

@pytest.mark.asyncio
async def test_get_null_base64_url_encoded(send_request):
    request = string.build_get_null_base64_url_encoded_request()
    assert (await send_request(request)).text == ''

@pytest.mark.asyncio
async def test_enum_referenced(send_request, send_request_json_response):
    request = enum.build_put_referenced_request(json='red color')
    await send_request(request)

    request = enum.build_put_referenced_request(json="red color")
    await send_request(request)

    request = enum.build_get_referenced_request()
    assert await send_request_json_response(request) == 'red color'

@pytest.mark.asyncio
async def test_enum_referenced_constant(send_request, send_request_json_response):
    request = enum.build_put_referenced_request(json='red color')
    await send_request(request)

    request = enum.build_get_referenced_constant_request()
    assert await send_request_json_response(request) == {'field1': 'Sample String'} # there's no constant on the response, so just getting field1
