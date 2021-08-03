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
from mediatypeslowlevel.aio import MediaTypesClient
from mediatypeslowlevel.rest import *
from async_generator import yield_, async_generator

import pytest

@pytest.fixture
@async_generator
async def client():
    async with MediaTypesClient() as client:
        await yield_(client)

@pytest.fixture
def send_request_json_response(client, base_send_request_json_response):
    async def _send_request(request):
        return await base_send_request_json_response(client, request)
    return _send_request

@pytest.mark.asyncio
async def test_pdf(send_request_json_response):
    request = build_analyze_body_request(content=b"PDF", content_type="application/pdf")
    assert await send_request_json_response(request) == "Nice job with PDF"

@pytest.mark.asyncio
async def test_json(send_request_json_response):
    request = build_analyze_body_request(json={"source":"foo"})
    assert await send_request_json_response(request) == "Nice job with JSON"

@pytest.mark.asyncio
async def test_content_type_with_encoding(send_request_json_response):
    request = build_content_type_with_encoding_request(content="hello", content_type='text/plain; encoding=UTF-8')
    assert await send_request_json_response(request) == "Nice job sending content type with encoding"

@pytest.mark.asyncio
async def test_pdf_no_accept_header(send_request):
    request = build_analyze_body_no_accept_header_request(content=b"PDF", content_type="application/pdf")
    await send_request(request)

@pytest.mark.asyncio
async def test_json_no_accept_header(send_request):
    request = build_analyze_body_no_accept_header_request(json={"source":"foo"})
    await send_request(request)