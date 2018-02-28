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
sys.path.append(join(tests, "Lro"))

# Import mock from Autorest.Python.Tests
mockfiles = realpath(join(cwd, pardir, pardir, "vanilla", "AcceptanceTests"))
sys.path.append(mockfiles)

from msrest.serialization import Deserializer
from msrest.exceptions import DeserializationError
from msrest.authentication import BasicTokenAuthentication
from msrest.polling.async_poller import async_poller
from msrestazure.azure_exceptions import CloudError, CloudErrorData
from msrestazure.polling.async_arm_polling import (
    AsyncARMPolling,
)
from lro import AutoRestLongRunningOperationTestService
from lro.models import *  # pylint: disable=W0614

from http_tests import TestAuthentication

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

import pytest

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
        request = self._client.get(status_link)
        # ARM requires to re-inject 'x-ms-client-request-id' while polling
        header_parameters = {
            'x-ms-client-request-id': self._operation.initial_response.request.headers['x-ms-client-request-id']
        }
        header_parameters.update(self._polling_cookie(self._response))
        return await self._client.async_send(request, header_parameters)


class TestLro:

    @property
    def client(self):
        if not hasattr(self, "_client"):
            cred = BasicTokenAuthentication({"access_token" :str(uuid4())})
            self._client = AutoRestLongRunningOperationTestService(cred, base_url="http://localhost:3000")
            self._client._client.creds = TestAuthentication()
            self._client.config.long_running_operation_timeout = 0 # In theory pointless, since we use AutorestTestARMPolling
        return self._client

    async def assertRaisesWithMessage(self, msg, func, *args, **kwargs):
        try:
            await self.lro_result(func, *args, **kwargs)
            pytest.fail("CloudError wasn't raised as expected")

        except CloudError as err:
            assert msg in err.message
            assert err.response is not None
            error = err.error
            assert error is not None
            if isinstance(error, CloudErrorData):
                assert error.message is not None

    async def lro_result(self, func, *args, **kwargs):
        if "polling" not in kwargs:
            kwargs["polling"] = AutorestTestARMPolling(0)
        return await func(*args, **kwargs)

    @pytest.mark.asyncio
    async def test_lro_happy_paths(self):

        product = Product(location="West US")

        # Test manual poller
        raw_process = await self.client.lr_os.put201_creating_succeeded200_async(product, raw=True, polling=False)
        process = await async_poller(self.client, raw_process, Product, AsyncARMPolling(timeout=0))
        assert "Succeeded" == process.provisioning_state

        process = await self.lro_result(self.client.lr_os.put201_creating_succeeded200_async, product)
        assert "Succeeded" == process.provisioning_state

        await self.assertRaisesWithMessage("Operation failed with status: 200. Details: Resource state Failed",
            self.client.lr_os.put201_creating_failed200_async, product)

        process = await self.lro_result(self.client.lr_os.put200_updating_succeeded204_async, product)
        assert "Succeeded" == process.provisioning_state

        await self.assertRaisesWithMessage("Operation failed with status: 200. Details: Resource state Canceled",
            self.client.lr_os.put200_acceptedcanceled200_async, product)

        # Testing nopolling
        process = await self.lro_result(self.client.lr_os.put201_creating_succeeded200_async, product, polling=False)
        assert "Creating" == process.provisioning_state

        process = await self.lro_result(self.client.lr_os.put201_creating_failed200_async, product, polling=False)
        assert "Created" == process.provisioning_state

        process = await self.lro_result(self.client.lr_os.put200_updating_succeeded204_async, product, polling=False)
        assert "Updating" == process.provisioning_state

        process = await self.lro_result(self.client.lr_os.put200_acceptedcanceled200_async, product, polling=False)
        assert "Accepted" == process.provisioning_state

        # Testing nopolling and raw at the same time
        process = await self.lro_result(self.client.lr_os.put201_creating_succeeded200_async, product, raw=True, polling=False)
        assert "Creating" == process.output.provisioning_state

        process = await self.lro_result(self.client.lr_os.put201_creating_failed200_async, product, raw=True, polling=False)
        assert "Created" == process.output.provisioning_state

        process = await self.lro_result(self.client.lr_os.put200_updating_succeeded204_async, product, raw=True, polling=False)
        assert "Updating" == process.output.provisioning_state

        process = await self.lro_result(self.client.lr_os.put200_acceptedcanceled200_async, product, raw=True, polling=False)
        assert "Accepted" == process.output.provisioning_state

        process = await self.lro_result(self.client.lr_os.put_no_header_in_retry_async, product)
        assert "Succeeded" == process.provisioning_state

        process = await self.lro_result(self.client.lr_os.put_async_no_header_in_retry_async, product)
        assert "Succeeded" == process.provisioning_state

        process = await self.lro_result(self.client.lr_os.put_sub_resource_async, SubProduct())
        assert "Succeeded" == process.provisioning_state

        process = await self.lro_result(self.client.lr_os.put_async_sub_resource_async, SubProduct())
        assert "Succeeded" == process.provisioning_state

        process = await self.lro_result(self.client.lr_os.put_non_resource_async, Sku())
        assert "100" == process.id

        process = await self.lro_result(self.client.lr_os.put_async_non_resource_async, Sku())
        assert "100" == process.id

        process = await self.lro_result(self.client.lr_os.post202_retry200_async, product)
        assert process is None

        process = await self.lro_result(self.client.lr_os.put200_succeeded_async, product)
        assert "Succeeded" == process.provisioning_state

        process = await self.lro_result(self.client.lr_os.put200_succeeded_no_state_async, product)
        assert "100" == process.id

        process = await self.lro_result(self.client.lr_os.put202_retry200_async, product)
        assert "100" == process.id

        process = await self.lro_result(self.client.lr_os.put_async_retry_succeeded_async, product)
        assert "Succeeded" == process.provisioning_state

        process = await self.lro_result(self.client.lr_os.put_async_no_retry_succeeded_async, product)
        assert "Succeeded" == process.provisioning_state

        await self.assertRaisesWithMessage("Operation failed with status: 200. Details: Resource state Failed",
            self.client.lr_os.put_async_retry_failed_async, product)

        await self.assertRaisesWithMessage("Operation failed with status: 200. Details: Resource state Canceled",
            self.client.lr_os.put_async_no_retrycanceled_async, product)

        assert await self.lro_result(self.client.lr_os.delete204_succeeded_async) is None
        assert await self.lro_result(self.client.lr_os.delete202_retry200_async) is None
        assert await self.lro_result(self.client.lr_os.delete202_no_retry204_async) is None

        assert await self.lro_result(self.client.lr_os.delete_async_no_retry_succeeded_async) is None
        assert await self.lro_result(self.client.lr_os.delete_no_header_in_retry_async) is None

        assert await self.lro_result(self.client.lr_os.delete_async_no_header_in_retry_async) is None

        await self.assertRaisesWithMessage("Operation failed with status: 200. Details: Resource state Canceled",
            self.client.lr_os.delete_async_retrycanceled_async)

        await self.assertRaisesWithMessage("Operation failed with status: 200. Details: Resource state Failed",
            self.client.lr_os.delete_async_retry_failed_async)

        assert await self.lro_result(self.client.lr_os.delete_async_retry_succeeded_async) is None

        process = await self.lro_result(self.client.lr_os.delete_provisioning202_accepted200_succeeded_async)
        assert "Succeeded" == process.provisioning_state

        result = await self.lro_result(self.client.lr_os.delete_provisioning202_deletingcanceled200_async)
        assert result.provisioning_state == 'Canceled'

        result = await self.lro_result(self.client.lr_os.delete_provisioning202_deleting_failed200_async)
        assert result.provisioning_state == 'Failed'

        assert await self.lro_result(self.client.lr_os.post202_no_retry204_async, product) is None

        await self.assertRaisesWithMessage("Internal Server Error",
            self.client.lr_os.post_async_retry_failed_async)

        await self.assertRaisesWithMessage("Operation failed with status: 200. Details: Resource state Canceled",
            self.client.lr_os.post_async_retrycanceled_async)

        prod = await self.lro_result(self.client.lr_os.post_async_retry_succeeded_async)
        assert prod.id == "100"

        prod = await self.lro_result(self.client.lr_os.post_async_no_retry_succeeded_async)
        assert prod.id == "100"

        sku = await self.lro_result(self.client.lr_os.post200_with_payload_async)
        assert sku.id == '1'

        process = await self.lro_result(self.client.lro_retrys.put201_creating_succeeded200_async, product)
        assert 'Succeeded' == process.provisioning_state

        process = await self.lro_result(self.client.lro_retrys.put_async_relative_retry_succeeded_async, product)
        assert 'Succeeded' == process.provisioning_state

        process = await self.lro_result(self.client.lro_retrys.delete_provisioning202_accepted200_succeeded_async)
        assert 'Succeeded' == process.provisioning_state

        assert await self.lro_result(self.client.lro_retrys.delete202_retry200_async) is None
        assert await self.lro_result(self.client.lro_retrys.delete_async_relative_retry_succeeded_async) is None
        assert await self.lro_result(self.client.lro_retrys.post202_retry200_async, product) is None
        assert await self.lro_result(self.client.lro_retrys.post_async_relative_retry_succeeded_async, product) is None

        custom_headers = {"x-ms-client-request-id": '9C4D50EE-2D56-4CD3-8152-34347DC9F2B0'}

        process = await self.lro_result(self.client.lr_os_custom_header.put_async_retry_succeeded_async, product, custom_headers)
        assert process is not None

        process = await self.lro_result(self.client.lr_os_custom_header.post_async_retry_succeeded_async, product, custom_headers)
        assert process is None

        process = await self.lro_result(self.client.lr_os_custom_header.put201_creating_succeeded200_async, product, custom_headers)
        assert process is not None

        process = await self.lro_result(self.client.lr_os_custom_header.post202_retry200_async, product, custom_headers)
        assert process is None

    @pytest.mark.asyncio
    async def test_lro_sad_paths(self):

        product = Product(location="West US")

        await self.assertRaisesWithMessage("Expected bad request message",
            self.client.lrosa_ds.put_non_retry400_async, product)

        await self.assertRaisesWithMessage("Error from the server",
            self.client.lrosa_ds.put_non_retry201_creating400_async, product)

        await self.assertRaisesWithMessage("Operation failed with status: 'Bad Request'",
            self.client.lrosa_ds.put_async_relative_retry400_async, product)

        await self.assertRaisesWithMessage("Expected bad request message",
            self.client.lrosa_ds.delete_non_retry400_async)

        await self.assertRaisesWithMessage("Expected bad request message",
            self.client.lrosa_ds.delete202_non_retry400_async)

        await self.assertRaisesWithMessage("Expected bad request message",
            self.client.lrosa_ds.delete_async_relative_retry400_async)

        await self.assertRaisesWithMessage("Expected bad request message",
            self.client.lrosa_ds.post_non_retry400_async, product)

        await self.assertRaisesWithMessage("Expected bad request message",
            self.client.lrosa_ds.post202_non_retry400_async, product)

        await self.assertRaisesWithMessage("Expected bad request message",
            self.client.lrosa_ds.post_async_relative_retry400_async, product)

        await self.assertRaisesWithMessage("The response from long running operation does not contain a body.",
            self.client.lrosa_ds.put_error201_no_provisioning_state_payload_async, product)

        await self.assertRaisesWithMessage("The response from long running operation does not contain a body.",
            self.client.lrosa_ds.put_async_relative_retry_no_status_async, product)

        await self.assertRaisesWithMessage("The response from long running operation does not contain a body.",
            self.client.lrosa_ds.put_async_relative_retry_no_status_payload_async, product)

        with pytest.raises(DeserializationError):
            await self.lro_result(self.client.lrosa_ds.put200_invalid_json_async, product)

        with pytest.raises(DeserializationError):
            await self.lro_result(self.client.lrosa_ds.put_async_relative_retry_invalid_json_polling_async, product)

        with pytest.raises(Exception):
            await self.lro_result(self.client.lrosa_ds.put_async_relative_retry_invalid_header_async, product)

        with pytest.raises(Exception):
            await self.lro_result(self.client.lrosa_ds.delete202_retry_invalid_header_async)

        with pytest.raises(Exception):
            await self.lro_result(self.client.lrosa_ds.delete_async_relative_retry_invalid_header_async)

        with pytest.raises(Exception):
            await self.lro_result(self.client.lrosa_ds.post202_retry_invalid_header_async)

        with pytest.raises(Exception):
            await self.lro_result(self.client.lrosa_ds.post_async_relative_retry_invalid_header_async)

        with pytest.raises(DeserializationError):
            await self.lro_result(self.client.lrosa_ds.delete_async_relative_retry_invalid_json_polling_async)

        with pytest.raises(DeserializationError):
            await self.lro_result(self.client.lrosa_ds.post_async_relative_retry_invalid_json_polling_async)

        await self.lro_result(self.client.lrosa_ds.delete204_succeeded_async)

        await self.assertRaisesWithMessage("The response from long running operation does not contain a body.",
            self.client.lrosa_ds.delete_async_relative_retry_no_status_async)

        await self.assertRaisesWithMessage("Unable to find status link for polling.",
            self.client.lrosa_ds.post202_no_location_async)

        await self.assertRaisesWithMessage("The response from long running operation does not contain a body.",
            self.client.lrosa_ds.post_async_relative_retry_no_payload_async)

        await self.assertRaisesWithMessage("Operation failed",
            self.client.lrosa_ds.put_non_retry201_creating400_invalid_json_async, product)

if __name__ == '__main__':
    unittest.main()
