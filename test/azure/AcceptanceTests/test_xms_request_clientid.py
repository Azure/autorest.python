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

from msrest.serialization import Deserializer
from msrest.authentication import BasicTokenAuthentication
from azure.core.exceptions import HttpResponseError

from azurespecialproperties import AutoRestAzureSpecialParametersTestClient
from azurespecialproperties import models

import pytest

@pytest.fixture
def client():
    valid_subscription = '1234-5678-9012-3456'
    cred = BasicTokenAuthentication({"access_token":123})
    with AutoRestAzureSpecialParametersTestClient(cred, valid_subscription, base_url="http://localhost:3000") as client:
        yield client

class TestXmsRequestClientId(object):

    def test_client_request_id_in_exception(self, client):
        try:
            client.xms_client_request_id.get()
            pytest.fail("HttpResponseError wasn't raised as expected")

        except HttpResponseError as err:
            pass

    def test_xms_request_client_id_in_client(self, client):
        client._config.generate_client_request_id = False
        client.xms_client_request_id.get()
