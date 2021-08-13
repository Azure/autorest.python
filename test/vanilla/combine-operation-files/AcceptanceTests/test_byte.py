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

from msrest.exceptions import DeserializationError

from bodybytecombineoperationfiles import AutoRestSwaggerBATByteService

import pytest

@pytest.fixture
def client():
    with AutoRestSwaggerBATByteService(base_url="http://localhost:3000") as client:
        yield client

class TestByte(object):

    def test_non_ascii(self, client):
        tests = bytearray([0x0FF, 0x0FE, 0x0FD, 0x0FC, 0x0FB, 0x0FA, 0x0F9, 0x0F8, 0x0F7, 0x0F6])
        client.byte.put_non_ascii(tests)
        assert tests ==  client.byte.get_non_ascii()

    def test_get_null(self, client):
        assert client.byte.get_null() is None

    def test_get_empty(self, client):
        assert bytearray() ==  client.byte.get_empty()

    def test_get_invalid(self, client):
        with pytest.raises(DeserializationError):
            client.byte.get_invalid()

    def test_models(self):
        from bodybytecombineoperationfiles.models import Error

        if sys.version_info >= (3,5):
            from bodybytecombineoperationfiles.models._models_py3 import Error as ErrorPy3
            assert Error == ErrorPy3
        else:
            from bodybytecombineoperationfiles.models._models import Error as ErrorPy2
            assert Error == ErrorPy2

    def test_operation_groups(self):
        from bodybytecombineoperationfiles.operations import ByteOperations

        with pytest.raises(ImportError):
            from bodybytecombineoperationfiles.operations import _combine_operations_py3
            
        from bodybytecombineoperationfiles.operations._combine_operations import ByteOperations as ByteOperationsPy2
        assert ByteOperations == ByteOperationsPy2
