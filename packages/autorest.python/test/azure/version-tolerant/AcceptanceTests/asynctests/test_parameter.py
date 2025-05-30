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
from azure.core.exceptions import HttpResponseError
from async_generator import yield_, async_generator

from azureparametergroupingversiontolerant.aio import AutoRestParameterGroupingTestService
from azurespecialpropertiesversiontolerant.aio import AutoRestAzureSpecialParametersTestClient


import pytest


@pytest.fixture
@async_generator
async def client():
    async with AutoRestParameterGroupingTestService() as client:
        await yield_(client)


@pytest.fixture
def valid_subscription():
    return "1234-5678-9012-3456"


@pytest.fixture
@async_generator
async def azure_client(valid_subscription, credential, authentication_policy):
    async with AutoRestAzureSpecialParametersTestClient(
        credential, valid_subscription, authentication_policy=authentication_policy, endpoint="http://localhost:3000"
    ) as client:
        await yield_(client)


@pytest.fixture
def body_parameter():
    return 1234


@pytest.fixture
def header_parameter():
    return "header"


@pytest.fixture
def query_parameter():
    return 21


@pytest.fixture
def path_parameter():
    return "path"


@pytest.fixture
def unencoded_path():
    return "path1/path2/path3"


@pytest.fixture
def unencoded_query():
    return "value1&q2=value2&q3=value3"


@pytest.mark.asyncio
async def test_post_all_required_parameters(client, body_parameter, header_parameter, query_parameter, path_parameter):
    await client.parameter_grouping.post_required(
        path_parameter,
        body_parameter,
        query=query_parameter,
        custom_header=header_parameter,
    )


@pytest.mark.asyncio
async def test_post_required_parameters_null_optional_parameters(client, body_parameter, path_parameter):
    await client.parameter_grouping.post_required(path_parameter, body_parameter, query=None)


@pytest.mark.asyncio
async def test_post_required_parameters_with_null_required_property(client, path_parameter):

    with pytest.raises(HttpResponseError):
        # supposed to raise a validation error, but since we don't validate, we get a service error instead
        await client.parameter_grouping.post_required(path_parameter, body=None)
    with pytest.raises(TypeError):
        await client.parameter_grouping.post_required()


@pytest.mark.asyncio
async def test_post_all_optional(client, header_parameter, query_parameter):
    await client.parameter_grouping.post_optional(
        custom_header=header_parameter,
        query=query_parameter,
    )


@pytest.mark.asyncio
async def test_post_none_optional(client):
    await client.parameter_grouping.post_optional(query=None)


@pytest.mark.asyncio
async def test_post_all_multi_param_groups(client, header_parameter, query_parameter):
    await client.parameter_grouping.post_multi_param_groups(
        header_one=header_parameter,
        query_one=query_parameter,
        header_two="header2",
        query_two=42,
    )


@pytest.mark.asyncio
async def test_post_some_multi_param_groups(client, header_parameter):
    await client.parameter_grouping.post_multi_param_groups(
        header_one=header_parameter,
        query_two=42,
    )


@pytest.mark.asyncio
async def test_post_shared_parameter_group_object(client, header_parameter):
    await client.parameter_grouping.post_shared_parameter_group_object(header_one=header_parameter)


@pytest.mark.asyncio
async def test_post_reserved_words(client):
    await client.parameter_grouping.post_reserved_words(from_parameter="bob", accept_parameter="yes")


@pytest.mark.asyncio
async def test_subscription_in_credentials(azure_client):
    # valid_api_version = '2.0'
    await azure_client.subscription_in_credentials.post_method_global_not_provided_valid()
    await azure_client.subscription_in_credentials.post_method_global_valid()
    await azure_client.subscription_in_credentials.post_path_global_valid()
    await azure_client.subscription_in_credentials.post_swagger_global_valid()


@pytest.mark.asyncio
async def test_subscription_in_method(azure_client, valid_subscription):
    await azure_client.subscription_in_method.post_method_local_valid(valid_subscription)
    await azure_client.subscription_in_method.post_path_local_valid(valid_subscription)
    await azure_client.subscription_in_method.post_swagger_local_valid(valid_subscription)
    with pytest.raises(ValueError):
        await azure_client.subscription_in_method.post_method_local_null(None)


@pytest.mark.asyncio
async def test_api_version_default(azure_client):
    await azure_client.api_version_default.get_method_global_not_provided_valid()
    await azure_client.api_version_default.get_method_global_valid()
    await azure_client.api_version_default.get_path_global_valid()
    await azure_client.api_version_default.get_swagger_global_valid()


@pytest.mark.asyncio
async def test_api_version_local(azure_client):
    await azure_client.api_version_local.get_method_local_valid()
    await azure_client.api_version_local.get_method_local_null()
    await azure_client.api_version_local.get_path_local_valid()
    await azure_client.api_version_local.get_swagger_local_valid()


@pytest.mark.asyncio
async def test_skip_url_encoding(azure_client, unencoded_path, unencoded_query):
    await azure_client.skip_url_encoding.get_method_path_valid(unencoded_path)
    await azure_client.skip_url_encoding.get_path_valid(unencoded_path)
    await azure_client.skip_url_encoding.get_swagger_path_valid()
    await azure_client.skip_url_encoding.get_method_query_valid(q1=unencoded_query)
    await azure_client.skip_url_encoding.get_path_query_valid(q1=unencoded_query)
    await azure_client.skip_url_encoding.get_swagger_query_valid()
    await azure_client.skip_url_encoding.get_method_query_null()
    await azure_client.skip_url_encoding.get_method_query_null(q1=None)


@pytest.mark.asyncio
async def test_azure_odata(azure_client):
    await azure_client.odata.get_with_filter(filter="id gt 5 and name eq 'foo'", top=10, orderby="id")


@pytest.mark.asyncio
async def test_group_with_constant(client):
    await client.parameter_grouping.group_with_constant(grouped_constant="foo", grouped_parameter="bar")
