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
import unittest
import subprocess
import sys
import tempfile
import json
from uuid import uuid4
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

from azure.core.exceptions import HttpResponseError

from azurespecialproperties.aio import AutoRestAzureSpecialParametersTestClient
from azurespecialproperties import models

import pytest


@pytest.fixture
@async_generator
async def client(credential, authentication_policy):
    valid_subscription = "1234-5678-9012-3456"
    async with AutoRestAzureSpecialParametersTestClient(
        credential,
        valid_subscription,
        base_url="http://localhost:3000",
        authentication_policy=authentication_policy,
    ) as client:
        await yield_(client)


class TestXmsRequestClientId(object):
    @pytest.mark.asyncio
    async def test_client_request_id_in_exception(self, client):
        # expectedRequestId = '9C4D50EE-2D56-4CD3-8152-34347DC9F2B0'
        with pytest.raises(HttpResponseError):
            await client.xms_client_request_id.get()

    @pytest.mark.asyncio
    async def test_xms_request_client_id_in_client_none(self, client):
        # expectedRequestId = '9C4D50EE-2D56-4CD3-8152-34347DC9F2B0'
        await client.xms_client_request_id.get(request_id=None)

    @pytest.mark.asyncio
    async def test_xms_request_client_id_in_client(self, client):
        await client.xms_client_request_id.get(request_id="9C4D50EE-2D56-4CD3-8152-34347DC9F2B0")

    @pytest.mark.asyncio
    async def test_xms_request_client_overwrite_via_parameter(self, client):
        await client.xms_client_request_id.param_get(x_ms_client_request_id="9C4D50EE-2D56-4CD3-8152-34347DC9F2B0")

    @pytest.mark.asyncio
    async def test_xms_custom_named_request_id(self, client):
        await client.header.custom_named_request_id(foo_client_request_id="9C4D50EE-2D56-4CD3-8152-34347DC9F2B0")

    @pytest.mark.asyncio
    async def test_xms_custom_named_request_id_parameter_group(self, client):
        param_group = models.HeaderCustomNamedRequestIdParamGroupingParameters(
            foo_client_request_id="9C4D50EE-2D56-4CD3-8152-34347DC9F2B0"
        )
        await client.header.custom_named_request_id_param_grouping(header_custom_named_request_id_param_grouping_parameters=param_group)
