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

import time

from azure.core.exceptions import DecodeError, HttpResponseError
from azure.core.pipeline.policies import ContentDecodePolicy, RetryPolicy, HeadersPolicy, RequestIdPolicy
from azure.core.rest import HttpRequest
from azure.mgmt.core.polling.arm_polling import ARMPolling

from lrolowlevel import AutoRestLongRunningOperationTestService
from lrolowlevel.rest import lr_os_custom_header, lro_retrys, lros, lrosads
from azure.core.polling import LROPoller, NoPolling

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

import pytest

POLLING_INTERVAL = 0

class AutorestTestARMPolling(ARMPolling):

    def _polling_cookie(self, response):
        """Collect retry cookie - we only want to do this for the test server
        at this point, unless we implement a proper cookie policy.

        :returns: Dictionary containing a cookie header if required,
         otherwise an empty dictionary.
        """
        parsed_url = urlparse(response.request.url)
        host = parsed_url.hostname.strip('.')
        if host == 'localhost':
            return {'cookie': response.headers.get('set-cookie', '')}
        return {}

    def request_status(self, status_link):
        request = self._client.get(status_link, headers=self._polling_cookie(self._pipeline_response.http_response))
        # ARM requires to re-inject 'x-ms-client-request-id' while polling
        if 'request_id' not in self._operation_config:
            self._operation_config['request_id'] = self._get_request_id()
        return self._client._pipeline.run(request, stream=False, **self._operation_config)

@pytest.fixture()
def client(cookie_policy, credential):
    """Create a AutoRestLongRunningOperationTestService client with test server credentials."""
    policies = [
        RequestIdPolicy(),
        HeadersPolicy(),
        ContentDecodePolicy(),
        RetryPolicy(),
        cookie_policy
    ]

    with AutoRestLongRunningOperationTestService(credential=credential, policies=policies, polling_interval=POLLING_INTERVAL) as client:
        yield client

@pytest.fixture()
def product():
    return {"location": "West US"}

@pytest.fixture()
def custom_headers():
    return {"x-ms-client-request-id": '9C4D50EE-2D56-4CD3-8152-34347DC9F2B0'}

def lro_result(func, *args, **kwargs):
    if "polling" not in kwargs:
        kwargs["polling"] = AutorestTestARMPolling(0)
    return func(*args, **kwargs).result()

@pytest.fixture
def get_long_running_output(deserializer):
    # this is the default deserializer, just returns deserialized object
    def _callback(pipeline_response):
        return deserializer("object", pipeline_response.http_response)
    return _callback

@pytest.fixture
def get_long_running_output_return_none():
    # for use if the swagger has no defined return object, so we
    # follow the convenience layer, and just return none
    def _callback(pipeline_response):
        return None
    return _callback

@pytest.fixture
def get_poller(get_long_running_output, client):

    def _callback(request, **kwargs):
        pipeline_response = client.send_request(
            request,
            _return_pipeline_response=True
        )
        pipeline_response.http_response.raise_for_status()
        polling = kwargs.pop("polling", True)
        deserializer = kwargs.pop("get_long_running_output", get_long_running_output)
        polling_method = kwargs.pop("polling_method", None)
        if not polling_method:
            polling_method = AutorestTestARMPolling(kwargs.pop("polling_interval", 0)) if polling else NoPolling()
        return LROPoller(client._client, pipeline_response, deserializer, polling_method)
    return _callback

def _check_message_in_error(ex, message):
    try:
        assert ex.value.message.lower() == message.lower()
    except AssertionError:
        assert message.lower() in ex.value.message.lower()

@pytest.fixture
def assert_polling_raises_with_message(get_poller):
    def _callback(request, message, **kwargs):
        poller = get_poller(request, **kwargs)
        with pytest.raises(HttpResponseError) as ex:
            poller.result()
        _check_message_in_error(ex, message)
    return _callback

@pytest.fixture
def assert_initial_call_raises_with_message(get_poller):
    def _callback(request, message, **kwargs):
        with pytest.raises(HttpResponseError) as ex:
            get_poller(request, **kwargs)  # this makes the initial call
        _check_message_in_error(ex, message)
    return _callback

