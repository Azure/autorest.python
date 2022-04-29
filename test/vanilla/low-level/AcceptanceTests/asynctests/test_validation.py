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
import sys
 
from azure.core.exceptions import HttpResponseError
from async_generator import yield_, async_generator

from validationlowlevel.aio import AutoRestValidationTest
from validationlowlevel.rest import *

import pytest

@pytest.fixture
@async_generator
async def client():
    async with AutoRestValidationTest(
            "abc123",
        ) as client:
        client.api_version = "12-34-5678"
        await yield_(client)

@pytest.fixture
def send_request(client, base_send_request):
    async def _send_request(request):
        return await base_send_request(client, request)
    return _send_request

@pytest.fixture
def send_request_json_response(client, base_send_request_json_response):
    async def _send_request(request):
        return await base_send_request_json_response(client, request)
    return _send_request

@pytest.fixture
def constant_body():
    """This is NOT considering the constant body, this should work with
    the commented line.
    See https://github.com/Azure/autorest.modelerfour/issues/83
    """
    return {
        'child': {
            'constProperty': 'constant'
        },
        'constChild': {
            'constProperty': 'constant',
            'constProperty2': 'constant2'
        },
        'constInt': 0,
        'constString': 'constant',
        'constStringAsEnum': 'constant_string_as_enum'
    }

@pytest.mark.asyncio
async def test_with_constant_in_path(send_request):
    request = build_get_with_constant_in_path_request()
    await send_request(request)

@pytest.mark.asyncio
async def test_post_with_constant_in_body(send_request_json_response, constant_body):
    request = build_post_with_constant_in_body_request(json=constant_body)
    product = await send_request_json_response(request)
    assert product is not None

# Note: the client-side-validation is not supported for low-level client, 
#       so this request with faked path will be sent to testserver and get an ResourceNotFoundError
@pytest.mark.asyncio
async def test_fakedpath_validation(send_request):
    with pytest.raises(ResourceNotFoundError):
        request = build_validation_of_method_parameters_request(subscription_id="abc123", resource_group_name="1", id=100)
        await send_request(request)
 