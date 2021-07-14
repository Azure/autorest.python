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

from head import AutoRestHeadTestService
from headexceptions import AutoRestHeadExceptionTestService

from azure.core.exceptions import HttpResponseError

import pytest

class TestHead(object):

    def test_head(self, credential, authentication_policy):

        with AutoRestHeadTestService(credential, base_url="http://localhost:3000", authentication_policy=authentication_policy) as client:

            assert client.http_success.head200()
            assert client.http_success.head204()
            assert not client.http_success.head404()

    def test_head_exception(self, credential, authentication_policy):

        with AutoRestHeadExceptionTestService(credential, base_url="http://localhost:3000", authentication_policy=authentication_policy) as client:

            client.head_exception.head200()
            client.head_exception.head204()
            with pytest.raises(HttpResponseError):
                client.head_exception.head404()
