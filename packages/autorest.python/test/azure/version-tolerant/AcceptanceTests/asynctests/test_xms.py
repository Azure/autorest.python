﻿# --------------------------------------------------------------------------
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

from azure.core.exceptions import HttpResponseError

from azurespecialpropertiesversiontolerant.aio import AutoRestAzureSpecialParametersTestClient

import pytest


@pytest.fixture
@async_generator
async def client(credential, authentication_policy):
    valid_subscription = "1234-5678-9012-3456"
    async with AutoRestAzureSpecialParametersTestClient(
        credential, valid_subscription, authentication_policy=authentication_policy, endpoint="http://localhost:3000"
    ) as client:
        await yield_(client)


@pytest.fixture
@async_generator
async def client_no_request_id(credential, authentication_policy):
    valid_subscription = "1234-5678-9012-3456"
    async with AutoRestAzureSpecialParametersTestClient(
        credential,
        valid_subscription,
        auto_request_id=False,
        authentication_policy=authentication_policy,
        endpoint="http://localhost:3000",
    ) as client:
        await yield_(client)


@pytest.mark.asyncio
async def test_client_request_id_in_exception(client):
    # expectedRequestId = '9C4D50EE-2D56-4CD3-8152-34347DC9F2B0'
    with pytest.raises(HttpResponseError):
        await client.xms_client_request_id.get()


@pytest.mark.asyncio
async def test_xms_request_client_id_in_client_none(client):
    # expectedRequestId = '9C4D50EE-2D56-4CD3-8152-34347DC9F2B0'
    await client.xms_client_request_id.get(request_id=None)


@pytest.mark.asyncio
async def test_xms_request_client_id_in_client(client):
    await client.xms_client_request_id.get(request_id="9C4D50EE-2D56-4CD3-8152-34347DC9F2B0")


@pytest.mark.asyncio
async def test_xms_request_client_overwrite_via_parameter(client_no_request_id):
    # We DON'T support a Swagger parameter for request_id, the request_id policy will overwrite it.
    # We disable the request_id policy for this test
    await client_no_request_id.xms_client_request_id.param_get(
        headers={"x-ms-client-request-id": "9C4D50EE-2D56-4CD3-8152-34347DC9F2B0"}
    )


@pytest.mark.asyncio
async def test_xms_custom_named_request_id(client):
    await client.header.custom_named_request_id(foo_client_request_id="9C4D50EE-2D56-4CD3-8152-34347DC9F2B0")


@pytest.mark.asyncio
async def test_xms_custom_named_request_id_parameter_group(client):
    await client.header.custom_named_request_id_param_grouping(
        foo_client_request_id="9C4D50EE-2D56-4CD3-8152-34347DC9F2B0"
    )
