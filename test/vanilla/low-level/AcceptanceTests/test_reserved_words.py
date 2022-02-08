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
from reservedwordslowlevel import ReservedWordsClient
from reservedwordslowlevel.rest import import_builders
from reservedwordslowlevel.rest import (
    build_operation_with_content_param_request,
    build_operation_with_data_param_request,
    build_operation_with_files_param_request,
    build_operation_with_json_param_request,
    build_operation_with_url_request,
)

@pytest.fixture
def client():
    with ReservedWordsClient() as client:
        yield client

@pytest.fixture
def send_request(client, base_send_request):
    def _send_request(request):
        return base_send_request(client, request)
    return _send_request

def test_operation_group_import(send_request):
    request = import_builders.build_operation_one_request(parameter1="foo")
    send_request(request)

def test_operation_with_content_param(send_request):
    request = build_operation_with_content_param_request(content=b"hello, world", headers={"Content-Type": "application/octet-stream"})
    send_request(request)

def test_operation_with_json_param(send_request):
    request = build_operation_with_json_param_request(json={"hello": "world"})
    send_request(request)

def test_operation_with_data_param(send_request):
    request = build_operation_with_data_param_request(data={"data": "hello", "world": "world"})
    send_request(request)

def test_operation_with_files_param(send_request):
    request = build_operation_with_files_param_request(files={
        "file_name": "my.txt",
        "files": b'bytes'
    })
    send_request(request)

def test_operation_with_url(send_request):
    request = build_operation_with_url_request("foo", header_parameters="x-ms-header", query_parameters=["one", "two"])
    send_request(request)
