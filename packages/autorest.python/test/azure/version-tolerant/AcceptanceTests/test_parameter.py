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

from azureparametergroupingversiontolerant import AutoRestParameterGroupingTestService
from azurespecialpropertiesversiontolerant import AutoRestAzureSpecialParametersTestClient

from azure.core.exceptions import HttpResponseError
import pytest

@pytest.fixture
def client():
    with AutoRestParameterGroupingTestService() as client:
        yield client

@pytest.fixture
def valid_subscription():
    return '1234-5678-9012-3456'

@pytest.fixture
def azure_client(valid_subscription, credential, authentication_policy):
    with AutoRestAzureSpecialParametersTestClient(credential, valid_subscription, authentication_policy=authentication_policy) as client:
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


def test_post_all_required_parameters(client, body_parameter, header_parameter, query_parameter, path_parameter):
    client.parameter_grouping.post_required(
        path_parameter,
        body_parameter,
        query=query_parameter,
        custom_header=header_parameter,
    )

def test_post_required_parameters_null_optional_parameters(client, body_parameter, path_parameter):
    client.parameter_grouping.post_required(
        path_parameter,
        body_parameter,
        query=None
    )

def test_post_required_parameters_with_null_required_property(client, path_parameter):

    with pytest.raises(HttpResponseError):
        # supposed to raise a validation error, but since we don't validate, we get a service error instead
        client.parameter_grouping.post_required(path_parameter, body=None)
    with pytest.raises(TypeError):
        client.parameter_grouping.post_required()

def test_post_all_optional(client, header_parameter, query_parameter):
    client.parameter_grouping.post_optional(
        custom_header=header_parameter,
        query=query_parameter,
    )

def test_post_none_optional(client):
    client.parameter_grouping.post_optional(query=None)

def test_post_all_multi_param_groups(client, header_parameter, query_parameter):
    client.parameter_grouping.post_multi_param_groups(
        header_one=header_parameter,
        query_one=query_parameter,
        header_two="header2",
        query_two=42,
    )

def test_post_some_multi_param_groups(client, header_parameter):
    client.parameter_grouping.post_multi_param_groups(
        header_one=header_parameter,
        query_two=42,
    )

def test_post_shared_parameter_group_object(client, header_parameter):
    client.parameter_grouping.post_shared_parameter_group_object(header_one=header_parameter)

def test_post_reserved_words(client):
    client.parameter_grouping.post_reserved_words(from_parameter="bob", accept_parameter="yes")

def test_subscription_in_credentials(azure_client):
    # valid_api_version = '2.0'
    azure_client.subscription_in_credentials.post_method_global_not_provided_valid()
    azure_client.subscription_in_credentials.post_method_global_valid()
    azure_client.subscription_in_credentials.post_path_global_valid()
    azure_client.subscription_in_credentials.post_swagger_global_valid()

def test_subscription_in_method(azure_client, valid_subscription):
    azure_client.subscription_in_method.post_method_local_valid(valid_subscription)
    azure_client.subscription_in_method.post_path_local_valid(valid_subscription)
    azure_client.subscription_in_method.post_swagger_local_valid(valid_subscription)
    with pytest.raises(ValueError):
        azure_client.subscription_in_method.post_method_local_null(None)

def test_api_version_default(azure_client):
    azure_client.api_version_default.get_method_global_not_provided_valid()
    azure_client.api_version_default.get_method_global_valid()
    azure_client.api_version_default.get_path_global_valid()
    azure_client.api_version_default.get_swagger_global_valid()

def test_api_version_local(azure_client):
    azure_client.api_version_local.get_method_local_valid()
    azure_client.api_version_local.get_method_local_null()
    azure_client.api_version_local.get_path_local_valid()
    azure_client.api_version_local.get_swagger_local_valid()

def test_skip_url_encoding(azure_client, unencoded_path, unencoded_query):
    azure_client.skip_url_encoding.get_method_path_valid(unencoded_path)
    azure_client.skip_url_encoding.get_path_valid(unencoded_path)
    azure_client.skip_url_encoding.get_swagger_path_valid()
    azure_client.skip_url_encoding.get_method_query_valid(q1=unencoded_query)
    azure_client.skip_url_encoding.get_path_query_valid(q1=unencoded_query)
    azure_client.skip_url_encoding.get_swagger_query_valid()
    azure_client.skip_url_encoding.get_method_query_null()
    azure_client.skip_url_encoding.get_method_query_null(q1=None)

def test_azure_odata(azure_client):
    azure_client.odata.get_with_filter(filter="id gt 5 and name eq 'foo'", top=10, orderby="id")

def test_group_with_constant(client):
    client.parameter_grouping.group_with_constant(grouped_constant="foo", grouped_parameter="bar")
