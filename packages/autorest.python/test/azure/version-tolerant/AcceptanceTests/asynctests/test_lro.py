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
from azure.core.rest import HttpRequest
from async_generator import yield_, async_generator
import time

from azure.core.exceptions import DecodeError, HttpResponseError
from azure.core.pipeline.policies import ContentDecodePolicy, AsyncRetryPolicy, HeadersPolicy, RequestIdPolicy

from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from lroversiontolerant.aio import AutoRestLongRunningOperationTestService


try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

import pytest

POLLING_INTERVAL = 0

class AutorestTestARMPolling(AsyncARMPolling):

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

    async def request_status(self, status_link):

        request = HttpRequest("GET", status_link, headers=self._polling_cookie(self._pipeline_response.http_response))
        # ARM requires to re-inject 'x-ms-client-request-id' while polling
        if 'request_id' not in self._operation_config:
            self._operation_config['request_id'] = self._get_request_id()
        return (await self._client._pipeline.run(request, stream=False, **self._operation_config))

@pytest.fixture
@async_generator
async def client(cookie_policy, credential):
    """Create a AutoRestLongRunningOperationTestService client with test server credentials."""
    policies = [
        RequestIdPolicy(),
        HeadersPolicy(),
        ContentDecodePolicy(),
        AsyncRetryPolicy(),
        cookie_policy
    ]
    async with AutoRestLongRunningOperationTestService(credential=credential, policies=policies, polling_interval=POLLING_INTERVAL) as client:
        await yield_(client)


@pytest.fixture()
def product():
    return {"location": "West US"}

@pytest.fixture()
def custom_headers():
    return {"x-ms-client-request-id": '9C4D50EE-2D56-4CD3-8152-34347DC9F2B0'}

async def assert_raises_with_message(msg, func, *args, **kwargs):
    try:
        await lro_result(func, *args, **kwargs)
        pytest.fail("HttpResponseError wasn't raised as expected")

    except HttpResponseError as err:
        assert err.response is not None
        print("BODY: "+err.response.text())

        try:
            msg, internal_msg = msg
        except ValueError:
            internal_msg = None

        # Autorest testserver doesn't respect ARM spec
        # The point of this file is NOT to test if LRO return
        # type are compatible with ARM spec.
        # So, we hack a little the system and check if we have the expected
        # message in the JSON body.
        # We should have more testserver on valid ARM errors....
        assert msg.lower() in err.message.lower()
        if internal_msg:
            assert internal_msg in str(err.inner_exception)

async def lro_result(func, *args, **kwargs):
    if "polling" not in kwargs:
        AutorestTestARMPolling.__name__ = "AsyncARMPolling"
        kwargs["polling"] = AutorestTestARMPolling(0)
    return await (await func(*args, **kwargs)).result()

@pytest.mark.asyncio
async def test_post_double_headers_final(client):
    poller = await client.lros.begin_post_double_headers_final_location_get()
    continuation_token = poller.continuation_token()

    poller = await client.lros.begin_post_double_headers_final_location_get(continuation_token=continuation_token)
    product = await poller.result()
    assert product["id"] == "100"

@pytest.mark.asyncio
async def test_post_double_headers_default(client):
    # This test will work as long as the default is Location
    poller = await client.lros.begin_post_double_headers_final_azure_header_get_default()
    product = await poller.result()
    assert product["id"] == "100"

@pytest.mark.asyncio
async def test_happy_put201_creating_succeeded200(client, product):
    process = await lro_result(client.lros.begin_put201_creating_succeeded200, product)
    assert "Succeeded" == process['properties']['provisioningState']

    # Testing nopolling
    process = await lro_result(client.lros.begin_put201_creating_succeeded200, product, polling=False)
    assert "Creating" == process['properties']['provisioningState']

@pytest.mark.asyncio
async def test_happy_put201_creating_failed200(client, product):
    await assert_raises_with_message(
        ("Operation returned an invalid status 'OK'", "failed"),
        client.lros.begin_put201_creating_failed200, product)

    process = await lro_result(client.lros.begin_put201_creating_failed200, product, polling=False)
    assert "Created" == process['properties']['provisioningState']

