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
import io
import pytest
from mediatypes.aio import MediaTypesClient
from mediatypes._rest import *

def test_json_body_no_content_type_kwarg():
    request = build_analyze_body_request(json={"source":"foo"})
    assert request.headers["Content-Type"] == "application/json"
    assert request._internal_request.headers["Content-Type"] == "application/json"
    assert request.content == '{"source": "foo"}'
    assert request._internal_request.body == '{"source": "foo"}'  # internal request is what actually gets passed to the pipelines


def test_json_body_content_type_kwarg():
    request = build_analyze_body_request(json=[{"source":"foo"}], content_type="application/json+cloudevents-batch")
    assert request.headers["Content-Type"] == "application/json+cloudevents-batch"
    assert request._internal_request.headers["Content-Type"] == "application/json+cloudevents-batch"
    assert request.content == '[{"source": "foo"}]'
    assert request._internal_request.body == '[{"source": "foo"}]'

def test_string_body_no_content_type_kwarg():
    request = build_analyze_body_request(content="hello")
    assert request.headers["Content-Type"] == "text/plain"
    assert request._internal_request.headers["Content-Type"] == "text/plain"

def test_string_body_content_type_kwarg():
    request = build_analyze_body_request(content="hello", content_type="text/plain")
    assert request.headers["Content-Type"] == "text/plain"
    assert request._internal_request.headers["Content-Type"] == "text/plain"

def test_io_body_no_content_type_kwarg():
    request = build_analyze_body_request(content=b"PDF")
    assert request.headers["Content-Type"] == "application/octet-stream"
    assert request._internal_request.headers["Content-Type"] == "application/octet-stream"

def test_io_body_content_type_kwarg():
    request = build_analyze_body_request(content=b"PDF", content_type="application/pdf")
    assert request.headers["Content-Type"] == "application/pdf"
    assert request._internal_request.headers["Content-Type"] == "application/pdf"

def test_stream_no_content_type_kwarg():
    test_string = "Upload file test case"
    test_bytes = bytearray(test_string, encoding='utf-8')
    with io.BytesIO(test_bytes) as stream_data:
        request = build_analyze_body_request(content=stream_data)
    assert request.headers["Transfer-Encoding"] == "chunked"
    assert request.headers["Content-Type"] == "application/octet-stream"
    assert request._internal_request.headers["Content-Type"] == "application/octet-stream"

def test_stream_content_type_kwarg():
    test_string = "Upload file test case"
    test_bytes = bytearray(test_string, encoding='utf-8')
    with io.BytesIO(test_bytes) as stream_data:
        request = build_analyze_body_request(content=stream_data, content_type="application/json")
    assert request.headers["Content-Type"] == "application/json"
    assert request._internal_request.headers["Content-Type"] == "application/json"
    assert request.headers["Transfer-Encoding"] == "chunked"

def test_file_description_no_content_type_kwarg():
    with open(__file__) as fd:
        request = build_analyze_body_request(content=fd)
    assert request.headers["Transfer-Encoding"] == "chunked"
    assert request.headers["Content-Type"] == "application/octet-stream"
    assert request._internal_request.headers["Content-Type"] == "application/octet-stream"

def test_file_description_content_type_kwarg():
    with open(__file__) as fd:
        request = build_analyze_body_request(content=fd, content_type="application/pdf")
    assert request.headers["Transfer-Encoding"] == "chunked"
    assert request.headers["Content-Type"] == "application/pdf"
    assert request._internal_request.headers["Content-Type"] == "application/pdf"

def test_content_type_in_headers_no_content_type_kwarg():
    request = build_analyze_body_request(content="", headers={"Content-Type": "application/exotic"})
    assert request.headers["Content-Type"] == "application/exotic"
    assert request._internal_request.headers["Content-Type"] == "application/exotic"

def test_content_type_in_headers_content_type_kwarg():
    request = build_analyze_body_request(content="", headers={"Content-Type": "application/exotic"}, content_type="application/pdf")
    assert request.headers["Content-Type"] == "application/pdf"
    assert request._internal_request.headers["Content-Type"] == "application/pdf"

@pytest.mark.asyncio
async def test_stream_unread_until_send_request():
    class FakeStream:
        def __init__(self):
            self.call_count = 0

        def streaming_body(self, data):
            self.call_count += 1
            yield data

    fake_stream = FakeStream()
    request = build_analyze_body_request(content=fake_stream.streaming_body(b"PDF"))
    assert request.headers["Transfer-Encoding"] == "chunked"
    assert request.headers["Content-Type"] == "application/octet-stream"
    assert request._internal_request.headers["Content-Type"] == "application/octet-stream"
    assert fake_stream.call_count == 0
    await MediaTypesClient()._send_request(request)
    assert fake_stream.call_count == 1