def test_post_double_headers_final_continuation_token(client, get_poller, get_long_running_output):
    request = lros.build_post_double_headers_final_location_get_request()

    poller = get_poller(request)
    continuation_token = poller.continuation_token()

    poller = LROPoller.from_continuation_token(
        polling_method=ARMPolling(0),
        continuation_token=continuation_token,
        client=client._client,
        deserialization_callback=get_long_running_output,
    )
    product = poller.result()
    assert product['id'] == "100"

def test_post_double_headers_final(get_poller):
    request = lros.build_post_double_headers_final_location_get_request()
    poller = get_poller(request)
    product = poller.result()
    assert product['id'] == "100"

    request = lros.build_post_double_headers_final_azure_header_get_request()
    polling_method = AutorestTestARMPolling(0, lro_options={"final-state-via": "azure-async-operation"})
    product = get_poller(request, polling_method=polling_method).result()
    assert product['id'] == "100"

def test_post_double_headers_default(get_poller):
    # This test will work as long as the default is Location
    request = lros.build_post_double_headers_final_azure_header_get_default_request()
    product = get_poller(request).result()
    assert product['id'] == "100"

def test_happy_put201_creating_succeeded200(get_poller):
    request = lros.build_put201_creating_succeeded200_request()
    process = get_poller(request).result()
    assert "Succeeded" == process['properties']['provisioningState']

    # Testing nopolling
    request = lros.build_put201_creating_succeeded200_request()
    process = get_poller(request, polling=False).result()
    assert "Creating" == process['properties']['provisioningState']

def test_happy_put201_creating_failed200(assert_polling_raises_with_message, get_poller):
    request = lros.build_put201_creating_failed200_request()
    assert_polling_raises_with_message(request, "Operation returned an invalid status 'OK'")

    request = lros.build_put201_creating_failed200_request()
    process = get_poller(request, polling=False).result()
    assert "Created" == process['properties']['provisioningState']

def test_happy_put200_updating_succeeded204(get_poller):
    request = lros.build_put200_updating_succeeded204_request()
    process = get_poller(request).result()
    assert "Succeeded" == process['properties']['provisioningState']

    process = get_poller(request, polling=False).result()
    assert "Updating" == process['properties']['provisioningState']

def test_happy_put200_acceptedcanceled200(get_poller, assert_polling_raises_with_message):
    request = lros.build_put200_acceptedcanceled200_request()
    assert_polling_raises_with_message(request, "Operation returned an invalid status 'OK'")

    request = lros.build_put200_acceptedcanceled200_request()
    process = get_poller(request, polling=False).result()
    assert "Accepted" == process['properties']['provisioningState']

def test_happy_put_no_header_in_retry(get_poller):
    request = lros.build_put_no_header_in_retry_request()
    process = get_poller(request).result()
    assert "Succeeded" == process['properties']['provisioningState']

    request = lros.build_put_async_no_header_in_retry_request()
    process = get_poller(request).result()
    assert "Succeeded" == process['properties']['provisioningState']

def test_happy_put_sub_resource(get_poller):
    request = lros.build_put_sub_resource_request()
    process = get_poller(request).result()
    assert "Succeeded" == process['properties']['provisioningState']

    request = lros.build_put_async_sub_resource_request()
    process = get_poller(request).result()
    assert "Succeeded" == process['properties']['provisioningState']

def test_happy_put_non_resource(get_poller):
    request = lros.build_put_non_resource_request()
    process = get_poller(request).result()
    assert "100" == process['id']

    request = lros.build_put_async_non_resource_request()
    process = get_poller(request).result()
    assert "100" == process['id']

def test_happy_put200_succeeded(get_poller):
    request = lros.build_put200_succeeded_request()
    process = get_poller(request).result()
    assert "Succeeded" == process['properties']['provisioningState']

    request = lros.build_put200_succeeded_no_state_request()
    process = get_poller(request).result()
    assert "100" == process['id']

def test_put201_succeeded(get_poller):
    request = lros.build_put201_succeeded_request()
    process = get_poller(request).result()

    assert "Succeeded" == process['properties']['provisioningState']
    assert "100" == process['id']
    assert "foo" == process['name']

def test_happy_put202_retry200(get_poller):
    request = lros.build_put202_retry200_request()
    process = get_poller(request).result()
    assert "100" == process['id']

def test_happy_put_retry_succeeded(get_poller):
    request = lros.build_put_async_retry_succeeded_request()
    process = get_poller(request).result()
    assert "Succeeded" == process['properties']['provisioningState']

    request = lros.build_put_async_no_retry_succeeded_request()
    process = get_poller(request).result()
    assert "Succeeded" == process['properties']['provisioningState']

