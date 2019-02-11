﻿# --------------------------------------------------------------------------
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

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "Head"))
sys.path.append(join(tests, "HeadExceptions"))

from msrest.serialization import Deserializer
from msrest.exceptions import DeserializationError, HttpOperationError
from msrest.authentication import BasicTokenAuthentication
from msrestazure.azure_exceptions import CloudError, CloudErrorData

from head.aio import AutoRestHeadTestService
from headexceptions.aio import AutoRestHeadExceptionTestService

import pytest

class TestHead(object):

    @pytest.mark.asyncio
    async def test_head(self):

        cred = BasicTokenAuthentication({"access_token" :str(uuid4())})
        client = AutoRestHeadTestService(cred, base_url="http://localhost:3000")

        assert await client.http_success.head200()
        assert await client.http_success.head204()
        assert not await client.http_success.head404()

    @pytest.mark.asyncio
    async def test_head_exception(self):

        cred = BasicTokenAuthentication({"access_token" :str(uuid4())})
        client = AutoRestHeadExceptionTestService(cred, base_url="http://localhost:3000")

        await client.head_exception.head200()
        await client.head_exception.head204()
        with pytest.raises(CloudError):
            await client.head_exception.head404()


if __name__ == '__main__':
    unittest.main()
