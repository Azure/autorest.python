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
from azure.core.exceptions import HttpResponseError

import pytest
import json

@pytest.fixture
def client():
    with MediaTypesClient() as client:
        yield client


class TestMediaTypes(object):

    def test_pdf(self, client):
        result = client.analyze_body(input=b"PDF", content_type="application/pdf")
        assert result == "Nice job with PDF"

    def test_json_pass(self, client):
        json_input = json.loads('{"source":"foo"}')
        result = client.analyze_body(input=json_input)
        assert result == "Nice job with JSON"

    def test_json_fail(self, client):
        json_input=json.loads('{"wrong":true}')
        with pytest.raises(HttpResponseError) as excinfo:
            result = client.analyze_body(input=json_input)
        assert "Did not received what I was expecting" in str(excinfo)