@pytest.mark.asyncio
async def test_happy_put200_updating_succeeded204(client, product):
    process = await lro_result(client.lros.begin_put200_updating_succeeded204, product)
    assert "Succeeded" == process['properties']['provisioningState']

    process = await lro_result(client.lros.begin_put200_updating_succeeded204, product, polling=False)
    assert "Updating" == process['properties']['provisioningState']

@pytest.mark.asyncio
async def test_happy_put200_acceptedcanceled200(client, product):
    await assert_raises_with_message(
        ("Operation returned an invalid status 'OK'", "canceled"),
        client.lros.begin_put200_acceptedcanceled200, product)

    process = await lro_result(client.lros.begin_put200_acceptedcanceled200, product, polling=False)
    assert "Accepted" == process['properties']['provisioningState']

@pytest.mark.asyncio
async def test_happy_put_no_header_in_retry(client, product):
    process = await lro_result(client.lros.begin_put_no_header_in_retry, product)
    assert "Succeeded" == process['properties']['provisioningState']

    process = await lro_result(client.lros.begin_put_async_no_header_in_retry, product)
    assert "Succeeded" == process['properties']['provisioningState']

@pytest.mark.asyncio
async def test_happy_put_sub_resource(client):
    process = await lro_result(client.lros.begin_put_sub_resource, {})
    assert "Succeeded" == process['properties']['provisioningState']

    process = await lro_result(client.lros.begin_put_async_sub_resource, {})
    assert "Succeeded" == process['properties']['provisioningState']

@pytest.mark.asyncio
async def test_happy_put_non_resource(client):
    process = await lro_result(client.lros.begin_put_non_resource, {})
    assert "100" == process["id"]

    process = await lro_result(client.lros.begin_put_async_non_resource, {})
    assert "100" == process["id"]

@pytest.mark.asyncio
async def test_happy_put200_succeeded(client, product):
    process = await lro_result(client.lros.begin_put200_succeeded, product)
    assert "Succeeded" == process['properties']['provisioningState']

    process = await lro_result(client.lros.begin_put200_succeeded_no_state, product)
    assert "100" == process["id"]

@pytest.mark.asyncio
async def test_put201_succeeded(client, product):
    process = await lro_result(client.lros.begin_put201_succeeded, product)

    assert "Succeeded" == process['properties']['provisioningState']
    assert "100" == process["id"]
    assert "foo" == process["name"]

@pytest.mark.asyncio
async def test_happy_put202_retry200(client, product):
    process = await lro_result(client.lros.begin_put202_retry200, product)
    assert "100" == process["id"]

@pytest.mark.asyncio
async def test_happy_put_retry_succeeded(client, product):
    process = await lro_result(client.lros.begin_put_async_retry_succeeded, product)
    assert "Succeeded" == process['properties']['provisioningState']

    process = await lro_result(client.lros.begin_put_async_no_retry_succeeded, product)
    assert "Succeeded" == process['properties']['provisioningState']

@pytest.mark.asyncio
async def test_happy_put_retry_failed_canceled(client, product):
    await assert_raises_with_message(
        ("Operation returned an invalid status 'OK'", "failed"),
        client.lros.begin_put_async_retry_failed, product)

    await assert_raises_with_message(
        ("Operation returned an invalid status 'OK'", "canceled"),
        client.lros.begin_put_async_no_retrycanceled, product)

@pytest.mark.asyncio
async def test_post202_retry200(client, product):
    process = await lro_result(client.lros.begin_post202_retry200, product)
    assert process is None

@pytest.mark.asyncio
async def test_happy_delete(client):
    assert await lro_result(client.lros.begin_delete204_succeeded) is None
    assert await lro_result(client.lros.begin_delete202_retry200) is None
    assert await lro_result(client.lros.begin_delete202_no_retry204) is None

