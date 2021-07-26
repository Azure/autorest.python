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

from azure.core.exceptions import DecodeError

from bodyboolean import AutoRestBoolTestService

import pytest

@pytest.fixture
def client():
    with AutoRestBoolTestService(base_url="http://localhost:3000") as client:
        yield client

class TestBool(object):

    def test_model_get_true(self, client):
        assert client.bool.get_true()

    def test_model_get_false(self, client):
        assert not client.bool.get_false()

    def test_model_get_null(self, client):
        client.bool.get_null()

    def test_model_put_false(self, client):
        client.bool.put_false()

    def test_model_put_true(self, client):
        client.bool.put_true()

    def test_model_get_invalid(self, client):
        with pytest.raises(DecodeError):
            client.bool.get_invalid()

    def test_models(self):
        from bodyboolean.models import Error

        if sys.version_info >= (3,5):
            from bodyboolean.models._models_py3 import Error as ErrorPy3
            assert Error == ErrorPy3
        else:
            from bodyboolean.models._models import Error as ErrorPy2
            assert Error == ErrorPy2

    def test_operation_groups(self):
        from bodyboolean.operations import BoolOperations

        if sys.version_info >= (3, 5):
            from bodyboolean.operations._bool_operations_py3 import BoolOperations as BoolOperationsPy3
            assert BoolOperations == BoolOperationsPy3
        else:
            from bodyboolean.operations._bool_operations import BoolOperations as BoolOperationsPy2
            assert BoolOperations == BoolOperationsPy2
