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

from mediatypes.aio import MediaTypesClient
from azure.core.exceptions import HttpResponseError

import pytest
import json

@pytest.fixture
@async_generator
async def client():
    async with MediaTypesClient() as client:
        await yield_(client)


class TestMediaTypes(object):
    @pytest.mark.asyncio
    async def test_pdf(self, client):
        result = await client.analyze_body(input=b"PDF", content_type="application/pdf")
        assert result == "Nice job with PDF"

    @pytest.mark.asyncio
    async def test_json(self, client):
        json_input = json.loads('{"source":"foo"}')
        result = await client.analyze_body(input=json_input)
        assert result == "Nice job with JSON"

    @pytest.mark.asyncio
    async def test_incorrect_content_type(self, client):
        with pytest.raises(ValueError):
            await client.analyze_body(input=b"PDF", content_type="text/plain")

    @pytest.mark.asyncio
    async def test_content_type_with_encoding(self, client):
        result = await client.content_type_with_encoding(input="hello", content_type='text/plain; charset=UTF-8')
        assert result == "Nice job sending content type with encoding"

    @pytest.mark.asyncio
    async def test_pdf_no_accept_header(self, client):
        await client.analyze_body_no_accept_header(input=b"PDF", content_type="application/pdf")

    @pytest.mark.asyncio
    async def test_json_no_accept_header(self, client):
        json_input = json.loads('{"source":"foo"}')
        await client.analyze_body_no_accept_header(input=json_input)

    @pytest.mark.asyncio
    async def test_binary_body_two_content_types(self, client):
        json_input = json.dumps({"hello":"world"})
        await client.binary_body_with_two_content_types(json_input, content_type="application/json")

        content = b"hello, world"
        await client.binary_body_with_two_content_types(content, content_type="application/octet-stream")
