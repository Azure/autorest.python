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
import sys
import pytest
from mediatypeslowlevel import MediaTypesClient
from mediatypeslowlevel.rest import *

def test_json_body_no_content_type_kwarg():
    request = build_analyze_body_request(json={"source":"foo"})
    assert request.headers["Content-Type"] == "application/json"
    assert request.content == '{"source": "foo"}'


def test_json_body_content_type_kwarg():
    request = build_analyze_body_request(json=[{"source":"foo"}], content_type="application/json+cloudevents-batch")
    assert request.headers["Content-Type"] == "application/json+cloudevents-batch"
    assert request.content == '[{"source": "foo"}]'

def test_string_body_no_content_type_kwarg():
    request = build_analyze_body_request(content="hello")
    assert request.headers["Content-Type"] == "text/plain"

def test_string_body_content_type_kwarg():
    request = build_analyze_body_request(content="hello", content_type="text/plain")
    assert request.headers["Content-Type"] == "text/plain"

def test_io_body_no_content_type_kwarg():
    request = build_analyze_body_request(content=b"PDF")
    assert not request.headers.get("Content-Type")

def test_io_body_content_type_kwarg():
    request = build_analyze_body_request(content=b"PDF", content_type="application/pdf")
    assert request.headers["Content-Type"] == "application/pdf"

def test_stream_no_content_type_kwarg():
    test_string = "Upload file test case"
    test_bytes = bytearray(test_string, encoding='utf-8')
    with io.BytesIO(test_bytes) as stream_data:
        request = build_analyze_body_request(content=stream_data)
    assert not request.headers.get("Content-Type")

def test_stream_content_type_kwarg():
    test_string = "Upload file test case"
    test_bytes = bytearray(test_string, encoding='utf-8')
    with io.BytesIO(test_bytes) as stream_data:
        request = build_analyze_body_request(content=stream_data, content_type="application/json")
    assert request.headers["Content-Type"] == "application/json"

def test_file_description_no_content_type_kwarg():
    with open(__file__) as fd:
        request = build_analyze_body_request(content=fd)
    assert not request.headers.get("Content-Type")

def test_file_description_content_type_kwarg():
    with open(__file__) as fd:
        request = build_analyze_body_request(content=fd, content_type="application/pdf")
    assert request.headers["Content-Type"] == "application/pdf"

def test_content_type_in_headers_no_content_type_kwarg():
    request = build_analyze_body_request(content="", headers={"Content-Type": "application/exotic"})
    assert request.headers["Content-Type"] == "application/exotic"

def test_content_type_in_headers_content_type_kwarg():
    request = build_analyze_body_request(content="", headers={"Content-Type": "application/exotic"}, content_type="application/pdf")
    assert request.headers["Content-Type"] == "application/pdf"

def test_stream_unread_until_send_request():
    class FakeStream:
        def __init__(self):
            self.call_count = 0

        def streaming_body(self, data):
            self.call_count += 1
            yield data

    fake_stream = FakeStream()
    request = build_analyze_body_request(content=fake_stream.streaming_body(b"PDF"))
    assert not request.headers.get("Content-Type")
    assert fake_stream.call_count == 0
    MediaTypesClient().send_request(request)
    assert fake_stream.call_count == 1
