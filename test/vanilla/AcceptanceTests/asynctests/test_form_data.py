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
import subprocess
import sys
import io
import isodate
import os
import tempfile
from os.path import dirname, pardir, join, realpath

from msrest.exceptions import DeserializationError

from bodyformdata.aio import AutoRestSwaggerBATFormDataService

import pytest

@pytest.fixture
@async_generator
def dummy_file():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as dummy:
        dummy.write("Test file")
    # Get outside of the "with", so file can be re-opened on Windows
    await yield_(dummy.name)
    os.remove(dummy.name)

@pytest.fixture
@async_generator
async def client():
    async with AutoRestSwaggerBATFormDataService(
        base_url="http://localhost:3000",
        connection_data_block_size = 2,
        retry_total = 50,  # Be agressive on this test, sometimes testserver DDOS :-p
        retry_backoff_factor = 1.6
    ) as client:
        await yield_(client)


class TestFormData(object):

    @pytest.mark.asyncio
    async def test_file_upload_stream(self, client):
        test_string = "Upload file test case"
        test_bytes = bytearray(test_string, encoding='utf-8')
        result = io.BytesIO()
        with io.BytesIO(test_bytes) as stream_data:
            resp = await client.formdata.upload_file(stream_data, "UploadFile.txt")
            async for r in resp:
                result.write(r)
            assert result.getvalue().decode() ==  test_string

    @pytest.mark.asyncio
    async def test_file_upload_stream_raw(self, client):
        def test_callback(response, data, headers):
            return data

        test_string = "Upload file test case"
        test_bytes = bytearray(test_string, encoding='utf-8')
        result = io.BytesIO()
        with io.BytesIO(test_bytes) as stream_data:
            resp = await client.formdata.upload_file(stream_data, "UploadFile.txt", cls=test_callback)
            async for data in resp:
                result.write(data)
            assert result.getvalue().decode() ==  test_string

    @pytest.mark.asyncio
    async def test_file_upload_file_stream(self, client, dummy_file):
        name = os.path.basename(dummy_file)
        result = io.BytesIO()
        with open(dummy_file, 'rb') as upload_data:
            resp = await client.formdata.upload_file(upload_data, name)
            async for r in resp:
                result.write(r)
            assert result.getvalue().decode() ==  "Test file"

    @pytest.mark.asyncio
    async def test_file_upload_file_stream_raw(self, client, dummy_file):

        def test_callback(response, data, headers):
            return data

        name = os.path.basename(dummy_file)
        result = io.BytesIO()
        with open(dummy_file, 'rb') as upload_data:
            resp = await client.formdata.upload_file(upload_data, name, cls=test_callback)
            async for data in resp:
                result.write(data)
            assert result.getvalue().decode() ==  "Test file"

    @pytest.mark.asyncio
    async def test_file_body_upload(self, client, dummy_file):
        test_string = "Upload file test case"
        test_bytes = bytearray(test_string, encoding='utf-8')

        result = io.BytesIO()
        with io.BytesIO(test_bytes) as stream_data:
            resp = await client.formdata.upload_file_via_body(stream_data)
            async for r in resp:
                result.write(r)
            assert result.getvalue().decode() ==  test_string

        result = io.BytesIO()
        with open(dummy_file, 'rb') as upload_data:
            resp = await client.formdata.upload_file_via_body(upload_data)
            async for r in resp:
                result.write(r)
            assert result.getvalue().decode() ==  "Test file"

    @pytest.mark.asyncio
    async def test_file_body_upload_generator(self, client, dummy_file):
        test_string = "Upload file test case"
        test_bytes = bytearray(test_string, encoding='utf-8')

        async def stream_upload(data, length, block_size):
            progress = 0
            while True:
                block = data.read(block_size)
                progress += len(block)
                print("Progress... {}%".format(int(progress*100/length)))
                if not block:
                    break
                yield block

        result = io.BytesIO()
        with io.BytesIO(test_bytes) as stream_data:
            streamed_upload = stream_upload(stream_data, len(test_string), 2)
            resp = await client.formdata.upload_file_via_body(streamed_upload)
            async for r in resp:
                result.write(r)
            assert result.getvalue().decode() ==  test_string

        result = io.BytesIO()
        with open(dummy_file, 'rb') as upload_data:
            streamed_upload = stream_upload(upload_data, len("Test file"), 2)
            response = await client.formdata.upload_file_via_body(streamed_upload)
            async for data in response:
                result.write(data)
            assert result.getvalue().decode() == "Test file"