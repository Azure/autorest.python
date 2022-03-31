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
from mediatypesversiontolerant import MediaTypesClient

import pytest
import json

@pytest.fixture
def client():
    with MediaTypesClient() as client:
        yield client

def test_pdf(client):
    result = client.analyze_body(input=b"PDF", content_type="application/pdf")
    assert result == "Nice job with PDF"

def test_json(client):
    json_input = json.loads('{"source":"foo"}')
    result = client.analyze_body(input=json_input)
    assert result == "Nice job with JSON"

def test_content_type_with_encoding(client):
    result = client.content_type_with_encoding(input="hello", content_type='text/plain; charset=UTF-8')
    assert result == "Nice job sending content type with encoding"

def test_pdf_no_accept_header(client):
    client.analyze_body_no_accept_header(input=b"PDF", content_type="application/pdf")

def test_json_no_accept_header(client):
    json_input = json.loads('{"source":"foo"}')
    client.analyze_body_no_accept_header(input=json_input)

def test_binary_body_two_content_types(client):
    json_input = {"hello":"world"}
    client.binary_body_with_two_content_types(json_input, content_type="application/json")

    content = b"hello, world"
    client.binary_body_with_two_content_types(content, content_type="application/octet-stream")

def test_binary_body_three_content_types(client):
    json_input = {"hello":"world"}
    client.binary_body_with_three_content_types(json_input)

    content = b"hello, world"
    client.binary_body_with_three_content_types(content, content_type="application/octet-stream")

    content = "hello, world"
    client.binary_body_with_three_content_types(content, content_type="text/plain")
