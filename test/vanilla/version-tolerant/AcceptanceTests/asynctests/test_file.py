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
import io
from os.path import dirname, pardir, join, realpath

from bodyfileversiontolerant.aio import AutoRestSwaggerBATFileService

import pytest

cwd = dirname(realpath(__file__))


@pytest.fixture
@async_generator
async def client(connection_data_block_size=None):
    async with AutoRestSwaggerBATFileService(
        connection_data_block_size=connection_data_block_size
    ) as client:
        await yield_(client)

@pytest.fixture
def callback():
    def _callback(response, data_stream, headers):
        assert not data_stream._internal_response._released
        return data_stream
    return _callback

@pytest.mark.asyncio
@pytest.mark.parametrize('client', [1000], indirect=True)
async def test_get_file(client):
    file_length = 0
    with io.BytesIO() as file_handle:
        stream = await client.files.get_file()
        assert not stream._internal_response._released

        async for data in stream.iter_bytes():
            assert 0 < len(data) <= stream.block_size
            file_length += len(data)
            file_handle.write(data)

        assert file_length !=  0

        sample_file = realpath(
            join(cwd, pardir, pardir, pardir, pardir, pardir,
                    "node_modules", "@microsoft.azure", "autorest.testserver", "routes", "sample.png"))

        with open(sample_file, 'rb') as data:
            sample_data = hash(data.read())
        assert sample_data ==  hash(file_handle.getvalue())

@pytest.mark.asyncio
@pytest.mark.parametrize('client', [4096], indirect=True)
async def test_get_empty_file(client):
    file_length = 0
    with io.BytesIO() as file_handle:
        stream = await client.files.get_empty_file()
        assert not stream._internal_response._released

        async for data in stream.iter_bytes():
            file_length += len(data)
            file_handle.write(data)

        assert file_length ==  0

@pytest.mark.asyncio
@pytest.mark.parametrize('client', [4096], indirect=True)
async def test_files_long_running(client):
    file_length = 0
    stream = await client.files.get_file_large()
    async for data in stream.iter_raw():
        assert 0 < len(data) <= stream.block_size
        file_length += len(data)

    assert file_length ==  3000 * 1024 * 1024

@pytest.mark.asyncio
@pytest.mark.parametrize('client', [None], indirect=True)
async def test_get_file_with_callback(client, callback):
    file_length = 0
    with io.BytesIO() as file_handle:
        stream = await client.files.get_file(cls=callback)
        async for data in stream.iter_raw():
            assert 0 < len(data) <= stream.block_size
            file_length += len(data)
            file_handle.write(data)

        assert file_length !=  0

        sample_file = realpath(
            join(cwd, pardir, pardir, pardir, pardir, pardir,
                    "node_modules", "@microsoft.azure", "autorest.testserver", "routes", "sample.png"))

        with open(sample_file, 'rb') as data:
            sample_data = hash(data.read())
        assert sample_data ==  hash(file_handle.getvalue())

@pytest.mark.asyncio
@pytest.mark.parametrize('client', [None], indirect=True)
async def test_get_empty_file_with_callback(client, callback):
    file_length = 0
    with io.BytesIO() as file_handle:
        stream = await client.files.get_empty_file(cls=callback)
        async for data in stream.iter_bytes():
            file_length += len(data)
            file_handle.write(data)

        assert stream._internal_response._released
        assert file_length ==  0
