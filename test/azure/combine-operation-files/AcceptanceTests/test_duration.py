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

from msrest.exceptions import DeserializationError

from bodydurationcombineoperationfiles import AutoRestDurationTestService

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
        delta = timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11)
        client.duration.put_positive_duration(delta)

    def test_models(self):
        from bodydurationcombineoperationfiles.models import Error

        if sys.version_info >= (3,5):
            from bodydurationcombineoperationfiles.models._models_py3 import Error as ErrorPy3
            assert Error == ErrorPy3
        else:
            from bodydurationcombineoperationfiles.models._models import Error as ErrorPy2
            assert Error == ErrorPy2

    def test_operation_groups(self):
        from bodydurationcombineoperationfiles.operations import DurationOperations

        with pytest.raises(ImportError):
            from bodydurationcombineoperationfiles.operations import _duration_operations_py3

        from bodydurationcombineoperationfiles.operations._combine_operations import DurationOperations as DurationOperationsPy2
        assert DurationOperations == DurationOperationsPy2
