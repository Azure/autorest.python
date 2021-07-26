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
import sys
from nonstringenums import NonStringEnumsClient
from nonstringenums.models import IntEnum, FloatEnum

import pytest
import json

@pytest.fixture
def client():
    with NonStringEnumsClient() as client:
        yield client


class TestNonStringEnums(object):

    def test_put_int_enum(self, client):
        result = client.int.put(IntEnum.TWO_HUNDRED)
        assert result == "Nice job posting an int enum"

    def test_get_int_enum(self, client):
        result = client.int.get()
        assert result == IntEnum.FOUR_HUNDRED_TWENTY_NINE.value

    def test_put_float_enum(self, client):
        result = client.float.put(FloatEnum.TWO_HUNDRED4)
        assert result == "Nice job posting a float enum"

    def test_get_float_enum(self, client):
        result = client.float.get()
        assert result == FloatEnum.FOUR_HUNDRED_TWENTY_NINE1.value

    def test_lowercase_enum_retrieval(self):
        assert FloatEnum.four_hundred_twenty_nine1 == FloatEnum.FOUR_HUNDRED_TWENTY_NINE1
        assert 429.1 == FloatEnum.FOUR_HUNDRED_TWENTY_NINE1

    def test_operation_groups(self):
        from nonstringenums.operations import FloatOperations

        if sys.version_info >= (3, 5):
            from nonstringenums.operations._float_operations_py3 import FloatOperations as FloatOperationsPy3
            assert FloatOperations == FloatOperationsPy3
        else:
            from nonstringenums.operations._float_operations import FloatOperations as FloatOperationsPy2
            assert FloatOperations == FloatOperationsPy2