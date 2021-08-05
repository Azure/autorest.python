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

import pytest

from subscriptionidapiversion import MicrosoftAzureTestUrl
from subscriptionidapiversion.models import SampleResourceGroup

class TestAzureUrl(object):

    def test_azure_url(self, credential, authentication_policy):

        sub_id = str(uuid4())

        with MicrosoftAzureTestUrl(credential, sub_id, base_url="http://localhost:3000", authentication_policy=authentication_policy) as client:

            group = client.group.get_sample_resource_group("testgoup101")
            assert group.name ==  "testgroup101"
            assert group.location ==  "West US"

    def test_models(self):
        from subscriptionidapiversion.models import Error

        if sys.version_info >= (3,5):
            from subscriptionidapiversion.models._models_py3 import Error as ErrorPy3
            assert Error == ErrorPy3
        else:
            from subscriptionidapiversion.models._models import Error as ErrorPy2
            assert Error == ErrorPy2

    def test_operation_groups(self):
        from subscriptionidapiversion.operations import GroupOperations

        with pytest.raises(ImportError):
            from subscriptionidapiversion.operations import _group_operations_py3

        from subscriptionidapiversion.operations._group_operations import GroupOperations as GroupOperationsPy2
        assert GroupOperations == GroupOperationsPy2
