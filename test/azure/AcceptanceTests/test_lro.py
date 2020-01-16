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

import subprocess
import sys
import isodate
import tempfile
import json
from uuid import uuid4
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

from azure.core.exceptions import DecodeError
from azure.core.polling import LROPoller
from azure.core.pipeline.policies import ContentDecodePolicy, RetryPolicy, HeadersPolicy, RequestIdPolicy

from azure.mgmt.core.polling.arm_polling import ARMPolling
from azure.mgmt.core.exceptions import ARMError

from lro import AutoRestLongRunningOperationTestService
from lro.models import *  # pylint: disable=W0614


try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

import pytest

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
        request = self._client.get(status_link, headers=self._polling_cookie(self._response))
        # ARM requires to re-inject 'x-ms-client-request-id' while polling
        if 'request_id' not in self._operation_config:
            self._operation_config['request_id'] = self._operation.initial_response.request.headers['x-ms-client-request-id']
        return self._client._pipeline.run(request, stream=False, **self._operation_config).http_response

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

    with AutoRestLongRunningOperationTestService(credential, base_url="http://localhost:3000", policies=policies, polling_interval=0) as client:
        yield client

@pytest.fixture()
def product():
    return Product(location="West US")

@pytest.fixture()
def custom_headers():
    return {"x-ms-client-request-id": '9C4D50EE-2D56-4CD3-8152-34347DC9F2B0'}