def test_happy_put_retry_failed_canceled(get_poller, assert_polling_raises_with_message):
    request = lros.build_put_async_retry_failed_request()
    assert_polling_raises_with_message(request, "Operation returned an invalid status 'OK'")

    request = lros.build_put_async_no_retrycanceled_request()
    assert_polling_raises_with_message(request, "Operation returned an invalid status 'OK'")

def test_post202_retry200(get_poller, get_long_running_output_return_none):
    request = lros.build_post202_retry200_request()
    process = get_poller(request, get_long_running_output=get_long_running_output_return_none).result()
    assert process is None

def test_happy_delete(get_poller):
    request = lros.build_delete204_succeeded_request()
    assert get_poller(request).result() is None

    request = lros.build_delete202_retry200_request()
    assert get_poller(request).result() is None

    request = lros.build_delete202_no_retry204_request()
    assert get_poller(request).result() is None

def test_happy_delete_no_header_in_retry(get_poller, get_long_running_output_return_none):
    request = lros.build_delete_no_header_in_retry_request()
    assert get_poller(request).result() is None

    request = lros.build_delete_async_no_header_in_retry_request()
    assert get_poller(request, get_long_running_output=get_long_running_output_return_none).result() is None

def test_happy_delete_async_retry_failed_canceled(assert_polling_raises_with_message):
    request = lros.build_delete_async_retrycanceled_request()
    assert_polling_raises_with_message(request, "Operation returned an invalid status 'OK'")

    request = lros.build_delete_async_retry_failed_request()
    assert_polling_raises_with_message(request, "Operation returned an invalid status 'OK'")

def test_happy_delete_async_succeeded(get_poller, get_long_running_output_return_none):
    request = lros.build_delete_async_no_retry_succeeded_request()
    assert get_poller(request, get_long_running_output=get_long_running_output_return_none).result() is None

    request = lros.build_delete_async_retry_succeeded_request()
    assert get_poller(request, get_long_running_output=get_long_running_output_return_none).result() is None

def test_happy_delete_provisioning(get_poller):
    request = lros.build_delete_provisioning202_accepted200_succeeded_request()
    process = get_poller(request).result()
    assert "Succeeded" == process['properties']['provisioningState']

    request = lros.build_delete_provisioning202_deletingcanceled200_request()
    result = get_poller(request).result()
    assert result['properties']['provisioningState'] == 'Canceled'

    request = lros.build_delete_provisioning202_deleting_failed200_request()
    result = get_poller(request).result()
    assert result['properties']['provisioningState'] == 'Failed'

def test_happy_post(get_poller):
    request = lros.build_post202_no_retry204_request()
    assert get_poller(request).result() is None

    request = lros.build_post200_with_payload_request()

    sku = get_poller(request).result()
    assert sku['id'] == '1'

def test_happy_post_async_retry_failed_canceled(assert_polling_raises_with_message):
    request = lros.build_post_async_retry_failed_request()
    assert_polling_raises_with_message(request, "Internal Server Error")

    request = lros.build_post_async_retrycanceled_request()
    assert_polling_raises_with_message(request, "Operation returned an invalid status 'OK'")

def test_happy_post_async_succeeded(get_poller):
    request = lros.build_post_async_retry_succeeded_request()
    prod = get_poller(request).result()
    assert prod['id'] == "100"

    request = lros.build_post_async_no_retry_succeeded_request()
    prod = get_poller(request).result()
    assert prod['id'] == "100"

def test_retrys_put(get_poller):
    request = lro_retrys.build_put201_creating_succeeded200_request()
    process = get_poller(request).result()
    assert 'Succeeded' == process['properties']['provisioningState']

    request = lro_retrys.build_put_async_relative_retry_succeeded_request()
    process = get_poller(request).result()
    assert 'Succeeded' == process['properties']['provisioningState']

def test_retrys_delete(get_poller, get_long_running_output_return_none):
    request = lro_retrys.build_delete_provisioning202_accepted200_succeeded_request()
    process = get_poller(request).result()
    assert 'Succeeded' == process['properties']['provisioningState']

    request = lro_retrys.build_delete202_retry200_request()
    assert get_poller(request, get_long_running_output=get_long_running_output_return_none).result() is None

    request = lro_retrys.build_delete_async_relative_retry_succeeded_request()
    assert get_poller(request, get_long_running_output=get_long_running_output_return_none).result() is None

