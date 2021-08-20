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

from headlowlevel import AutoRestHeadTestService
from headlowlevel.rest import http_success
from headexceptionslowlevel import AutoRestHeadExceptionTestService
from headexceptionslowlevel.rest import head_exception
from azure.core.exceptions import HttpResponseError

import pytest

def test_head(credential, authentication_policy):
    with AutoRestHeadTestService(credential, authentication_policy=authentication_policy) as client:
        request = http_success.build_head200_request()
        response = client.send_request(request)
        response.raise_for_status()

        request = http_success.build_head204_request()
        response = client.send_request(request)
        response.raise_for_status()

        request = http_success.build_head404_request()
        response = client.send_request(request)
        with pytest.raises(HttpResponseError):
            response.raise_for_status()

def test_head_exception(credential, authentication_policy):
    with AutoRestHeadExceptionTestService(credential, authentication_policy=authentication_policy) as client:
        request = head_exception.build_head200_request()
        response = client.send_request(request)
        response.raise_for_status()

        request = head_exception.build_head204_request()
        response = client.send_request(request)
        response.raise_for_status()

        request = head_exception.build_head404_request()
        response = client.send_request(request)
        with pytest.raises(HttpResponseError):
            response.raise_for_status()
