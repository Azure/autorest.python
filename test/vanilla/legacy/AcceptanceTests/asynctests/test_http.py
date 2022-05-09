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

from async_generator import yield_, async_generator
import unittest
import subprocess
import sys
import isodate
import tempfile
import requests
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

import requests

from azure.core.exceptions import HttpResponseError
from azure.core.pipeline.policies import ContentDecodePolicy, AsyncRetryPolicy, HeadersPolicy, AsyncRedirectPolicy
from msrest.exceptions import DeserializationError

from httpinfrastructure.aio import AutoRestHttpInfrastructureTestService
from httpinfrastructure.models import B, C, D, MyException

import pytest


@pytest.fixture
@async_generator
async def client(cookie_policy):
    """Create a AutoRestHttpInfrastructureTestService client with test server credentials."""
    policies = [
        HeadersPolicy(),
        ContentDecodePolicy(),
        AsyncRedirectPolicy(),
        AsyncRetryPolicy(),
        cookie_policy
    ]
    async with AutoRestHttpInfrastructureTestService(base_url="http://localhost:3000", policies=policies) as client:
        await yield_(client)


class TestHttp(object):
    async def assert_status(self, code, func, *args, **kwargs):
        def return_status(pipeline_response, data, headers):
            return pipeline_response.http_response.status_code
        kwargs['cls'] = return_status
        status_code = await func(*args, **kwargs)
        assert status_code == code

    async def assert_raises_with_message(self, msg, func, *args, **kwargs):
        try:
            await func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            assert err.message == msg

    async def assert_raises_with_model(self, code, model, func, *args, **kwargs):
        try:
            await func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            if err.model:
                assert isinstance(err.model, model)
            assert err.response.status_code == code

    async def assert_raises_with_status(self, code, func, *args, **kwargs):
        try:
            await func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            assert err.response.status_code == code

    async def assert_raises_with_status_and_message(self, code, msg, func, *args, **kwargs):
        try:
            await func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            assert err.model.message == msg
            assert msg in err.message
            assert msg in str(err)
            assert err.response.status_code == code

    async def assert_raises_with_status_and_response_contains(self, code, msg, func, *args, **kwargs):
        try:
            await func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            assert err.response.status_code == code
            assert msg in err.response.text()


    @pytest.mark.asyncio
    async def test_get200_model204(self, client):
        r = await client.multiple_responses.get200_model204_no_model_default_error200_valid()
        assert '200' ==  r.status_code

        await self.assert_raises_with_status(201,
            client.multiple_responses.get200_model204_no_model_default_error201_invalid)

        await self.assert_raises_with_status(202,
            client.multiple_responses.get200_model204_no_model_default_error202_none)

        assert (await client.multiple_responses.get200_model204_no_model_default_error204_valid()) is None

        await self.assert_raises_with_status_and_message(400, "client error",
            client.multiple_responses.get200_model204_no_model_default_error400_valid)

    @pytest.mark.asyncio
    async def test_get200_model201(self, client):
        await self.assert_status(200, client.multiple_responses.get200_model201_model_default_error200_valid)

        b_model = await client.multiple_responses.get200_model201_model_default_error201_valid()
        assert b_model is not None
        assert b_model.status_code ==  "201"
        assert b_model.text_status_code ==  "Created"

        await self.assert_raises_with_status_and_message(400, "client error",
            client.multiple_responses.get200_model201_model_default_error400_valid)

    @pytest.mark.asyncio
    async def test_get200_model_a201_model_c404(self, client):
        a_model = await client.multiple_responses.get200_model_a201_model_c404_model_d_default_error200_valid()
        assert a_model is not None
        assert a_model.status_code ==  "200"

        c_model = await client.multiple_responses.get200_model_a201_model_c404_model_d_default_error201_valid()
        assert c_model is not None
        assert c_model.http_code ==  "201"

        d_model = await client.multiple_responses.get200_model_a201_model_c404_model_d_default_error404_valid()
        assert d_model is not None
        assert d_model.http_status_code ==  "404"

        await self.assert_raises_with_status_and_message(400, "client error",
            client.multiple_responses.get200_model_a201_model_c404_model_d_default_error400_valid)

    @pytest.mark.asyncio
    async def test_get202_none204(self, client):
        await client.multiple_responses.get202_none204_none_default_error202_none()
        await client.multiple_responses.get202_none204_none_default_error204_none()

        await self.assert_raises_with_status_and_message(400, "client error",
            client.multiple_responses.get202_none204_none_default_error400_valid)

        await client.multiple_responses.get202_none204_none_default_none202_invalid()
        await client.multiple_responses.get202_none204_none_default_none204_none()

        await self.assert_raises_with_status(400,
            client.multiple_responses.get202_none204_none_default_none400_none)

        await self.assert_raises_with_status(400,
            client.multiple_responses.get202_none204_none_default_none400_invalid)

    @pytest.mark.asyncio
    async def test_get_default_model_a200(self, client):
        await self.assert_status(200, client.multiple_responses.get_default_model_a200_valid)

        assert (await client.multiple_responses.get_default_model_a200_none()) is None
        await client.multiple_responses.get_default_model_a200_valid()
        await client.multiple_responses.get_default_model_a200_none()

    @pytest.mark.asyncio
    async def test_get_default_model_a400(self, client):
        await self.assert_raises_with_model(400, MyException,
            client.multiple_responses.get_default_model_a400_valid)

        await self.assert_raises_with_model(400, MyException,
            client.multiple_responses.get_default_model_a400_none)

    @pytest.mark.asyncio
    async def test_get_default_none200(self, client):
        await client.multiple_responses.get_default_none200_invalid()
        await client.multiple_responses.get_default_none200_none()

    @pytest.mark.asyncio
    async def test_get_default_none400(self, client):
        await self.assert_raises_with_status(400,
            client.multiple_responses.get_default_none400_invalid)

        await self.assert_raises_with_status(400,
            client.multiple_responses.get_default_none400_none)

    @pytest.mark.asyncio
    async def test_get200_model_a200(self, client):
        assert await client.multiple_responses.get200_model_a200_none() is None

        await self.assert_status(200, client.multiple_responses.get200_model_a200_valid)

        assert (await client.multiple_responses.get200_model_a200_invalid()).status_code is None

    @pytest.mark.asyncio
    async def test_get200_model_a400(self, client):
        await self.assert_raises_with_status(400,
            client.multiple_responses.get200_model_a400_none)
        await self.assert_raises_with_status(400,
            client.multiple_responses.get200_model_a400_valid)
        await self.assert_raises_with_status(400,
            client.multiple_responses.get200_model_a400_invalid)

    @pytest.mark.asyncio
    async def test_get200_model_a202(self, client):
        await self.assert_raises_with_status(202,
            client.multiple_responses.get200_model_a202_valid)

    @pytest.mark.asyncio
    async def test_server_error_status_codes_501(self, client):

        await self.assert_raises_with_status(requests.codes.not_implemented,
            client.http_server_failure.head501)

        await self.assert_raises_with_status(requests.codes.not_implemented,
            client.http_server_failure.get501)

    @pytest.mark.asyncio
    async def test_server_error_status_codes_505(self, client):
        await self.assert_raises_with_status(requests.codes.http_version_not_supported,
            client.http_server_failure.post505)

        await self.assert_raises_with_status(requests.codes.http_version_not_supported,
            client.http_server_failure.delete505)

    @pytest.mark.asyncio
    async def test_retry_status_codes_408(self, client):
        await client.http_retry.head408()

    @pytest.mark.asyncio
    async def test_retry_status_codes_502(self, client):
        await client.http_retry.get502()
        await client.http_retry.options502()

    @pytest.mark.asyncio
    async def test_retry_status_codes_500(self, client):
        await client.http_retry.put500()
        await client.http_retry.patch500()

    @pytest.mark.asyncio
    async def test_retry_status_codes_503(self, client):
        await client.http_retry.post503()
        await client.http_retry.delete503()

    @pytest.mark.asyncio
    async def test_retry_status_codes_504(self, client):
        await client.http_retry.put504()
        await client.http_retry.patch504()

    @pytest.mark.asyncio
    async def test_error_status_codes_400(self, client):
        await self.assert_raises_with_status(requests.codes.bad_request,
            client.http_client_failure.head400)

        await self.assert_raises_with_status(requests.codes.bad_request,
            client.http_client_failure.get400)

        # TODO, 4042586: Support options operations in swagger modeler
        #await self.assert_raises_with_status(requests.codes.bad_request,
        #    await client.http_client_failure.options400)

        await self.assert_raises_with_status(requests.codes.bad_request,
            client.http_client_failure.put400)

        await self.assert_raises_with_status(requests.codes.bad_request,
            client.http_client_failure.patch400)

        await self.assert_raises_with_status(requests.codes.bad_request,
            client.http_client_failure.post400)

        await self.assert_raises_with_status(requests.codes.bad_request,
            client.http_client_failure.delete400)

    @pytest.mark.asyncio
    async def test_error_status_codes_401(self, client):
        await self.assert_raises_with_status(requests.codes.unauthorized,
            client.http_client_failure.head401)

    @pytest.mark.asyncio
    async def test_error_status_codes_402(self, client):
        await self.assert_raises_with_status(requests.codes.payment_required,
            client.http_client_failure.get402)

    @pytest.mark.asyncio
    async def test_error_status_codes_403(self, client):
        # TODO, 4042586: Support options operations in swagger modeler
        #await self.assert_raises_with_status(requests.codes.forbidden,
        #    client.http_client_failure.options403)

        await self.assert_raises_with_status(requests.codes.forbidden,
            client.http_client_failure.get403)

    @pytest.mark.asyncio
    async def test_error_status_codes_404(self, client):
        await self.assert_raises_with_status(requests.codes.not_found,
            client.http_client_failure.put404)

    @pytest.mark.asyncio
    async def test_error_status_codes_405(self, client):
        await self.assert_raises_with_status(requests.codes.method_not_allowed,
            client.http_client_failure.patch405)

    @pytest.mark.asyncio
    async def test_error_status_codes_406(self, client):
        await self.assert_raises_with_status(requests.codes.not_acceptable,
            client.http_client_failure.post406)

    @pytest.mark.asyncio
    async def test_error_status_codes_407(self, client):
        await self.assert_raises_with_status(requests.codes.proxy_authentication_required,
            client.http_client_failure.delete407)

    @pytest.mark.asyncio
    async def test_error_status_codes_409(self, client):
        await self.assert_raises_with_status(requests.codes.conflict,
            client.http_client_failure.put409)

    @pytest.mark.asyncio
    async def test_error_status_codes_410(self, client):
        await self.assert_raises_with_status(requests.codes.gone,
            client.http_client_failure.head410)

    @pytest.mark.asyncio
    async def test_error_status_codes_411(self, client):
        await self.assert_raises_with_status(requests.codes.length_required,
            client.http_client_failure.get411)

        # TODO, 4042586: Support options operations in swagger modeler
        #await self.assert_raises_with_status(requests.codes.precondition_failed,
        #    client.http_client_failure.options412)

        await self.assert_raises_with_status(requests.codes.precondition_failed,
            client.http_client_failure.get412)

        await self.assert_raises_with_status(requests.codes.request_entity_too_large,
            client.http_client_failure.put413)

        await self.assert_raises_with_status(requests.codes.request_uri_too_large,
            client.http_client_failure.patch414)

        await self.assert_raises_with_status(requests.codes.unsupported_media,
            client.http_client_failure.post415)

        await self.assert_raises_with_status(requests.codes.requested_range_not_satisfiable,
            client.http_client_failure.get416)

        await self.assert_raises_with_status(requests.codes.expectation_failed,
            client.http_client_failure.delete417)

        await self.assert_raises_with_status(429,
            client.http_client_failure.head429)

    @pytest.mark.asyncio
    async def test_redirect_to_300(self, client):
        await self.assert_status(200, client.http_redirects.get300)
        await self.assert_status(200, client.http_redirects.head300)

    @pytest.mark.asyncio
    async def test_redirect_to_301(self, client):
        await self.assert_status(200, client.http_redirects.head301)
        await self.assert_status(200, client.http_redirects.get301)
        await self.assert_status(requests.codes.moved_permanently, client.http_redirects.put301)

    @pytest.mark.asyncio
    async def test_redirect_to_302(self, client):
        await self.assert_status(200, client.http_redirects.head302)
        await self.assert_status(200, client.http_redirects.get302)
        await self.assert_status(requests.codes.found, client.http_redirects.patch302)

    @pytest.mark.asyncio
    async def test_redicret_to_303(self, client):
        await self.assert_status(200, client.http_redirects.post303)

    @pytest.mark.asyncio
    async def test_redirect_to_307(self, client):
        await self.assert_status(200, client.http_redirects.head307)
        await self.assert_status(200, client.http_redirects.get307)
        await self.assert_status(200, client.http_redirects.options307)
        await self.assert_status(200, client.http_redirects.put307)
        await self.assert_status(200, client.http_redirects.post307)
        await self.assert_status(200, client.http_redirects.patch307)
        await self.assert_status(200, client.http_redirects.delete307)

    @pytest.mark.asyncio
    async def test_bad_request_status_assert(self, client):
        await self.assert_raises_with_message("Operation returned an invalid status 'Bad Request'",
            (client.http_failure.get_empty_error))

    @pytest.mark.asyncio
    async def test_no_error_model_status_assert(self, client):
        await self.assert_raises_with_status_and_response_contains(requests.codes.bad_request, "NoErrorModel",
            (client.http_failure.get_no_model_error))

    @pytest.mark.asyncio
    async def test_success_status_codes_200(self, client):
        await client.http_success.head200()
        assert await client.http_success.get200()
        await client.http_success.put200()
        await client.http_success.post200()
        await client.http_success.patch200()
        await client.http_success.delete200()

        # TODO, 4042586: Support options operations in swagger modeler
        #assert await client.http_success.options200()

    @pytest.mark.asyncio
    async def test_success_status_codes_201(self, client):
        await client.http_success.put201()
        await client.http_success.post201()

    @pytest.mark.asyncio
    async def test_success_status_codes_202(self, client):
        await client.http_success.put202()
        await client.http_success.post202()
        await client.http_success.patch202()
        await client.http_success.delete202()

    @pytest.mark.asyncio
    async def test_success_status_codes_204(self, client):
        await client.http_success.head204()
        await client.http_success.put204()
        await client.http_success.post204()
        await client.http_success.delete204()
        await client.http_success.patch204()

    @pytest.mark.asyncio
    async def test_success_status_codes_404(self, client):
        await client.http_success.head404()

    @pytest.mark.asyncio
    async def test_empty_no_content(self, client):
        await self.assert_raises_with_status(requests.codes.bad_request,
            client.http_failure.get_no_model_empty)
