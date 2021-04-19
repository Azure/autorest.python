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

from async_generator import yield_, async_generator
import io
from azure.core.exceptions import HttpResponseError
from msrest.exceptions import ValidationError

from requiredoptional.aio import AutoRestRequiredOptionalTestService
from requiredoptional._rest import implicit, explicit
from requiredoptional.models import *

import pytest

@pytest.fixture
@async_generator
async def client_required():
    async with AutoRestRequiredOptionalTestService(
            "required_path",
            "required_query",
            base_url="http://localhost:3000") as client:
        client._config.required_global_path = "required_path"
        client._config.required_global_query = "required_query"
        await yield_(client)


@pytest.fixture
def make_request_required_client(client_required, base_make_request):
    def _make_request(request):
        return base_make_request(client_required, request)
    return _make_request

@pytest.fixture
@async_generator
async def client():
    async with AutoRestRequiredOptionalTestService(
            "required_path",
            "required_query",
            base_url="http://localhost:3000") as client:
        client._config.required_global_path = None
        client._config.required_global_query = None
        await yield_(client)

@pytest.fixture
def make_request_client(client, base_make_request):
    def _make_request(request):
        return base_make_request(client, request)
    return _make_request
# NOTE: in the LLC version, we can't raise as many ValidationErrors as the high level convenience layer does.
# This is because we're not serializing bodies at all, so msrest doesn't have a chance to throw the validation error


# These clients have a required global path and query
@pytest.mark.asyncio
async def test_put_optional(make_request_required_client):
    request = implicit.build_put_optional_query_request(query_parameter=None)
    await make_request_required_client(request)

    request = implicit.build_put_optional_body_request(json=None)
    await make_request_required_client(request)

    request = implicit.build_put_optional_header_request(query_parameter=None)
    await make_request_required_client(request)

@pytest.mark.asyncio
async def test_get_optional_global_query(make_request_required_client):
    request = implicit.build_get_optional_global_query_request(optional_global_query=None)
    await make_request_required_client(request)

@pytest.mark.asyncio
async def test_post_optional_integer(make_request_required_client):
    request = explicit.build_post_optional_integer_parameter_request(json=None)
    await make_request_required_client(request)


    request = explicit.build_post_optional_integer_property_request(json=IntOptionalWrapper(value=None).serialize())
    await make_request_required_client(request)

    request = explicit.build_post_optional_integer_header_request(header_parameter=None)
    await make_request_required_client(request)

@pytest.mark.asyncio
async def test_post_optional_string(make_request_required_client):
    request = explicit.build_post_optional_string_parameter_request(json=None)
    await make_request_required_client(request)


    request = explicit.build_post_optional_string_property_request(json=StringOptionalWrapper(value=None).serialize())
    await make_request_required_client(request)

    request = explicit.build_post_optional_string_header_request(body_parameter=None)
    await make_request_required_client(request)

@pytest.mark.asyncio
async def test_post_optional_class(make_request_required_client):
    request = explicit.build_post_optional_class_parameter_request()
    await make_request_required_client(request)

    request = explicit.build_post_optional_class_property_request(json=ClassOptionalWrapper(value=None).serialize())
    await make_request_required_client(request)

@pytest.mark.asyncio
async def test_post_optional_array(make_request_required_client):
    request = explicit.build_post_optional_array_parameter_request(json=None)
    await make_request_required_client(request)

    request = explicit.build_post_optional_array_property_request(json=ArrayOptionalWrapper(value=None).serialize())
    await make_request_required_client(request)

    request = explicit.build_post_optional_array_header_request(header_parameter=None)
    await make_request_required_client(request)

@pytest.mark.asyncio
async def test_implicit_get_required(make_request_client):
    with pytest.raises(ValidationError):
        request = implicit.build_get_required_path_request(path_parameter=None)
        await make_request_client(request)

    with pytest.raises(ValidationError):
        request = implicit.build_get_required_global_path_request(required_global_path=None)
        await make_request_client(request)

    with pytest.raises(ValidationError):
        request = implicit.build_get_required_global_query_request(required_global_query=None)
        await make_request_client(request)

@pytest.mark.asyncio
async def test_post_required_string(make_request_client):
    with pytest.raises(ValidationError):
        request = explicit.build_post_required_string_header_request(header_parameter=None)
        await make_request_client(request)

    with pytest.raises(HttpResponseError) as ex:
        request = explicit.build_post_required_string_parameter_request()
        await make_request_client(request)

    assert "Not Found" in str(ex.value)

    with pytest.raises(HttpResponseError)as ex:
        request = explicit.build_post_required_string_property_request(json=StringWrapper(value=None).serialize())
        await make_request_client(request)
    assert "Not Found" in str(ex.value)

@pytest.mark.asyncio
async def test_post_required_array(make_request_client):
    with pytest.raises(ValidationError):
        request = explicit.build_post_required_array_header_request(header_parameter=None)
        await make_request_client(request)

    with pytest.raises(HttpResponseError) as ex:
        request = explicit.build_post_required_array_parameter_request()
        await make_request_client(request)
    assert "Not Found" in str(ex.value)

    with pytest.raises(HttpResponseError) as ex:
        request = explicit.build_post_required_array_property_request(json=ArrayWrapper(value=None).serialize())
        await make_request_client(request)
    assert "Not Found" in str(ex.value)

@pytest.mark.asyncio
async def test_post_required_class(make_request_client):
    with pytest.raises(HttpResponseError) as ex:
        request = explicit.build_post_required_class_parameter_request()
        await make_request_client(request)
    assert "Not Found" in str(ex.value)

    with pytest.raises(HttpResponseError) as ex:
        request = explicit.build_post_required_class_property_request(json=ClassWrapper(value=None).serialize())
        await make_request_client(request)
    assert "Not Found" in str(ex.value)

@pytest.mark.asyncio
async def test_explict_put_optional_binary_body(make_request_client):
    request = explicit.build_put_optional_binary_body_request()
    await make_request_client(request)

@pytest.mark.asyncio
async def test_explict_put_required_binary_body(client):
    test_string = "Upload file test case"
    test_bytes = bytearray(test_string, encoding='utf-8')
    with io.BytesIO(test_bytes) as stream_data:
        request = explicit.build_put_required_binary_body_request(content=stream_data)
        await client._send_request(request, stream_response=True)

@pytest.mark.asyncio
async def test_implicit_put_optional_binary_body(make_request_client):
    request = explicit.build_put_optional_binary_body_request()
    await make_request_client(request)