def test_retrys_post(get_poller, get_long_running_output_return_none):
    request = lro_retrys.build_post202_retry200_request()
    assert get_poller(request, get_long_running_output=get_long_running_output_return_none).result() is None

    request = lro_retrys.build_post_async_relative_retry_succeeded_request()
    assert get_poller(request, get_long_running_output=get_long_running_output_return_none).result() is None

@pytest.mark.skip(reason="https://github.com/Azure/azure-sdk-for-python/issues/17757")
def test_custom_headers_put_async_retry_succeeded(get_poller, custom_headers):
    request = lr_os_custom_header.build_put_async_retry_succeeded_request(headers=custom_headers)
    assert get_poller(request).result() is not None

@pytest.mark.skip(reason="https://github.com/Azure/azure-sdk-for-python/issues/17757")
def test_custom_headers_post_async_retry_succeeded(get_poller, custom_headers):
    request = lr_os_custom_header.build_post_async_retry_succeeded_request(headers=custom_headers)
    assert get_poller(request).result() is None

@pytest.mark.skip(reason="https://github.com/Azure/azure-sdk-for-python/issues/17757")
def test_custom_headers_put201_creating_succeeded200(get_poller, custom_headers):
    request = lr_os_custom_header.build_put201_creating_succeeded200_request(headers=custom_headers)
    assert get_poller(request).result() is not None

@pytest.mark.skip(reason="https://github.com/Azure/azure-sdk-for-python/issues/17757")
def test_custom_headers_post202_retry200(get_poller, custom_headers):
    request = lr_os_custom_header.build_post202_retry200_request(headers=custom_headers)
    assert get_poller(request).result() is None

def test_sads_put_non_retry(assert_initial_call_raises_with_message, assert_polling_raises_with_message):
    request = lrosads.build_put_non_retry400_request()
    assert_initial_call_raises_with_message(request, "Bad Request")

    request = lrosads.build_put_non_retry201_creating400_request()
    assert_polling_raises_with_message(request, "Error from the server")

def test_sads_put_async_relative(assert_polling_raises_with_message):
    request = lrosads.build_put_async_relative_retry400_request()
    assert_polling_raises_with_message(request, "Operation returned an invalid status 'Bad Request'")

    request = lrosads.build_put_async_relative_retry_no_status_request()
    assert_polling_raises_with_message(request, "no status found in body")

    request = lrosads.build_put_async_relative_retry_no_status_payload_request()
    assert_polling_raises_with_message(request, "The response from long running operation does not contain a body.")

def test_sads_put_error201_no_provisioning_state_payload(assert_polling_raises_with_message):
    request = lrosads.build_put_error201_no_provisioning_state_payload_request()
    assert_polling_raises_with_message(request, "The response from long running operation does not contain a body.")

def test_sads_put200_invalid_json_with_exception(get_poller):
    request = lrosads.build_put200_invalid_json_request()
    with pytest.raises(DecodeError):
        get_poller(request).wait()

@pytest.mark.skip(reason="The reason this fails is bc the convenience layer fails in deserializing the response headers. LLC doesn't do that, so skipping")
def test_sads_put_async_relative_with_exception(get_poller):
    request = lrosads.build_put_async_relative_retry_invalid_json_polling_request()
    with pytest.raises(DecodeError):
        get_poller(request).wait()

    request = lrosads.build_put_async_relative_retry_invalid_header_request()
    with pytest.raises(Exception):
        get_poller(request).wait()

def test_sads_put_non_retry201_creating400_invalid_json_with_exception(get_poller):
    request = lrosads.build_put_non_retry201_creating400_invalid_json_request()
    with pytest.raises(DecodeError):
        get_poller(request).wait()

def tests_lro_sads_delete_non_retry(assert_initial_call_raises_with_message, assert_polling_raises_with_message):
    request = lrosads.build_delete_non_retry400_request()
    assert_initial_call_raises_with_message(request, "Bad Request")

    request = lrosads.build_delete202_non_retry400_request()
    assert_polling_raises_with_message(request, "Bad Request")