@pytest.mark.asyncio
async def test_happy_delete_no_header_in_retry(client):
    assert await lro_result(client.lros.begin_delete_no_header_in_retry) is None
    assert await lro_result(client.lros.begin_delete_async_no_header_in_retry) is None

@pytest.mark.asyncio
async def test_happy_delete_async_retry_failed_canceled(client):
    await assert_raises_with_message(
        ("Operation returned an invalid status 'OK'", "canceled"),
        client.lros.begin_delete_async_retrycanceled)

    await assert_raises_with_message(
        ("Operation returned an invalid status 'OK'", "failed"),
        client.lros.begin_delete_async_retry_failed)

@pytest.mark.asyncio
async def test_happy_delete_async_succeeded(client):
    assert await lro_result(client.lros.begin_delete_async_no_retry_succeeded) is None
    assert await lro_result(client.lros.begin_delete_async_retry_succeeded) is None

@pytest.mark.asyncio
async def test_happy_delete_provisioning(client):
    process = await lro_result(client.lros.begin_delete_provisioning202_accepted200_succeeded)
    assert "Succeeded" == process['properties']['provisioningState']

    result = await lro_result(client.lros.begin_delete_provisioning202_deletingcanceled200)
    assert result['properties']['provisioningState'] == 'Canceled'

    result = await lro_result(client.lros.begin_delete_provisioning202_deleting_failed200)
    assert result['properties']['provisioningState'] == 'Failed'

@pytest.mark.asyncio
async def test_happy_post(client, product):
    assert await lro_result(client.lros.begin_post202_no_retry204, product) is None

    sku = await lro_result(client.lros.begin_post200_with_payload)
    assert sku["id"] == '1'

@pytest.mark.asyncio
async def test_happy_post_async_retry_failed_canceled(client, product):
    await assert_raises_with_message("Internal Server Error",
        client.lros.begin_post_async_retry_failed)

    await assert_raises_with_message(
        ("Operation returned an invalid status 'OK'", "canceled"),
        client.lros.begin_post_async_retrycanceled)

@pytest.mark.asyncio
async def test_happy_post_async_succeeded(client, product):
    prod = await lro_result(client.lros.begin_post_async_retry_succeeded)
    assert prod["id"] == "100"

    prod = await lro_result(client.lros.begin_post_async_no_retry_succeeded)
    assert prod["id"] == "100"

@pytest.mark.asyncio
async def test_retrys_put(client, product):
    process = await lro_result(client.lro_retrys.begin_put201_creating_succeeded200, product)
    assert 'Succeeded' == process['properties']['provisioningState']

    process = await lro_result(client.lro_retrys.begin_put_async_relative_retry_succeeded, product)
    assert 'Succeeded' == process['properties']['provisioningState']

@pytest.mark.asyncio
async def test_retrys_delete(client, product):
    process = await lro_result(client.lro_retrys.begin_delete_provisioning202_accepted200_succeeded)
    assert 'Succeeded' == process['properties']['provisioningState']

    assert await lro_result(client.lro_retrys.begin_delete202_retry200) is None
    assert await lro_result(client.lro_retrys.begin_delete_async_relative_retry_succeeded) is None

@pytest.mark.asyncio
async def test_retrys_post(client, product):
    assert await lro_result(client.lro_retrys.begin_post202_retry200, product) is None
    assert await lro_result(client.lro_retrys.begin_post_async_relative_retry_succeeded, product) is None

@pytest.mark.asyncio
async def test_custom_headers_put_async_retry_succeeded(client, product, custom_headers):
    process = await lro_result(client.lr_os_custom_header.begin_put_async_retry_succeeded, product, headers=custom_headers)
    assert process is not None

@pytest.mark.asyncio
async def test_custom_headers_post_async_retry_succeeded(client, product, custom_headers):
    process = await lro_result(client.lr_os_custom_header.begin_post_async_retry_succeeded, product, headers=custom_headers)
    assert process is None

