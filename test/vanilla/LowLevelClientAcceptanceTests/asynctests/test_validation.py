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

from msrest.exceptions import ValidationError
from async_generator import yield_, async_generator

from validation.aio import AutoRestValidationTest
from validation.models import (
    Product,
    ConstantProduct,
    ChildProduct)
from validation._rest import *

import pytest

@pytest.fixture
@async_generator
async def client():
    async with AutoRestValidationTest(
            "abc123",
            base_url="http://localhost:3000") as client:
        client.api_version = "12-34-5678"
        await yield_(client)

@pytest.fixture
def make_request(client, base_make_request):
    async def _make_request(request):
        return await base_make_request(client, request)
    return _make_request

@pytest.fixture
def make_request_json_response(client, base_make_request_json_response):
    async def _make_request(request):
        return await base_make_request_json_response(client, request)
    return _make_request

@pytest.fixture
def constant_body():
    """This is NOT considering the constant body, this should work with
    the commented line.
    See https://github.com/Azure/autorest.modelerfour/issues/83
    """
    #return Product(child=ChildProduct())
    return Product(
        child=ChildProduct(),
        const_child=ConstantProduct(),
    )

@pytest.mark.asyncio
async def test_with_constant_in_path(make_request):
    request = build_get_with_constant_in_path_request()
    await make_request(request)

@pytest.mark.asyncio
async def test_post_with_constant_in_body(make_request_json_response, constant_body):
    request = build_post_with_constant_in_body_request(json=constant_body.serialize())
    product = Product.deserialize(await make_request_json_response(request))
    assert product is not None

@pytest.mark.asyncio
async def test_min_length_validation(make_request):
    try:
        request = build_validation_of_method_parameters_request(subscription_id="abc123", resource_group_name="1", id=100)
        await make_request(request)
    except ValidationError as err:
        assert err.rule ==  "min_length"
        assert err.target ==  "resource_group_name"

@pytest.mark.asyncio
async def test_max_length_validation(make_request):
    try:
        request = build_validation_of_method_parameters_request(subscription_id="abc123", resource_group_name="1234567890A", id=100)
        await make_request(request)
    except ValidationError as err:
        assert err.rule ==  "max_length"
        assert err.target ==  "resource_group_name"

@pytest.mark.asyncio
async def test_pattern_validation(make_request):
    try:
        request = build_validation_of_method_parameters_request(subscription_id="abc123", resource_group_name="!@#$", id=100)
        await make_request(request)
    except ValidationError as err:
        assert err.rule ==  "pattern"
        assert err.target ==  "resource_group_name"

@pytest.mark.asyncio
async def test_multiple_validation(make_request):
    try:
        request = build_validation_of_method_parameters_request(subscription_id="abc123", resource_group_name="123", id=105)
        await make_request(request)
    except ValidationError as err:
        assert err.rule ==  "multiple"
        assert err.target ==  "id"

@pytest.mark.asyncio
async def test_minimum_validation(make_request):
    try:
        request = build_validation_of_method_parameters_request(subscription_id="abc123", resource_group_name="123", id=0)
        await make_request(request)
    except ValidationError as err:
        assert err.rule ==  "minimum"
        assert err.target ==  "id"

@pytest.mark.asyncio
async def test_maximum_validation(make_request):
    try:
        request = build_validation_of_method_parameters_request(subscription_id="abc123", resource_group_name="123", id=2000)
        await make_request(request)
    except ValidationError as err:
        assert err.rule ==  "maximum"
        assert err.target ==  "id"

# NOTE: removed body validation, since it doesn't make sense for LLC as we serialize the body ourselves and pass it in


@pytest.mark.xfail(reason="https://github.com/Azure/autorest.modelerfour/issues/90")
@pytest.mark.asyncio
async def test_api_version_validation(make_request):
    client = AutoRestValidationTest(
        "abc123",
        base_url="http://localhost:3000")
    client.api_version = "abc"
    try:
        request = build_validation_of_method_parameters_request(subscription_id="abc123", resource_group_name="123", id=150)
        await make_request(request)
    except ValidationError as err:
        assert err.rule ==  "pattern"
        assert err.target ==  "self.api_version"