def test_sads_delete_async_relative(assert_polling_raises_with_message):
    request = lrosads.build_delete_async_relative_retry400_request()
    assert_polling_raises_with_message(request, "Bad Request")

    request = lrosads.build_delete_async_relative_retry_no_status_request()
    assert_polling_raises_with_message(request, "no status found in body")

def test_sads_delete204_succeeded(get_poller):
    request = lrosads.build_delete204_succeeded_request()
    get_poller(request).wait()

@pytest.mark.skip(reason="The reason this fails is bc the convenience layer fails in deserializing the retry-after header /bar as an int. LLC doesn't do that, so skipping")
def test_sads_delete_async_relative_with_exception(get_poller):
    request = lrosads.build_delete_async_relative_retry_invalid_header_request()
    with pytest.raises(Exception):
        get_poller(request).wait()

    request = lrosads.build_delete_async_relative_retry_invalid_json_polling_request()
    with pytest.raises(DecodeError):
        get_poller(request).wait()

@pytest.mark.skip(reason="The reason this fails is bc the convenience layer fails in deserializing the retry-after header /bar as an int. LLC doesn't do that, so skipping")
def test_sads_delete202_retry_invalid_header_with_exception(get_poller):
    request = lrosads.build_delete202_retry_invalid_header_request()
    with pytest.raises(Exception):
        get_poller(request).wait()

def test_sads_post_non_retry(assert_initial_call_raises_with_message, assert_polling_raises_with_message):
    request = lrosads.build_post_non_retry400_request()
    assert_initial_call_raises_with_message(request, "Bad Request")

    request = lrosads.build_post202_non_retry400_request()
    assert_polling_raises_with_message(request, "Bad Request")

def test_sads_post_async_relative(assert_polling_raises_with_message):
    request = lrosads.build_post_async_relative_retry400_request()
    assert_polling_raises_with_message(request, "Bad Request")

    request = lrosads.build_post_async_relative_retry_no_payload_request()
    assert_polling_raises_with_message(request, "The response from long running operation does not contain a body.")

def test_sads_post202_no_location(get_poller):
    # Testserver wants us to fail (coverage name is LROErrorPostNoLocation)
    # Actually, Python will NOT, and consider any kind of success 2xx on the initial call
    # is an actual success
    request = lrosads.build_post202_no_location_request()
    process = get_poller(request).result()
    assert process is None

@pytest.mark.skip(reason="The reason this fails is bc the convenience layer fails in deserializing the retry-after header /bar as an int. LLC doesn't do that, so skipping")
def test_sads_post_async_relative_with_exception(get_poller):
    request = lrosads.build_post_async_relative_retry_invalid_header_request()
    with pytest.raises(Exception):
        get_poller(request).wait()

    request = lrosads.build_post_async_relative_retry_invalid_json_polling_request()

    with pytest.raises(DecodeError):
        get_poller(request).wait()

@pytest.mark.skip(reason="The reason this fails is bc the convenience layer fails in deserializing the retry-after header /bar as an int. LLC doesn't do that, so skipping")
def test_post202_retry_invalid_header_with_exception(get_poller):
    request = lrosads.build_post202_retry_invalid_header_request()
    with pytest.raises(Exception):
        get_poller(request).wait()

def test_polling_interval_operation(get_poller):
    default_polling_interval_start_time = time.time()
    request = lros.build_post_double_headers_final_azure_header_get_default_request()
    product1 = get_poller(request).result()
    default_polling_interval_duration = time.time() - default_polling_interval_start_time
    assert abs(default_polling_interval_duration - 0) < 0.1

    one_second_polling_interval_start_time = time.time()
    request = lros.build_post_double_headers_final_azure_header_get_default_request()

    product2 = get_poller(request, polling_interval=1).result()
    one_second_polling_interval_duration = time.time() - one_second_polling_interval_start_time
    assert abs(one_second_polling_interval_duration - 1) < 0.1

    assert product1 == product2

def test_passing_kwargs(get_poller):
    request = lros.build_put200_succeeded_request(headers={"Content-Type": "application/json"})
    process = get_poller(request).result()
    assert "Succeeded" == process['properties']['provisioningState']

def test_lro_list(get_poller):
    request = lros.build_post202_list_request()
    products = get_poller(request).result()
    assert len(products) == 1
    product = products[0]
    assert product['id'] == "100"
    assert product['name'] == "foo"

