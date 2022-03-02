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
from mediatypes import MediaTypesClient
import json

import pytest
import json
import sys

@pytest.fixture
def client():
    with MediaTypesClient() as client:
        yield client


class TestMediaTypes(object):

    def test_pdf(self, client):
        result = client.analyze_body(input=b"PDF", content_type="application/pdf")
        assert result == "Nice job with PDF"

    def test_json(self, client):
        json_input = json.loads('{"source":"foo"}')
        result = client.analyze_body(input=json_input)
        assert result == "Nice job with JSON"

    def test_incorrect_content_type(self, client):
        with pytest.raises(ValueError):
            client.analyze_body(input=b"PDF", content_type="text/plain")

    def test_content_type_with_encoding(self, client):
        result = client.content_type_with_encoding(input="hello", content_type='text/plain; charset=UTF-8')
        assert result == "Nice job sending content type with encoding"

    def test_pdf_no_accept_header(self, client):
        client.analyze_body_no_accept_header(input=b"PDF", content_type="application/pdf")

    def test_json_no_accept_header(self, client):
        json_input = json.loads('{"source":"foo"}')
        client.analyze_body_no_accept_header(input=json_input)

    def test_binary_body_two_content_types(self, client):
        json_input = json.dumps({"hello":"world"})
        client.binary_body_with_two_content_types(json_input, content_type="application/json")

        content = b"hello, world"
        client.binary_body_with_two_content_types(content, content_type="application/octet-stream")

    def test_binary_body_three_content_types(self, client):
        json_input = json.dumps({"hello":"world"})
        client.binary_body_with_three_content_types(json_input)

        content = b"hello, world"
        client.binary_body_with_three_content_types(content, content_type="application/octet-stream")

        content = "hello, world"
        client.binary_body_with_three_content_types(content, content_type="text/plain")

    def test_models(self):
        from mediatypes.models import SourcePath

        from mediatypes.models._models_py3 import SourcePath as SourcePathPy3
        assert SourcePath == SourcePathPy3

    def test_operation_groups(self):
        from mediatypes.operations import MediaTypesClientOperationsMixin

        with pytest.raises(ImportError):
            from mediatypes.operations import _media_types_client_operations_py3

        from mediatypes.operations._media_types_client_operations import MediaTypesClientOperationsMixin as MediaTypesClientOperationsMixinPy2
        assert MediaTypesClientOperationsMixin == MediaTypesClientOperationsMixinPy2
