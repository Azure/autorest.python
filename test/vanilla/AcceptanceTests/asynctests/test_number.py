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
from decimal import Decimal
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "BodyNumber"))

from msrest.serialization import Deserializer
from msrest.exceptions import DeserializationError

from bodynumber import AutoRestNumberTestService

import pytest

class TestNumber(object):

    @pytest.mark.asyncio
    async def test_numbers(self):
        client = AutoRestNumberTestService(base_url="http://localhost:3000")

        await client.number.put_big_float_async(3.402823e+20)
        await client.number.put_small_float_async(3.402823e-20)
        await client.number.put_big_double_async(2.5976931e+101)
        await client.number.put_small_double_async(2.5976931e-101)
        await client.number.put_big_double_negative_decimal_async()
        await client.number.put_big_double_positive_decimal_async()
        await client.number.put_big_decimal_async(Decimal(2.5976931e+101))
        await client.number.put_small_decimal_async(Decimal(2.5976931e-101))
        # await client.number.put_big_decimal_positive_decimal_async()
        # await client.number.put_big_decimal_negative_decimal_async()
        await client.number.get_null_async()
        assert await client.number.get_big_float_async() ==  3.402823e+20
        assert await client.number.get_small_float_async() ==  3.402823e-20
        assert await client.number.get_big_double_async() ==  2.5976931e+101
        assert await client.number.get_small_double_async() ==  2.5976931e-101
        assert await client.number.get_big_double_negative_decimal_async() ==  -99999999.99
        assert await client.number.get_big_double_positive_decimal_async() ==  99999999.99
        assert await client.number.get_big_decimal_async() ==  2.5976931e+101
        assert await client.number.get_small_decimal_async() ==  2.5976931e-101
        assert await client.number.get_big_decimal_negative_decimal_async() ==  -99999999.99
        assert await client.number.get_big_decimal_positive_decimal_async() ==  99999999.99

        with pytest.raises(DeserializationError):
            await client.number.get_invalid_decimal_async()

        with pytest.raises(DeserializationError):
            await client.number.get_invalid_double_async()

        with pytest.raises(DeserializationError):
            await client.number.get_invalid_float_async()
