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

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "AzureParameterGrouping"))
sys.path.append(join(tests, "SubscriptionIdApiVersion"))
sys.path.append(join(tests, "AzureBodyDuration"))
sys.path.append(join(tests, "AzureSpecials"))

from msrest.authentication import BasicTokenAuthentication
from msrest.exceptions import DeserializationError, ValidationError

from azureparametergrouping import AutoRestParameterGroupingTestService
from subscriptionidapiversion import MicrosoftAzureTestUrl
from bodyduration import AutoRestDurationTestService
from azurespecialproperties import AutoRestAzureSpecialParametersTestClient

from azureparametergrouping.models import (
    ParameterGroupingPostMultiParamGroupsSecondParamGroup,
    ParameterGroupingPostOptionalParameters,
    ParameterGroupingPostRequiredParameters,
    FirstParameterGroup)

import pytest

class TestParameter(object):

    @pytest.mark.asyncio
    async def test_parameter_grouping(self):

        bodyParameter = 1234
        headerParameter = 'header'
        queryParameter = 21
        pathParameter = 'path'

        cred = BasicTokenAuthentication({"access_token" :str(uuid4())})
        client = AutoRestParameterGroupingTestService(cred, base_url="http://localhost:3000")

        # Valid required parameters
        requiredParameters = ParameterGroupingPostRequiredParameters(body=bodyParameter, path=pathParameter, custom_header=headerParameter, query=queryParameter)
        await client.parameter_grouping.post_required_async(requiredParameters)

        #Required parameters but null optional parameters
        requiredParameters = ParameterGroupingPostRequiredParameters(body=bodyParameter, path=pathParameter, query=None)
        await client.parameter_grouping.post_required_async(requiredParameters)

        #Required parameters object is not null, but a required property of the object is
        requiredParameters = ParameterGroupingPostRequiredParameters(body = None, path = pathParameter)

        with pytest.raises(ValidationError):
            await client.parameter_grouping.post_required_async(requiredParameters)
        with pytest.raises(ValidationError):
            await client.parameter_grouping.post_required_async(None)

        #Valid optional parameters
        optionalParameters = ParameterGroupingPostOptionalParameters(custom_header = headerParameter, query = queryParameter)
        await client.parameter_grouping.post_optional_async(optionalParameters)

        #null optional paramters
        await client.parameter_grouping.post_optional_async(None)

        #Multiple grouped parameters
        firstGroup = FirstParameterGroup(header_one = headerParameter, query_one = queryParameter)
        secondGroup = ParameterGroupingPostMultiParamGroupsSecondParamGroup(header_two = "header2", query_two = 42)

        await client.parameter_grouping.post_multi_param_groups_async(firstGroup, secondGroup)

        #Multiple grouped parameters -- some optional parameters omitted
        firstGroup = FirstParameterGroup(header_one = headerParameter)
        secondGroup = ParameterGroupingPostMultiParamGroupsSecondParamGroup(query_two = 42)

        await client.parameter_grouping.post_multi_param_groups_async(firstGroup, secondGroup)
        await client.parameter_grouping.post_shared_parameter_group_object_async(firstGroup)

    @pytest.mark.asyncio
    async def test_azure_special_parameters(self):

        validSubscription = '1234-5678-9012-3456'
        validApiVersion = '2.0'
        unencodedPath = 'path1/path2/path3'
        unencodedQuery = 'value1&q2=value2&q3=value3'
        cred = BasicTokenAuthentication({"access_token" :str(uuid4())})
        client = AutoRestAzureSpecialParametersTestClient(cred, validSubscription, base_url="http://localhost:3000")

        await client.subscription_in_credentials.post_method_global_not_provided_valid_async()
        await client.subscription_in_credentials.post_method_global_valid_async()
        await client.subscription_in_credentials.post_path_global_valid_async()
        await client.subscription_in_credentials.post_swagger_global_valid_async()
        await client.subscription_in_method.post_method_local_valid_async(validSubscription)
        await client.subscription_in_method.post_path_local_valid_async(validSubscription)
        await client.subscription_in_method.post_swagger_local_valid_async(validSubscription)
        with pytest.raises(ValidationError):
            await client.subscription_in_method.post_method_local_null_async(None)

        await client.api_version_default.get_method_global_not_provided_valid_async()
        await client.api_version_default.get_method_global_valid_async()
        await client.api_version_default.get_path_global_valid_async()
        await client.api_version_default.get_swagger_global_valid_async()
        await client.api_version_local.get_method_local_valid_async()
        await client.api_version_local.get_method_local_null_async()
        await client.api_version_local.get_path_local_valid_async()
        await client.api_version_local.get_swagger_local_valid_async()

        await client.skip_url_encoding.get_method_path_valid_async(unencodedPath)
        await client.skip_url_encoding.get_path_path_valid_async(unencodedPath)
        await client.skip_url_encoding.get_swagger_path_valid_async()
        await client.skip_url_encoding.get_method_query_valid_async(unencodedQuery)
        await client.skip_url_encoding.get_path_query_valid_async(unencodedQuery)
        await client.skip_url_encoding.get_swagger_query_valid_async()
        await client.skip_url_encoding.get_method_query_null_async()
        await client.skip_url_encoding.get_method_query_null_async(None)

    @pytest.mark.asyncio
    async def test_azure_odata(self):

        validSubscription = '1234-5678-9012-3456'
        cred = BasicTokenAuthentication({"access_token" :str(uuid4())})
        client = AutoRestAzureSpecialParametersTestClient(cred, validSubscription, base_url="http://localhost:3000")
        await client.odata.get_with_filter_async(filter="id gt 5 and name eq 'foo'", top=10, orderby="id")


if __name__ == '__main__':
    unittest.main()
