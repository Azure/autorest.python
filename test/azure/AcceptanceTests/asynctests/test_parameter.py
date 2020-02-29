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

from msrest.exceptions import DeserializationError, ValidationError

from azureparametergrouping.aio import AutoRestParameterGroupingTestService
from subscriptionidapiversion.aio import MicrosoftAzureTestUrl
from azurespecialproperties.aio import AutoRestAzureSpecialParametersTestClient

import pytest

@pytest.fixture
async def client():
    async with AutoRestParameterGroupingTestService(base_url="http://localhost:3000") as client:
        yield client

@pytest.fixture
def valid_subscription():
    return '1234-5678-9012-3456'

@pytest.fixture
async def azure_client(valid_subscription, credential, authentication_policy):
    async with AutoRestAzureSpecialParametersTestClient(
        credential, valid_subscription, base_url="http://localhost:3000", authentication_policy=authentication_policy
    ) as client:
        yield client

@pytest.fixture
def body_parameter():
    return 1234

@pytest.fixture
def header_parameter():
    return 'header'

@pytest.fixture
def query_parameter():
    return 21

@pytest.fixture
def path_parameter():
    return 'path'


@pytest.fixture
def unencoded_path():
    return 'path1/path2/path3'

@pytest.fixture
def unencoded_query():
    return 'value1&q2=value2&q3=value3'

class TestParameter(object):

    @pytest.mark.asyncio
    async def test_post_all_required_parameters(self, client, body_parameter, header_parameter, query_parameter, path_parameter):
        from azureparametergrouping.models import ParameterGroupingPostRequiredParameters
        # Valid required parameters
        required_parameters = ParameterGroupingPostRequiredParameters(body=body_parameter, path=path_parameter, custom_header=header_parameter, query=query_parameter)
        await client.parameter_grouping.post_required(required_parameters)

    @pytest.mark.asyncio
    async def test_post_required_parameters_null_optional_parameters(self, client, body_parameter, path_parameter):
        from azureparametergrouping.models import ParameterGroupingPostRequiredParameters
        #Required parameters but null optional parameters
        required_parameters = ParameterGroupingPostRequiredParameters(body=body_parameter, path=path_parameter, query=None)
        await client.parameter_grouping.post_required(required_parameters)

    @pytest.mark.asyncio
    async def test_post_required_parameters_with_null_required_property(self, client, path_parameter):
        from azureparametergrouping.models import ParameterGroupingPostRequiredParameters
        #Required parameters object is not null, but a required property of the object is
        required_parameters = ParameterGroupingPostRequiredParameters(body = None, path = path_parameter)

        with pytest.raises(ValidationError):
            await client.parameter_grouping.post_required(required_parameters)
        with pytest.raises(ValidationError):
            await client.parameter_grouping.post_required(None)

    @pytest.mark.asyncio
    async def test_post_all_optional(self, client, header_parameter, query_parameter):
        from azureparametergrouping.models import ParameterGroupingPostRequiredParameters, ParameterGroupingPostOptionalParameters
        #Valid optional parameters
        optional_parameters = ParameterGroupingPostOptionalParameters(custom_header = header_parameter, query = query_parameter)
        await client.parameter_grouping.post_optional(optional_parameters)

    @pytest.mark.asyncio
    async def test_post_none_optional(self, client):
        #null optional paramters
        await client.parameter_grouping.post_optional(None)

    @pytest.mark.asyncio
    async def test_post_all_multi_param_groups(self, client, header_parameter, query_parameter):
        from azureparametergrouping.models import FirstParameterGroup, ParameterGroupingPostMultiParamGroupsSecondParamGroup
        #Multiple grouped parameters
        first_group = FirstParameterGroup(header_one = header_parameter, query_one = query_parameter)
        second_group = ParameterGroupingPostMultiParamGroupsSecondParamGroup(header_two = "header2", query_two = 42)

        await client.parameter_grouping.post_multi_param_groups(first_group, second_group)

    @pytest.mark.asyncio
    async def test_post_some_multi_param_groups(self, client, header_parameter):
        from azureparametergrouping.models import FirstParameterGroup, ParameterGroupingPostMultiParamGroupsSecondParamGroup
        #Multiple grouped parameters -- some optional parameters omitted
        first_group = FirstParameterGroup(header_one = header_parameter)
        second_group = ParameterGroupingPostMultiParamGroupsSecondParamGroup(query_two = 42)

        await client.parameter_grouping.post_multi_param_groups(first_group, second_group)

    @pytest.mark.asyncio
    async def test_post_shared_parameter_group_object(self, client, header_parameter):
        from azureparametergrouping.models import FirstParameterGroup
        first_group = FirstParameterGroup(header_one = header_parameter)
        await client.parameter_grouping.post_shared_parameter_group_object(first_group)

    @pytest.mark.asyncio
    async def test_subscription_in_credentials(self, azure_client):
        # valid_api_version = '2.0'
        await azure_client.subscription_in_credentials.post_method_global_not_provided_valid()
        await azure_client.subscription_in_credentials.post_method_global_valid()
        await azure_client.subscription_in_credentials.post_path_global_valid()
        await azure_client.subscription_in_credentials.post_swagger_global_valid()

    @pytest.mark.asyncio
    async def test_subscription_in_method(self, azure_client, valid_subscription):
        await azure_client.subscription_in_method.post_method_local_valid(valid_subscription)
        await azure_client.subscription_in_method.post_path_local_valid(valid_subscription)
        await azure_client.subscription_in_method.post_swagger_local_valid(valid_subscription)
        with pytest.raises(ValidationError):
            await azure_client.subscription_in_method.post_method_local_null(None)

    @pytest.mark.asyncio
    async def test_api_version_default(self, azure_client):
        await azure_client.api_version_default.get_method_global_not_provided_valid()
        await azure_client.api_version_default.get_method_global_valid()
        await azure_client.api_version_default.get_path_global_valid()
        await azure_client.api_version_default.get_swagger_global_valid()

    @pytest.mark.xfail(reason="https://github.com/Azure/autorest.modelerfour/issues/93")
    @pytest.mark.asyncio
    async def test_api_version_local(self, azure_client):
        await azure_client.api_version_local.get_method_local_valid()
        await azure_client.api_version_local.get_method_local_null()
        await azure_client.api_version_local.get_path_local_valid()
        await azure_client.api_version_local.get_swagger_local_valid()

    @pytest.mark.asyncio
    async def test_skip_url_encoding(self, azure_client, unencoded_path, unencoded_query):
        await azure_client.skip_url_encoding.get_method_path_valid(unencoded_path)
        await azure_client.skip_url_encoding.get_path_valid(unencoded_path)
        await azure_client.skip_url_encoding.get_swagger_path_valid()
        await azure_client.skip_url_encoding.get_method_query_valid(unencoded_query)
        await azure_client.skip_url_encoding.get_path_query_valid(unencoded_query)
        await azure_client.skip_url_encoding.get_swagger_query_valid()
        await azure_client.skip_url_encoding.get_method_query_null()
        await azure_client.skip_url_encoding.get_method_query_null(None)

    @pytest.mark.asyncio
    async def test_azure_odata(self, azure_client):
        await azure_client.odata.get_with_filter(filter="id gt 5 and name eq 'foo'", top=10, orderby="id")