class TestLro:

    def assert_raises_with_message(self, msg, func, *args, **kwargs):
        try:
            self.lro_result(func, *args, **kwargs)
            pytest.fail("HttpResponseError wasn't raised as expected")

        except ARMError as err:
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
            assert msg in err.message or msg in (err.odata_json or {}).get("message", "")
            if internal_msg:
                assert internal_msg in str(err.inner_exception)

    def lro_result(self, func, *args, **kwargs):
        if "polling" not in kwargs:
            kwargs["polling"] = AutorestTestARMPolling(0)
        return func(*args, **kwargs).result()

    def test_post_double_headers_final(self, client):
        product = client.lros.begin_post_double_headers_final_location_get().result()
        assert product.id == "100"

        product = client.lros.begin_post_double_headers_final_azure_header_get().result()
        assert product.id == "100"

    @pytest.mark.xfail(reason="https://github.com/Azure/autorest.modelerfour/issues/14")
    def test_happy_put201_creating_succeeded200(self, client, product):
        process = self.lro_result(client.lros.begin_put201_creating_succeeded200, product)
        assert "Succeeded" ==  process.provisioning_state

        # Testing nopolling
        process = self.lro_result(client.lros.begin_put201_creating_succeeded200, product, polling=False)
        assert "Creating" ==  process.provisioning_state

    @pytest.mark.xfail(reason="https://github.com/Azure/autorest.modelerfour/issues/14")
    def test_happy_put201_creating_failed200(self, client, product):
        self.assert_raises_with_message(
            ("Operation returned an invalid status 'OK'", "failed"),
            client.lros.begin_put201_creating_failed200, product)

        process = self.lro_result(client.lros.begin_put201_creating_failed200, product, polling=False)
        assert "Created" ==  process.provisioning_state

    @pytest.mark.xfail(reason="https://github.com/Azure/autorest.modelerfour/issues/14")
    def test_happy_put200_updating_succeeded204(self, client, product):
        process = self.lro_result(client.lros.begin_put200_updating_succeeded204, product)
        assert "Succeeded" ==  process.provisioning_state

        process = self.lro_result(client.lros.begin_put200_updating_succeeded204, product, polling=False)
        assert "Updating" ==  process.provisioning_state

    @pytest.mark.xfail(reason="https://github.com/Azure/autorest.modelerfour/issues/14")
    def test_happy_put200_acceptedcanceled200(self, client, product):
        self.assert_raises_with_message(
            ("Operation returned an invalid status 'OK'", "canceled"),
            client.lros.begin_put200_acceptedcanceled200, product)

        process = self.lro_result(client.lros.begin_put200_acceptedcanceled200, product, polling=False)
        assert "Accepted" ==  process.provisioning_state

    @pytest.mark.xfail(reason="https://github.com/Azure/autorest.modelerfour/issues/14")
    def test_happy_put_no_header_in_retry(self, client, product):
        process = self.lro_result(client.lros.begin_put_no_header_in_retry, product)
        assert "Succeeded" ==  process.provisioning_state

        process = self.lro_result(client.lros.begin_put_async_no_header_in_retry, product)
        assert "Succeeded" ==  process.provisioning_state

    @pytest.mark.xfail(reason="https://github.com/Azure/autorest.modelerfour/issues/14")
    def test_happy_put_sub_resource(self, client):
        process = self.lro_result(client.lros.begin_put_sub_resource, SubProduct())
        assert "Succeeded" ==  process.provisioning_state

        process = self.lro_result(client.lros.begin_put_async_sub_resource, SubProduct())
        assert "Succeeded" ==  process.provisioning_state

    def test_happy_put_non_resource(self, client):
        process = self.lro_result(client.lros.begin_put_non_resource, Sku())
        assert "100" ==  process.id

        process = self.lro_result(client.lros.begin_put_async_non_resource, Sku())
        assert "100" ==  process.id

    @pytest.mark.xfail(reason="https://github.com/Azure/autorest.modelerfour/issues/14")
    def test_happy_put200_succeeded(self, client, product):
        process = self.lro_result(client.lros.begin_put200_succeeded, product)
        assert "Succeeded" ==  process.provisioning_state

        process = self.lro_result(client.lros.begin_put200_succeeded_no_state, product)
        assert "100" ==  process.id

    def test_happy_put202_retry200(self, client, product):
        process = self.lro_result(client.lros.begin_put202_retry200, product)
        assert "100" ==  process.id

    @pytest.mark.xfail(reason="https://github.com/Azure/autorest.modelerfour/issues/14")
    def test_happy_put_retry_succeeded(self, client, product):
        process = self.lro_result(client.lros.begin_put_async_retry_succeeded, product)
        assert "Succeeded" ==  process.provisioning_state

        process = self.lro_result(client.lros.begin_put_async_no_retry_succeeded, product)
        assert "Succeeded" ==  process.provisioning_state

    def test_happy_put_retry_failed_canceled(self, client, product):
        self.assert_raises_with_message(
            ("Operation returned an invalid status 'OK'", "failed"),
            client.lros.begin_put_async_retry_failed, product)

        self.assert_raises_with_message(
            ("Operation returned an invalid status 'OK'", "canceled"),
            client.lros.begin_put_async_no_retrycanceled, product)

    def test_post202_retry200(self, client, product):
        process = self.lro_result(client.lros.begin_post202_retry200, product)
        assert process is None

    def test_happy_delete(self, client):
        assert self.lro_result(client.lros.begin_delete204_succeeded) is None
        assert self.lro_result(client.lros.begin_delete202_retry200) is None
        assert self.lro_result(client.lros.begin_delete202_no_retry204) is None

    def test_happy_delete_no_header_in_retry(self, client):
        assert self.lro_result(client.lros.begin_delete_no_header_in_retry) is None
        assert self.lro_result(client.lros.begin_delete_async_no_header_in_retry) is None

    def test_happy_delete_async_retry_failed_canceled(self, client):
        self.assert_raises_with_message(
            ("Operation returned an invalid status 'OK'", "canceled"),
            client.lros.begin_delete_async_retrycanceled)

        self.assert_raises_with_message(
            ("Operation returned an invalid status 'OK'", "failed"),
            client.lros.begin_delete_async_retry_failed)

    def test_happy_delete_async_succeeded(self, client):
        assert self.lro_result(client.lros.begin_delete_async_no_retry_succeeded) is None
        assert self.lro_result(client.lros.begin_delete_async_retry_succeeded) is None

    @pytest.mark.xfail(reason="https://github.com/Azure/autorest.modelerfour/issues/14")
    def test_happy_delete_provisioning(self, client):
        process = self.lro_result(client.lros.begin_delete_provisioning202_accepted200_succeeded)
        assert "Succeeded" ==  process.provisioning_state

        result = self.lro_result(client.lros.begin_delete_provisioning202_deletingcanceled200)
        assert result.provisioning_state ==  'Canceled'

        result = self.lro_result(client.lros.begin_delete_provisioning202_deleting_failed200)
        assert result.provisioning_state ==  'Failed'

    def test_happy_post(self, client, product):
        assert self.lro_result(client.lros.begin_post202_no_retry204, product) is None

        sku = self.lro_result(client.lros.begin_post200_with_payload)
        assert sku.id ==  '1'

    def test_happy_post_async_retry_failed_canceled(self, client, product):
        self.assert_raises_with_message("Internal Server Error",
            client.lros.begin_post_async_retry_failed)

        self.assert_raises_with_message(
            ("Operation returned an invalid status 'OK'", "canceled"),
            client.lros.begin_post_async_retrycanceled)

    def test_happy_post_async_succeeded(self, client, product):
        prod = self.lro_result(client.lros.begin_post_async_retry_succeeded)
        assert prod.id ==  "100"

        prod = self.lro_result(client.lros.begin_post_async_no_retry_succeeded)
        assert prod.id ==  "100"

    @pytest.mark.xfail(reason="https://github.com/Azure/autorest.modelerfour/issues/14")
    def test_retrys_put(self, client, product):
        process = self.lro_result(client.lro_retrys.begin_put201_creating_succeeded200, product)
        assert 'Succeeded' ==  process.provisioning_state

        process = self.lro_result(client.lro_retrys.begin_put_async_relative_retry_succeeded, product)
        assert 'Succeeded' ==  process.provisioning_state

    @pytest.mark.xfail(reason="https://github.com/Azure/autorest.modelerfour/issues/14")
    def test_retrys_delete(self, client, product):
        process = self.lro_result(client.lro_retrys.begin_delete_provisioning202_accepted200_succeeded)
        assert 'Succeeded' ==  process.provisioning_state

        assert self.lro_result(client.lro_retrys.begin_delete202_retry200) is None
        assert self.lro_result(client.lro_retrys.begin_delete_async_relative_retry_succeeded) is None

    def test_retrys_post(self, client, product):
        assert self.lro_result(client.lro_retrys.begin_post202_retry200, product) is None
        assert self.lro_result(client.lro_retrys.begin_post_async_relative_retry_succeeded, product) is None

    def test_custom_headers_put_async_retry_succeeded(self, client, product, custom_headers):
        process = self.lro_result(client.lr_os_custom_header.begin_put_async_retry_succeeded, product, headers=custom_headers)
        assert process is not None

    def test_custom_headers_post_async_retry_succeeded(self, client, product, custom_headers):
        process = self.lro_result(client.lr_os_custom_header.begin_post_async_retry_succeeded, product, headers=custom_headers)
        assert process is None

    def test_custom_headers_put201_creating_succeeded200(self, client, product, custom_headers):
        process = self.lro_result(client.lr_os_custom_header.begin_put201_creating_succeeded200, product, headers=custom_headers)
        assert process is not None

    def test_custom_headers_post202_retry200(self, client, product, custom_headers):
        process = self.lro_result(client.lr_os_custom_header.begin_post202_retry200, product, headers=custom_headers)
        assert process is None

    def test_sads_put_non_retry(self, client, product):
        self.assert_raises_with_message("Bad Request",
            client.lrosads.begin_put_non_retry400, product)

        self.assert_raises_with_message("Error from the server",
            client.lrosads.begin_put_non_retry201_creating400, product)

    def test_sads_put_async_relative(self, client, product):
        self.assert_raises_with_message("Operation returned an invalid status 'Bad Request'",
            client.lrosads.begin_put_async_relative_retry400, product)

        self.assert_raises_with_message("The response from long running operation does not contain a body.",
            client.lrosads.begin_put_async_relative_retry_no_status, product)

        self.assert_raises_with_message("The response from long running operation does not contain a body.",
            client.lrosads.begin_put_async_relative_retry_no_status_payload, product)

    def test_sads_put_error201_no_provisioning_state_payload(self, client, product):
        self.assert_raises_with_message("The response from long running operation does not contain a body.",
            client.lrosads.begin_put_error201_no_provisioning_state_payload, product)

    def test_sads_put200_invalid_json_with_exception(self, client, product):
        with pytest.raises(DecodeError):
            self.lro_result(client.lrosads.begin_put200_invalid_json, product)

    def test_sads_put_async_relative_with_exception(self, client, product):
        with pytest.raises(DecodeError):
            self.lro_result(client.lrosads.begin_put_async_relative_retry_invalid_json_polling, product)

        with pytest.raises(Exception):
            self.lro_result(client.lrosads.begin_put_async_relative_retry_invalid_header, product)

    def test_sads_put_non_retry201_creating400_invalid_json_with_exception(self, client, product):
        with pytest.raises(DecodeError):
            self.lro_result(client.lrosads.begin_put_non_retry201_creating400_invalid_json, product)

    def tests_lro_sads_delete_non_retry(self, client, product):

        self.assert_raises_with_message("Bad Request",
            client.lrosads.begin_delete_non_retry400)

        self.assert_raises_with_message("Bad Request",
            client.lrosads.begin_delete202_non_retry400)

    def test_sads_delete_async_relative(self, client, product):
        self.assert_raises_with_message("Bad Request",
            client.lrosads.begin_delete_async_relative_retry400)

        self.assert_raises_with_message("The response from long running operation does not contain a body.",
            client.lrosads.begin_delete_async_relative_retry_no_status)

    def test_sads_delete204_succeeded(self, client):
        self.lro_result(client.lrosads.begin_delete204_succeeded)

    def test_sads_delete_async_relative_with_exception(self, client):
        with pytest.raises(Exception):
            self.lro_result(client.lrosads.begin_delete_async_relative_retry_invalid_header)

        with pytest.raises(DecodeError):
            self.lro_result(client.lrosads.begin_delete_async_relative_retry_invalid_json_polling)

    def test_sads_delete202_retry_invalid_header_with_exception(self, client):
        with pytest.raises(Exception):
            self.lro_result(client.lrosads.begin_delete202_retry_invalid_header)

    def test_sads_post_non_retry(self, client, product):
        self.assert_raises_with_message("Bad Request",
            client.lrosads.begin_post_non_retry400, product)

        self.assert_raises_with_message("Bad Request",
            client.lrosads.begin_post202_non_retry400, product)

    def test_sads_post_async_relative(self, client, product):
        self.assert_raises_with_message("Bad Request",
            client.lrosads.begin_post_async_relative_retry400, product)

        self.assert_raises_with_message("The response from long running operation does not contain a body.",
            client.lrosads.begin_post_async_relative_retry_no_payload)

    def test_sads_post202_no_location(self, client):
        self.assert_raises_with_message("Unable to find status link for polling.",
            client.lrosads.begin_post202_no_location)

    def test_sads_post_async_relative_with_exception(self, client):
        with pytest.raises(Exception):
            self.lro_result(client.lrosads.begin_post_async_relative_retry_invalid_header)

        with pytest.raises(DecodeError):
            self.lro_result(client.lrosads.begin_post_async_relative_retry_invalid_json_polling)

    def test_post202_retry_invalid_header_with_exception(self, client):
        with pytest.raises(Exception):
                self.lro_result(client.lrosads.begin_post202_retry_invalid_header)
