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
from mediatypes._rest import *

def test_json_body_no_content_type_kwarg():
    request = prepare_analyze_body(json={"source":"foo"})
    assert request.headers["Content-Type"] == "application/json"
    assert request.content == '{"source": "foo"}'
    assert request._internal_request.body == '{"source": "foo"}'  # internal request is what actually gets passed to the pipelines


def test_json_body_content_type_kwarg():
    request = prepare_analyze_body(json={"source":"foo"}, content_type="application/json+cloudevents-batch")
    assert request.headers["Content-Type"] == "application/json+cloudevents-batch"
    assert request.content == '{"source": "foo"}'
    assert request._internal_request.body == '{"source": "foo"}'  # internal request is what actually gets passed to the pipelines

def test_string_body_no_content_type_kwarg():
    request = prepare_analyze_body(content="hello")
    assert not request.headers.get("Content-Type")

def test_string_body_content_type_kwarg():
    request = prepare_analyze_body(content="hello", content_type="text/plain")
    assert request.headers["Content-Type"] == "text/plain"

def test_io_body_no_content_type_kwarg():
    request = prepare_analyze_body(content=b"PDF")
    assert not request.headers.get("Content-Type")

def test_io_body_content_type_kwarg():
    request = prepare_analyze_body(content=b"PDF", content_type="bonjour")
    assert request.headers["Content-Type"] == "bonjour"

def test_stream_no_content_type_kwarg():
    test_string = "Upload file test case"
    test_bytes = bytearray(test_string, encoding='utf-8')
    with io.BytesIO(test_bytes) as stream_data:
        request = prepare_analyze_body(content=stream_data)
    assert request.headers["Transfer-Encoding"] == "chunked"
    assert not request.headers.get("Content-Type")

def test_stream_content_type_kwarg():
    test_string = "Upload file test case"
    test_bytes = bytearray(test_string, encoding='utf-8')
    with io.BytesIO(test_bytes) as stream_data:
        request = prepare_analyze_body(content=stream_data, content_type="application/json")
    assert request.headers["Content-Type"] == "application/json"
    assert request.headers["Transfer-Encoding"] == "chunked"