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
from reservedwords import ReservedWordsClient, models

@pytest.fixture
def client():
    with ReservedWordsClient() as client:
        yield client

def test_operation_group_import(client):
    client.import_operations.operation_one(parameter1="foo")

def test_operation_with_content_param(client):
    client.operation_with_content_param(b"hello, world")

def test_operation_with_json_param(client):
    client.operation_with_json_param({"hello": "world"})

def test_operation_with_data_param(client):
    client.operation_with_data_param(data="hello", world="world")

def test_operation_with_files_param(client):
    client.operation_with_files_param(file_name="my.txt", files=b"bytes")

def test_operation_with_url(client):
    client.operation_with_url("foo", header_parameters="x-ms-header", query_parameters=["one", "two"])

def test_operation_with_enum(client):
    client.reserved_enum(models.MyEnum.IMPORT_ENUM)
