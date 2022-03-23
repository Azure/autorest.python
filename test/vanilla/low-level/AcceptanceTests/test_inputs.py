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
from bodycomplexlowlevel.rest import basic
try:
    from urlparse import urlparse  # type: ignore
except ImportError:
    from urllib.parse import urlparse

def test_header_input():
    request = basic.build_get_empty_request(headers={"hello": "world!"})
    assert len(request.headers) == 2
    assert request.headers["Accept"] == "application/json"
    assert request.headers["hello"] == "world!"

def test_header_input_override():
    request = basic.build_get_empty_request(headers={"Accept": "my/content-type"})
    assert request.headers == {"Accept": "my/content-type"}

def test_header_none_input():
    # just check we can build a request with empty headers
    basic.build_get_empty_request(headers=None)

def test_header_case_insensitive():
    accept_keys = ["accept", "Accept", "ACCEPT", "aCCePT"]
    for accept_key in accept_keys:
        request = basic.build_get_empty_request(headers={accept_key: "my/content-type"})
        assert request.headers == {"Accept": "my/content-type"}

def test_header_kwarg_and_header():
    request = basic.build_put_valid_request(json=None, headers={"content-type": "shouldn't/be-me"}, content_type="my/json")
    assert len(request.headers) == 2
    assert request.headers["content-type"] == "my/json"
    assert request.headers["accept"] == "application/json"

def test_query_input():
    request = basic.build_get_empty_request(params={"foo": "bar"})
    assert urlparse(request.url).query == "foo=bar"

def test_query_input_override():
    request = basic.build_put_valid_request(params={"api-version": "2021-10-01"})

    assert urlparse(request.url).query == "api-version=2021-10-01"

def test_query_none_input():
    # just check we can build a request with empty params
    basic.build_get_empty_request(params=None)

def test_query_case_insensitive():
    query_keys = ["foo", "Foo", "FOO", "fOo"]
    for query_key in query_keys:
        request = basic.build_get_empty_request(params={query_key: "bar"})
        assert urlparse(request.url).query.lower() == "foo=bar"

def test_query_kwarg_and_header():
    request = basic.build_put_valid_request(params={"api-version": "shouldn't-be-me"}, api_version="2021-10-01")
    assert urlparse(request.url).query == "api-version=2021-10-01"
