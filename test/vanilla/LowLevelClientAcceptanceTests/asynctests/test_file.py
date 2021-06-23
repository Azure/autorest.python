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
from os.path import dirname, pardir, join, realpath
import io
from bodyfile.aio import AutoRestSwaggerBATFileService
from bodyfile.rest.files import *

import pytest

cwd = dirname(realpath(__file__))


@pytest.fixture
@async_generator
async def client(connection_data_block_size=None):
    async with AutoRestSwaggerBATFileService(
        base_url="http://localhost:3000", connection_data_block_size=connection_data_block_size
    ) as client:
        await yield_(client)


@pytest.mark.asyncio
@pytest.mark.parametrize('client', [1000], indirect=True)
async def test_get_file(client):
    file_length = 0
    with io.BytesIO() as file_handle:
        request = build_get_file_request()
        async with client.send_request(request, stream=True) as response:
            assert not response._internal_response.internal_response._content_consumed
            assert not response.is_closed
            assert not response.is_stream_consumed
            async for data in response.iter_raw():
                # assert 0 < len(data) <= stream.block_size
                file_length += len(data)
                file_handle.write(data)

        assert file_length !=  0
        assert response.is_closed
        assert response.is_stream_consumed
        assert response._internal_response.internal_response._content_consumed
        sample_file = realpath(
        join(cwd, pardir, pardir, pardir,
            "node_modules", "@microsoft.azure", "autorest.testserver", "routes", "sample.png"))

        with open(sample_file, 'rb') as data:
            sample_data = hash(data.read())
        assert sample_data ==  hash(file_handle.getvalue())

@pytest.mark.asyncio
@pytest.mark.parametrize('client', [4096], indirect=True)
async def test_get_empty_file(client):
    file_length = 0
    with io.BytesIO() as file_handle:
        request = build_get_empty_file_request()
        async with client.send_request(request, stream=True) as response:
            assert not response._internal_response.internal_response._content_consumed

            async for data in response.iter_raw():
                file_length += len(data)
                file_handle.write(data)

        assert file_length ==  0

@pytest.mark.asyncio
@pytest.mark.parametrize('client', [4096], indirect=True)
async def test_files_long_running(client):
    file_length = 0
    request = build_get_file_large_request()
    async with client.send_request(request, stream=True) as response:
        chunk_size = 4095  # make less than connection data block size to make sure chunk size is working
        async for data in response.iter_bytes(chunk_size=chunk_size):
            assert 0 < len(data) <= chunk_size
            file_length += len(data)

    assert file_length ==  3000 * 1024 * 1024
