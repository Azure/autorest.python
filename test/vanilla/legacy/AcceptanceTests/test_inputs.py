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
from bodycomplex import AutoRestComplexTestService
from azure.core.pipeline.policies import CustomHookPolicy
try:
    from urlparse import urlparse  # type: ignore
except ImportError:
    from urllib.parse import urlparse

def get_client(callback):
    return AutoRestComplexTestService(policies=[CustomHookPolicy(raw_request_hook=callback)])

def test_header_input():
    def get_headers(pipeline_request):
        assert len(pipeline_request.http_request.headers) == 2
        assert pipeline_request.http_request.headers["hello"] == "world!"
        assert pipeline_request.http_request.headers["accept"] == "application/json"
        raise ValueError("Passed!")
    client = get_client(callback=get_headers)
    with pytest.raises(ValueError) as ex:
        client.basic.get_empty(headers={"hello": "world!"})
    assert str(ex.value) == "Passed!"

def test_header_input_override():
    def get_headers(pipeline_request):
        assert len(pipeline_request.http_request.headers) == 1
        assert pipeline_request.http_request.headers["Accept"] == "my/content-type"
        raise ValueError("Passed!")
    client = get_client(callback=get_headers)
    with pytest.raises(ValueError) as ex:
        client.basic.get_empty(headers={"Accept": "my/content-type"})
    assert str(ex.value) == "Passed!"

def test_header_none_input():
    with AutoRestComplexTestService() as client:
        client.basic.get_empty(headers=None)

def test_header_case_insensitive():
    def get_headers(pipeline_request):
        assert len(pipeline_request.http_request.headers) == 1
        assert pipeline_request.http_request.headers["Accept"] == "my/content-type"
        raise ValueError("Passed!")

    client = get_client(callback=get_headers)
    accept_keys = ["accept", "Accept", "ACCEPT", "aCCePT"]
    for accept_key in accept_keys:
        with pytest.raises(ValueError) as ex:
            client.basic.get_empty(headers={accept_key: "my/content-type"})
        assert str(ex.value) == "Passed!"

def test_query_input():
    def get_query(pipeline_request):
        assert urlparse(pipeline_request.http_request.url).query == "foo=bar"
        raise ValueError("Passed!")
    client = get_client(callback=get_query)
    with pytest.raises(ValueError) as ex:
        client.basic.get_empty(params={"foo": "bar"})
    assert str(ex.value) == "Passed!"

def test_query_input_override():
    def get_query(pipeline_request):
        assert urlparse(pipeline_request.http_request.url).query == "api-version=2021-10-01"
        raise ValueError("Passed!")

    client = get_client(callback=get_query)
    with pytest.raises(ValueError) as ex:
        # the default value is "2016-02-29"
        client.basic.put_valid({}, params={"api-version": "2021-10-01"})

    assert str(ex.value) == "Passed!"

def test_query_none_input():
    with AutoRestComplexTestService() as client:
        client.basic.get_empty(params=None)

def test_query_case_insensitive():
    def get_query(pipeline_request):
        assert urlparse(pipeline_request.http_request.url).query.lower() == "foo=bar"
        raise ValueError("Passed!")

    client = get_client(callback=get_query)
    query_keys = ["foo", "Foo", "FOO", "fOo"]
    for query_key in query_keys:
        with pytest.raises(ValueError) as ex:
            client.basic.get_empty(params={query_key: "bar"})
        assert str(ex.value) == "Passed!"
