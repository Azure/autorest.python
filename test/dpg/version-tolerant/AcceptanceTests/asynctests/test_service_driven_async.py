
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
import json
from azure.core.rest import HttpRequest
from dpgservicedriveninitialversiontolerant.aio import DPGClient as DPGClientInitial
from dpgservicedrivenupdateoneversiontolerant.aio import DPGClient as DPGClientUpdateOne

@pytest.fixture
async def initial_client():
    async with DPGClientInitial() as client:
        yield client

@pytest.fixture
async def update_one_client():
    async with DPGClientUpdateOne() as client:
        yield client

@pytest.mark.asyncio
async def test_add_optional_parameter_to_required(initial_client, update_one_client):
    await initial_client.params.get_required(
        parameter="foo"
    )
    await update_one_client.params.get_required(
        parameter="foo",
        new_parameter="bar",
    )

@pytest.mark.asyncio
async def test_add_optional_parameter_to_none(initial_client, update_one_client):
    await initial_client.params.head_no_params()
    await update_one_client.params.head_no_params()
    await update_one_client.params.head_no_params(
        new_parameter="bar"
    )
    
@pytest.mark.asyncio
async def test_add_optional_parameter_to_required_optional(initial_client, update_one_client):
    await initial_client.params.put_required_optional(
        required_param="foo",
        optional_param="bar"
    )
    await update_one_client.params.put_required_optional(
        required_param="foo",
        optional_param="bar"
    )
    await update_one_client.params.put_required_optional(
        required_param="foo",
        optional_param="bar",
        new_parameter="baz"
    )
    await update_one_client.params.put_required_optional(
        required_param="foo",
        new_parameter="baz"
    )

@pytest.mark.asyncio
async def test_add_optional_parameter_to_optional(initial_client, update_one_client):
    await initial_client.params.get_optional(
        optional_param="foo"
    )
    await update_one_client.params.get_optional(
        optional_param="foo"
    )
    await update_one_client.params.get_optional(
        optional_param="foo",
        new_parameter="bar"
    )

@pytest.mark.asyncio
async def test_add_new_content_type(initial_client, update_one_client):
    await initial_client.params.post_parameters({ "url": "http://example.org/myimage.jpeg" })
    await update_one_client.params.post_parameters({ "url": "http://example.org/myimage.jpeg" })
    await update_one_client.params.post_parameters(b"hello", content_type="image/jpeg")

@pytest.mark.asyncio
async def test_add_new_operation(initial_client, update_one_client):
    with pytest.raises(AttributeError):
        await initial_client.params.delete_parameters()
    await update_one_client.params.delete_parameters()

@pytest.mark.asyncio
async def test_add_new_path(initial_client, update_one_client):
    with pytest.raises(AttributeError):
        await initial_client.params.get_new_operation()
    assert await update_one_client.params.get_new_operation() == {'message': 'An object was successfully returned'}

@pytest.mark.asyncio
async def test_glass_breaker(update_one_client):
    request = HttpRequest(method="GET", url="/servicedriven/glassbreaker", params=[], headers={"Accept": "application/json"})
    response = await update_one_client.send_request(request)
    assert response.status_code == 200
    assert response.content.decode('utf8') == json.dumps({'message': 'An object was successfully returned'}, separators=(',', ':'))
