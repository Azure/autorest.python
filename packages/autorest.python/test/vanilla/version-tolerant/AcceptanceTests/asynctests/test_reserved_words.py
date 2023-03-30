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
import pytest
from reservedwordsversiontolerant.aio import ReservedWordsClient

@pytest.fixture
async def client():
    async with ReservedWordsClient() as client:
        yield client

@pytest.mark.asyncio
async def test_operation_group_import(client):
    await client.import_operations.operation_one(parameter1="foo")

@pytest.mark.asyncio
async def test_operation_with_content_param(client):
    await client.operation_with_content_param(b"hello, world")

@pytest.mark.asyncio
async def test_operation_with_json_param(client):
    await client.operation_with_json_param({"hello": "world"})

@pytest.mark.asyncio
async def test_operation_with_data_param(client):
    await client.operation_with_data_param({"data": "hello", "world": "world"})

@pytest.mark.asyncio
async def test_operation_with_files_param(client):
    await client.operation_with_files_param(files = {
        "file_name": "my.txt",
        "files": b'bytes'
    })

@pytest.mark.asyncio
async def test_operation_with_url(client):
    await client.operation_with_url("foo", header_parameters="x-ms-header", query_parameters=["one", "two"])

@pytest.mark.asyncio
async def test_operation_with_enum(client: ReservedWordsClient):
    await client.reserved_enum(enum_parameter="import")
