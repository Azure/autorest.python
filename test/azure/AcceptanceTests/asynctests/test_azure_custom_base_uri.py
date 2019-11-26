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
import os
from os.path import dirname, pardir, join, realpath

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "CustomBaseUri"))

from msrest.serialization import Deserializer
from msrest.exceptions import (
    DeserializationError,
    SerializationError,
    ValidationError
)
from msrest.authentication import BasicTokenAuthentication

from azure.core.exceptions import ServiceRequestError

from custombaseurl.aio import AutoRestParameterizedHostTestClient
from custombaseurl.models import Error, ErrorException

import pytest

@pytest.fixture
def client():
    cred = BasicTokenAuthentication({"access_token" :str(uuid4())})
    client = AutoRestParameterizedHostTestClient(cred, host="host:3000")
    client._config.retry_policy.retries = 0
    return client

class TestCustomBaseUri(object):

    @pytest.mark.asyncio
    async def test_custom_base_uri_positive(self, client):
        await client.paths.get_empty("local")

    @pytest.mark.asyncio
    async def test_custom_base_uri_get_empty(self, client):
        with pytest.raises(ServiceRequestError):
            await client.paths.get_empty("bad")

    @pytest.mark.asyncio
    async def test_custom_base_uri_get_none(self, client):
        with pytest.raises(ValidationError):
            await client.paths.get_empty(None)

    @pytest.mark.asyncio
    async def test_custom_base_uri_bad_host(self, client):
        client._config.host = "badhost:3000"
        with pytest.raises(ServiceRequestError):
            await client.paths.get_empty("local")

