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

def test_json_body_no_content_type_kwarg():
    request = preparer(json={})
    assert request.headers["Content-Type"] == "application/json"

def test_json_body_content_type_kwarg():
    request = preparer(json={}, content_type="application/json+cloudevents-batch")
    assert request.headers["Content-Type"] == "application/json+cloudevents-batch"

def test_stream_no_content_type_kwarg():
    request = preparer(content=my_stream)
    assert request.headers["Transfer-Encoding"] = "chunked"
    assert not request.headers["Content-Type"]

def test_stream_content_type_kwarg():
    request = preparer(content=my_stream, content_type="application/json")
    assert request.headers["Content-Type"] = "application/json"
    assert not request.headers["Transfer-Encoding"]