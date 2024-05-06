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
from azure.core.pipeline.policies import CustomHookPolicy
from bodyarray import AutoRestSwaggerBATArrayService


def is_rest(obj):
    return hasattr(obj, "content")


def test_raw_request_hook():
    def _callback(request):
        assert not is_rest(request.http_request)
        assert hasattr(request.http_request, "set_multipart_mixed")
        raise ValueError("I entered the callback!")

    raw_request_hook_policy = CustomHookPolicy(raw_request_hook=_callback)
    client = AutoRestSwaggerBATArrayService(policies=[raw_request_hook_policy])
    with pytest.raises(ValueError) as ex:
        client.array.get_array_empty()
    assert "I entered the callback!" in str(ex.value)


def test_raw_response_hook():
    def _callback(response):
        assert not is_rest(response.http_response)
        assert hasattr(response.http_response, "parts")
        raise ValueError("I entered the callback!")

    raw_response_hook_policy = CustomHookPolicy(raw_response_hook=_callback)
    client = AutoRestSwaggerBATArrayService(policies=[raw_response_hook_policy])
    with pytest.raises(ValueError) as ex:
        client.array.get_array_empty()
    assert "I entered the callback!" in str(ex.value)