@pytest.mark.asyncio
async def test_custom_headers_put201_creating_succeeded200(client, product, custom_headers):
    process = await lro_result(client.lr_os_custom_header.begin_put201_creating_succeeded200, product, headers=custom_headers)
    assert process is not None

@pytest.mark.asyncio
async def test_custom_headers_post202_retry200(client, product, custom_headers):
    process = await lro_result(client.lr_os_custom_header.begin_post202_retry200, product, headers=custom_headers)
    assert process is None

@pytest.mark.asyncio
async def test_sads_put_non_retry(client, product):
    await assert_raises_with_message("Bad Request",
        client.lrosads.begin_put_non_retry400, product)

    await assert_raises_with_message("Error from the server",
        client.lrosads.begin_put_non_retry201_creating400, product)

@pytest.mark.asyncio
async def test_sads_put_async_relative(client, product):
    await assert_raises_with_message("Operation returned an invalid status 'Bad Request'",
        client.lrosads.begin_put_async_relative_retry400, product)

    await assert_raises_with_message("no status found in body",
        client.lrosads.begin_put_async_relative_retry_no_status, product)

    await assert_raises_with_message("The response from long running operation does not contain a body.",
        client.lrosads.begin_put_async_relative_retry_no_status_payload, product)

@pytest.mark.asyncio
async def test_sads_put_error201_no_provisioning_state_payload(client, product):
    await assert_raises_with_message("The response from long running operation does not contain a body.",
        client.lrosads.begin_put_error201_no_provisioning_state_payload, product)

@pytest.mark.asyncio
async def test_sads_put200_invalid_json_with_exception(client, product):
    with pytest.raises(DecodeError):
        await lro_result(client.lrosads.begin_put200_invalid_json, product)

@pytest.mark.asyncio
async def test_sads_put_async_relative_with_exception(client, product):
    with pytest.raises(DecodeError):
        await lro_result(client.lrosads.begin_put_async_relative_retry_invalid_json_polling, product)

    with pytest.raises(Exception):
        await lro_result(client.lrosads.begin_put_async_relative_retry_invalid_header, product)

@pytest.mark.asyncio
async def test_sads_put_non_retry201_creating400_invalid_json_with_exception(client, product):
    with pytest.raises(DecodeError):
        await lro_result(client.lrosads.begin_put_non_retry201_creating400_invalid_json, product)

@pytest.mark.asyncio
async def tests_lro_sads_delete_non_retry(client, product):

    await assert_raises_with_message("Bad Request",
        client.lrosads.begin_delete_non_retry400)

    await assert_raises_with_message("Bad Request",
        client.lrosads.begin_delete202_non_retry400)

@pytest.mark.asyncio
async def test_sads_delete_async_relative(client, product):
    await assert_raises_with_message("Bad Request",
        client.lrosads.begin_delete_async_relative_retry400)

    await assert_raises_with_message("no status found in body",
        client.lrosads.begin_delete_async_relative_retry_no_status)

@pytest.mark.asyncio
async def test_sads_delete204_succeeded(client):
    await lro_result(client.lrosads.begin_delete204_succeeded)

@pytest.mark.asyncio
async def test_sads_delete_async_relative_with_exception(client):
    with pytest.raises(Exception):
        await lro_result(client.lrosads.begin_delete_async_relative_retry_invalid_header)

    with pytest.raises(DecodeError):
        await lro_result(client.lrosads.begin_delete_async_relative_retry_invalid_json_polling)

@pytest.mark.asyncio
async def test_sads_delete202_retry_invalid_header_with_exception(client):
    with pytest.raises(Exception):
        await lro_result(client.lrosads.begin_delete202_retry_invalid_header)

@pytest.mark.asyncio
async def test_sads_post_non_retry(client, product):
    await assert_raises_with_message("Bad Request",
        client.lrosads.begin_post_non_retry400, product)

    await assert_raises_with_message("Bad Request",
        client.lrosads.begin_post202_non_retry400, product)

