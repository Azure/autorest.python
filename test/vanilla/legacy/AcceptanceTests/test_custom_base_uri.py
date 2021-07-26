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
import os
from datetime import date, datetime, timedelta
from os.path import dirname, pardir, join, realpath

from msrest.exceptions import (
    DeserializationError,
    SerializationError,
    ValidationError)

from azure.core.exceptions import ServiceRequestError

from custombaseurl import AutoRestParameterizedHostTestClient
from custombaseurl.models import Error
from custombaseurlmoreoptions import AutoRestParameterizedCustomHostTestClient

import pytest

@pytest.fixture
def client():
    with AutoRestParameterizedHostTestClient("host:3000", retry_total = 0) as client:
        yield client

class TestCustomBaseUri(object):

    def test_positive(self):
        client = AutoRestParameterizedHostTestClient("host:3000")
        client.paths.get_empty("local")

    def test_get_empty_with_bad_string(self, client):
        with pytest.raises(ServiceRequestError):
            client.paths.get_empty("bad")

    def test_get_empty_with_none(self, client):
        with pytest.raises(ValidationError):
            client.paths.get_empty(None)

    def test_get_empty_from_bad_host(self):
        with AutoRestParameterizedHostTestClient("badhost:3000", retry_total = 0) as client:
            with pytest.raises(ServiceRequestError):
                client.paths.get_empty("local")

    def test_more_options(self):
        with AutoRestParameterizedCustomHostTestClient("test12", "host:3000") as client:
            client.paths.get_empty("http://lo", "cal", "key1")

    def test_models(self):
        from custombaseurl.models import Error

        if sys.version_info >= (3,5):
            from custombaseurl.models._models_py3 import Error as ErrorPy3
            assert Error == ErrorPy3
        else:
            from custombaseurl.models._models import Error as ErrorPy2
            assert Error == ErrorPy2

    def test_operation_groups(self):
        from custombaseurl.operations import PathsOperations

        if sys.version_info >= (3, 5):
            from custombaseurl.operations._paths_operations_py3 import PathsOperations as PathsOperationsPy3
            assert PathsOperations == PathsOperationsPy3
        else:
            from custombaseurl.operations._paths_operations import PathsOperations as PathsOperationsPy2
            assert PathsOperations == PathsOperationsPy2
