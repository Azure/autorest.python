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
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

from azure.core.exceptions import DeserializationError

from bodyduration import AutoRestDurationTestService

import pytest

@pytest.fixture
def client():
    with AutoRestDurationTestService(base_url="http://localhost:3000") as client:
        yield client

class TestDuration(object):

    def test_get_null_and_invalid(self, client):
        assert client.duration.get_null() is None

        with pytest.raises(DeserializationError):
            client.duration.get_invalid()

    def test_positive_duration(self, client):
        client.duration.get_positive_duration()
        client.duration.put_positive_duration(timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11))

    def test_models(self):
        from bodyduration.models import Error

        from bodyduration.models._models_py3 import Error as ErrorPy3
        assert Error == ErrorPy3

    def test_operation_groups(self):
        from bodyduration.operations import DurationOperations

        with pytest.raises(ImportError):
            from bodyduration.operations import _duration_operations_py3

        from bodyduration.operations._duration_operations import DurationOperations as DurationOperationsPy2
        assert DurationOperations == DurationOperationsPy2