@pytest.mark.asyncio
async def test_sads_post_async_relative(client, product):
    await assert_raises_with_message("Bad Request",
        client.lrosads.begin_post_async_relative_retry400, product)

    await assert_raises_with_message("The response from long running operation does not contain a body.",
        client.lrosads.begin_post_async_relative_retry_no_payload)

@pytest.mark.asyncio
async def test_sads_post202_no_location(client):
    # Testserver wants us to fail (coverage name is LROErrorPostNoLocation)
    # Actually, Python will NOT, and consider any kind of success 2xx on the initial call
    # is an actual success
    process = await lro_result(client.lrosads.begin_post202_no_location)
    assert process is None

@pytest.mark.asyncio
async def test_sads_post_async_relative_with_exception(client):
    with pytest.raises(Exception):
        await lro_result(client.lrosads.begin_post_async_relative_retry_invalid_header)

    with pytest.raises(DecodeError):
        await lro_result(client.lrosads.begin_post_async_relative_retry_invalid_json_polling)

@pytest.mark.asyncio
async def test_post202_retry_invalid_header_with_exception(client):
    with pytest.raises(Exception):
            await lro_result(client.lrosads.begin_post202_retry_invalid_header)

@pytest.mark.asyncio
async def test_polling_interval_operation(client):
    default_polling_interval_start_time = time.time()
    poller = await client.lros.begin_post_double_headers_final_azure_header_get_default()
    product1 = await poller.result()
    default_polling_interval_duration = time.time() - default_polling_interval_start_time
    assert abs(default_polling_interval_duration - 0) < 3

    one_second_polling_interval_start_time = time.time()
    poller = await client.lros.begin_post_double_headers_final_azure_header_get_default(polling_interval=1)
    product2 = await poller.result()
    one_second_polling_interval_duration = time.time() - one_second_polling_interval_start_time
    assert abs(one_second_polling_interval_duration - 1) < 3

    assert product1 == product2

@pytest.mark.asyncio
async def test_polling_interval_config(cookie_policy, credential, client):
    default_polling_interval_start_time = time.time()
    poller = await client.lros.begin_post_double_headers_final_azure_header_get_default()
    product1 = await poller.result()
    default_polling_interval_duration = time.time() - default_polling_interval_start_time
    assert abs(default_polling_interval_duration - 0) < 3

    # Now we create a new client with a polling_interval of 1
    policies = [
        RequestIdPolicy(),
        HeadersPolicy(),
        ContentDecodePolicy(),
        AsyncRetryPolicy(),
        cookie_policy
    ]
    client_one_second = AutoRestLongRunningOperationTestService(credential=credential, policies=policies, polling_interval=1)
    one_second_polling_interval_start_time = time.time()
    poller = await client_one_second.lros.begin_post_double_headers_final_azure_header_get_default()
    product2 = await poller.result()
    one_second_polling_interval_duration = time.time() - one_second_polling_interval_start_time
    assert abs(one_second_polling_interval_duration - 1) < 3
    assert product1 == product2

@pytest.mark.asyncio
async def test_passing_kwargs(client, product):
    process = await lro_result(client.lros.begin_put200_succeeded, product, content_type="application/json")
    assert "Succeeded" == process['properties']['provisioningState']

@pytest.mark.asyncio
async def test_lro_list(client, product):
    products = await lro_result(client.lros.begin_post202_list)
    assert len(products) == 1
    product = products[0]
    assert product["id"] == "100"
    assert product["name"]== "foo"

@pytest.mark.asyncio
async def test_patch201_retry_with_async_header(client, product):
    product = await lro_result(client.lros.begin_patch201_retry_with_async_header, product)
    assert product == {"properties": {"provisioningState": "Succeeded"}, "id": "/lro/patch/201/retry/onlyAsyncHeader", "name": "foo"}

@pytest.mark.asyncio
async def test_patch202_retry_with_async_and_location_header(client, product):
    product = await lro_result(client.lros.begin_patch202_retry_with_async_and_location_header, product)
    assert product == { "properties": { "provisioningState": "Succeeded"}, "id": "/lro/patch/202/retry/asyncAndLocationHeader", "name": "foo" }
