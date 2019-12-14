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

import unittest
import subprocess
import sys
import isodate
import tempfile
import json
from uuid import uuid4
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "AzureSpecials"))

from azure.core.exceptions import HttpResponseError

from azurespecialproperties.aio import AutoRestAzureSpecialParametersTestClient
from azurespecialproperties import models

import pytest

@pytest.fixture
async def client(credential, authentication_policy):
    valid_subscription = '1234-5678-9012-3456'
    async with AutoRestAzureSpecialParametersTestClient(
        credential, valid_subscription, base_url="http://localhost:3000", authentication_policy=authentication_policy
    ) as client:
        yield client

class TestXmsRequestClientId(object):
    @pytest.mark.asyncio
    async def test_client_request_id_in_exception(self, client):
        # expectedRequestId = '9C4D50EE-2D56-4CD3-8152-34347DC9F2B0'

        try:
            await client.x_ms_client_request_id.get()
            self.fail("HttpResponseError wasn't raised as expected")

        except HttpResponseError as err:
            pass

    @pytest.mark.asyncio
    async def test_xms_request_client_id_in_client(self, client):
        # expectedRequestId = '9C4D50EE-2D56-4CD3-8152-34347DC9F2B0'

        client._config.generate_client_request_id = False
        await client.x_ms_client_request_id.get()
