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

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "BodyDate"))

from msrest.serialization import Deserializer
from msrest.exceptions import DeserializationError

from bodydate import AutoRestDateTestService

import pytest

class TestDate(object):

    @pytest.mark.asyncio
    async def test_date(self):
        client = AutoRestDateTestService(base_url="http://localhost:3000")

        max_date = isodate.parse_date("9999-12-31T23:59:59.999999Z")
        min_date = isodate.parse_date("0001-01-01T00:00:00Z")
        await client.date_model.put_max_date_async(max_date)
        await client.date_model.put_min_date_async(min_date)

        assert max_date ==  await client.date_model.get_max_date_async()
        assert min_date ==  await client.date_model.get_min_date_async()
        assert await client.date_model.get_null_async() is None

        with pytest.raises(DeserializationError):
            await client.date_model.get_invalid_date_async()

        with pytest.raises(DeserializationError):
            await client.date_model.get_overflow_date_async()

        with pytest.raises(DeserializationError):
            await client.date_model.get_underflow_date_async()

if __name__ == '__main__':
    unittest.main()
