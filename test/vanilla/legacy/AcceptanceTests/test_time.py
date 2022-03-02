# coding=utf-8
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

import datetime

from bodytime import AutoRestTimeTestService
import pytest
import sys

@pytest.fixture
def client():
    with AutoRestTimeTestService(base_url="http://localhost:3000") as client:
        yield client

class TestTime(object):

    def test_get(self, client):
        assert client.time.get() == datetime.time(11, 34, 56)

    def test_put(self, client):
        result = client.time.put(datetime.time(8, 7, 56))
        assert result == "Nice job posting time"

    def test_models(self):
        from bodytime.models import Error

        from bodytime.models._models_py3 import Error as ErrorPy3
        assert Error == ErrorPy3

    def test_operation_groups(self):
        from bodytime.operations import TimeOperations

        with pytest.raises(ImportError):
            from bodytime.operations import _time_operations_py3

        from bodytime.operations._time_operations import TimeOperations as TimeOperationsPy2
        assert TimeOperations == TimeOperationsPy2
