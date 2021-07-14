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

from msrest.exceptions import (
    DeserializationError,
    SerializationError,
    ValidationError
)

from azure.core.exceptions import ServiceRequestError

from custombaseurl import AutoRestParameterizedHostTestClient
from custombaseurl.models import Error

import pytest

@pytest.fixture
def client():
    with AutoRestParameterizedHostTestClient(host="host:3000") as client:
        client._config.retry_policy.retries = 0
        yield client

class TestCustomBaseUri(object):

    def test_custom_base_uri_positive(self, client):
        client.paths.get_empty("local")

    def test_custom_base_uri_get_empty(self, client):
        with pytest.raises(ServiceRequestError):
            client.paths.get_empty("bad")

    def test_custom_base_uri_get_none(self, client):
        with pytest.raises(ValidationError):
            client.paths.get_empty(None)

    def test_custom_base_uri_bad_host(self, client):
        client._config.host = "badhost:3000"
        with pytest.raises(ServiceRequestError):
            client.paths.get_empty("local")

    def test_models(self):
        from custombaseurl.models import Error

        if sys.version_info >= (3,5):
            from custombaseurl.models._models_py3 import Error as ErrorPy3
            assert Error == ErrorPy3
        else:
            from custombaseurl.models._models import Error as ErrorPy2
            assert Error == ErrorPy2
