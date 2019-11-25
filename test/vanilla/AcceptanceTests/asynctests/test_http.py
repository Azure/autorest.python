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
import requests
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

import requests

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "Http"))

from azure.core.exceptions import HttpResponseError
from azure.core.pipeline.policies import ContentDecodePolicy, AsyncRetryPolicy, HeadersPolicy, AsyncRedirectPolicy
from msrest.exceptions import DeserializationError

from httpinfrastructure.aio import AutoRestHttpInfrastructureTestService
from httpinfrastructure.models import (
    A, B, C, D, ErrorException)

import pytest


@pytest.fixture()
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
        yield client


class TestHttp(object):

    @pytest.mark.asyncio
    async def assertStatus(self, code, func, *args, **kwargs):
        def return_status(response, data, headers):
            return response.status_code
        kwargs['cls'] = return_status
        status_code = func(*args, **kwargs)
        assert status_code == code

    @pytest.mark.asyncio
    async def assertRaisesWithMessage(self, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            assert err.message == msg

    @pytest.mark.asyncio
    async def assertRaisesWithModel(self, code, model, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            assert isinstance(err.error, model)
            assert err.response.status_code == code

    @pytest.mark.asyncio
    async def assertRaisesWithStatus(self, code, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            assert err.response.status_code == code

    @pytest.mark.asyncio
    async def assertRaisesWithStatusAndMessage(self, code, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            assert err.message == msg
            assert err.response.status_code == code

    @pytest.mark.asyncio
    async def assertRaisesWithStatusAndResponseContains(self, code, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            assert err.response.status_code == code
            assert msg in err.response.text()

    @pytest.mark.asyncio
    async def test_get200_model204(self, client):
        r = await client.multiple_responses.get200_model204_no_model_default_error200_valid()
        assert '200' ==  r.status_code

        self.assertRaisesWithStatus(201,
            await client.multiple_responses.get200_model204_no_model_default_error201_invalid)

        self.assertRaisesWithStatus(202,
            await client.multiple_responses.get200_model204_no_model_default_error202_none)

        assert await client.multiple_responses.get200_model204_no_model_default_error204_valid() is None

        self.assertRaisesWithStatusAndMessage(400, "client error",
            await client.multiple_responses.get200_model204_no_model_default_error400_valid)

    @pytest.mark.asyncio
    async def test_get200_model201(self, client):
        self.assertStatus(200, await client.multiple_responses.get200_model201_model_default_error200_valid)

        b_model = await client.multiple_responses.get200_model201_model_default_error201_valid()
        assert b_model is not None
        assert b_model.status_code ==  "201"
        assert b_model.text_status_code ==  "Created"

        self.assertRaisesWithStatusAndMessage(400, "client error",
            await client.multiple_responses.get200_model201_model_default_error400_valid)

    @pytest.mark.asyncio
    async def test_get200_model_a201_model_c404(self, client):
        a_model = await client.multiple_responses.get200_model_a201_model_c404_model_ddefault_error200_valid()
        assert a_model is not None
        assert a_model.status_code ==  "200"

        c_model = await client.multiple_responses.get200_model_a201_model_c404_model_ddefault_error201_valid()
        assert c_model is not None
        assert c_model.http_code ==  "201"

        d_model = await client.multiple_responses.get200_model_a201_model_c404_model_ddefault_error404_valid()
        assert d_model is not None
        assert d_model.http_status_code ==  "404"

        self.assertRaisesWithStatusAndMessage(400, "client error",
            await client.multiple_responses.get200_model_a201_model_c404_model_ddefault_error400_valid)

    @pytest.mark.asyncio
    async def test_get202_none204(self, client):
        await client.multiple_responses.get202_none204_none_default_error202_none()
        await client.multiple_responses.get202_none204_none_default_error204_none()

        self.assertRaisesWithStatusAndMessage(400, "client error",
            await client.multiple_responses.get202_none204_none_default_error400_valid)

        await client.multiple_responses.get202_none204_none_default_none202_invalid()
        await client.multiple_responses.get202_none204_none_default_none204_none()

        self.assertRaisesWithStatus(400,
            await client.multiple_responses.get202_none204_none_default_none400_none)

        self.assertRaisesWithStatus(400,
            await client.multiple_responses.get202_none204_none_default_none400_invalid)

    @pytest.mark.asyncio
    async def test_get_default_model_a200(self, client):
        self.assertStatus(200, await client.multiple_responses.get_default_model_a200_valid)

        assert await client.multiple_responses.get_default_model_a200_none() is None
        await client.multiple_responses.get_default_model_a200_valid()
        await client.multiple_responses.get_default_model_a200_none()

    @pytest.mark.asyncio
    async def test_get_default_model_a400(self, client):
        self.assertRaisesWithModel(400, A,
            await client.multiple_responses.get_default_model_a400_valid)

        self.assertRaisesWithModel(400, A,
            await client.multiple_responses.get_default_model_a400_none)

    @pytest.mark.asyncio
    async def test_get_default_none200(self, client):
        await client.multiple_responses.get_default_none200_invalid()
        await client.multiple_responses.get_default_none200_none()

    @pytest.mark.asyncio
    async def test_get_default_none400(self, client):
        self.assertRaisesWithStatus(400,
            await client.multiple_responses.get_default_none400_invalid)

        self.assertRaisesWithStatus(400,
            await client.multiple_responses.get_default_none400_none)

    @pytest.mark.asyncio
    async def test_get200_model_a200(self, client):
        assert await client.multiple_responses.get200_model_a200_none() is None

        self.assertStatus(200, await client.multiple_responses.get200_model_a200_valid)

        assert await client.multiple_responses.get200_model_a200_invalid().status_code is None

    @pytest.mark.asyncio
    async def test_get200_model_a400(self, client):
        self.assertRaisesWithStatus(400,
            await client.multiple_responses.get200_model_a400_none)
        self.assertRaisesWithStatus(400,
            await client.multiple_responses.get200_model_a400_valid)
        self.assertRaisesWithStatus(400,
            await client.multiple_responses.get200_model_a400_invalid)

    @pytest.mark.asyncio
    async def test_get200_model_a202(self, client):
        self.assertRaisesWithStatus(202,
            await client.multiple_responses.get200_model_a202_valid)

    @pytest.mark.asyncio
    async def test_server_error_status_codes_501(self, client):

        self.assertRaisesWithStatus(requests.codes.not_implemented,
            await client.http_server_failure.head501)

        self.assertRaisesWithStatus(requests.codes.not_implemented,
            await client.http_server_failure.get501)

    @pytest.mark.asyncio
    async def test_server_error_status_codes_505(self, client):
        self.assertRaisesWithStatus(requests.codes.http_version_not_supported,
            await client.http_server_failure.post505, True)

        self.assertRaisesWithStatus(requests.codes.http_version_not_supported,
            await client.http_server_failure.delete505, True)

    @pytest.mark.asyncio
    async def test_retry_status_codes_408(self, client):
        await client.http_retry.head408()

    @pytest.mark.asyncio
    async def test_retry_status_codes_502(self, client):
        await client.http_retry.get502()

        # TODO, 4042586: Support options operations in swagger modeler
        #await client.http_retry.options429()
    
    @pytest.mark.asyncio
    async def test_retry_status_codes_500(self, client):
        await client.http_retry.put500(True)
        await client.http_retry.patch500(True)

    @pytest.mark.asyncio
    async def test_retry_status_codes_503(self, client):
        await client.http_retry.post503(True)
        await client.http_retry.delete503(True)

    @pytest.mark.asyncio
    async def test_retry_status_codes_504(self, client):
        await client.http_retry.put504(True)
        await client.http_retry.patch504(True)

    @pytest.mark.asyncio
    async def test_error_status_codes_400(self, client):
        self.assertRaisesWithStatus(requests.codes.bad_request,
            await client.http_client_failure.head400)

        self.assertRaisesWithStatus(requests.codes.bad_request,
            await client.http_client_failure.get400)

        # TODO, 4042586: Support options operations in swagger modeler
        #self.assertRaisesWithStatus(requests.codes.bad_request,
        #    await client.http_client_failure.options400)

        self.assertRaisesWithStatus(requests.codes.bad_request,
            await client.http_client_failure.put400, True)

        self.assertRaisesWithStatus(requests.codes.bad_request,
            await client.http_client_failure.patch400, True)

        self.assertRaisesWithStatus(requests.codes.bad_request,
            await client.http_client_failure.post400, True)

        self.assertRaisesWithStatus(requests.codes.bad_request,
            await client.http_client_failure.delete400, True)

    @pytest.mark.asyncio
    async def test_error_status_codes_401(self, client):
        self.assertRaisesWithStatus(requests.codes.unauthorized,
            await client.http_client_failure.head401)

    @pytest.mark.asyncio
    async def test_error_status_codes_402(self, client):
        self.assertRaisesWithStatus(requests.codes.payment_required,
            await client.http_client_failure.get402)

    @pytest.mark.asyncio
    async def test_error_status_codes_403(self, client):
        # TODO, 4042586: Support options operations in swagger modeler
        #self.assertRaisesWithStatus(requests.codes.forbidden,
        #    await client.http_client_failure.options403)

        self.assertRaisesWithStatus(requests.codes.forbidden,
            await client.http_client_failure.get403)

    @pytest.mark.asyncio
    async def test_error_status_codes_404(self, client):
        self.assertRaisesWithStatus(requests.codes.not_found,
            await client.http_client_failure.put404, True)

    @pytest.mark.asyncio
    async def test_error_status_codes_405(self, client):
        self.assertRaisesWithStatus(requests.codes.method_not_allowed,
            await client.http_client_failure.patch405, True)

    @pytest.mark.asyncio
    async def test_error_status_codes_406(self, client):
        self.assertRaisesWithStatus(requests.codes.not_acceptable,
            await client.http_client_failure.post406, True)

    @pytest.mark.asyncio
    async def test_error_status_codes_407(self, client):
        self.assertRaisesWithStatus(requests.codes.proxy_authentication_required,
            await client.http_client_failure.delete407, True)

    @pytest.mark.asyncio
    async def test_error_status_codes_409(self, client):
        self.assertRaisesWithStatus(requests.codes.conflict,
            await client.http_client_failure.put409, True)

    @pytest.mark.asyncio
    async def test_error_status_codes_410(self, client):
        self.assertRaisesWithStatus(requests.codes.gone,
            await client.http_client_failure.head410)

    @pytest.mark.asyncio
    async def test_error_status_codes_411(self, client):
        self.assertRaisesWithStatus(requests.codes.length_required,
            await client.http_client_failure.get411)

        # TODO, 4042586: Support options operations in swagger modeler
        #self.assertRaisesWithStatus(requests.codes.precondition_failed,
        #    await client.http_client_failure.options412)

        self.assertRaisesWithStatus(requests.codes.precondition_failed,
            await client.http_client_failure.get412)

        self.assertRaisesWithStatus(requests.codes.request_entity_too_large,
            await client.http_client_failure.put413, True)

        self.assertRaisesWithStatus(requests.codes.request_uri_too_large,
            await client.http_client_failure.patch414, True)

        self.assertRaisesWithStatus(requests.codes.unsupported_media,
            await client.http_client_failure.post415, True)

        self.assertRaisesWithStatus(requests.codes.requested_range_not_satisfiable,
            await client.http_client_failure.get416)

        self.assertRaisesWithStatus(requests.codes.expectation_failed,
            await client.http_client_failure.delete417, True)

        self.assertRaisesWithStatus(429,
            await client.http_client_failure.head429)

    @pytest.mark.asyncio
    async def test_redirect_to_300(self, client):
        self.assertStatus(200, await client.http_redirects.get300)

    @pytest.mark.asyncio
    async def test_redirect_to_301(self, client):
        self.assertStatus(200, await client.http_redirects.head301)
        self.assertStatus(200, await client.http_redirects.get301)
        self.assertStatus(requests.codes.moved_permanently, await client.http_redirects.put301, True)

    @pytest.mark.asyncio
    async def test_redirect_to_302(self, client):
        self.assertStatus(200, await client.http_redirects.head302)
        self.assertStatus(200, await client.http_redirects.get302)
        self.assertStatus(requests.codes.found, await client.http_redirects.patch302, True)

    @pytest.mark.asyncio
    async def test_redicret_to_303(self, client):
        self.assertStatus(200, await client.http_redirects.post303, True)

    @pytest.mark.asyncio
    async def test_redirect_to_307(self, client):
        self.assertStatus(200, await client.http_redirects.head307)
        self.assertStatus(200, await client.http_redirects.get307)

        # TODO, 4042586: Support options operations in swagger modeler
        #self.assertStatus(200, await client.http_redirects.options307)
        self.assertStatus(200, await client.http_redirects.put307, True)
        self.assertStatus(200, await client.http_redirects.post307, True)
        self.assertStatus(200, await client.http_redirects.patch307, True)
        self.assertStatus(200, await client.http_redirects.delete307, True)

    @pytest.mark.asyncio
    async def test_bad_request_status_assert(self, client):
        self.assertRaisesWithMessage("Operation returned an invalid status 'Bad Request'",
            await client.http_failure.get_empty_error)

    @pytest.mark.asyncio
    async def test_no_error_model_status_assert(self, client):
        self.assertRaisesWithStatusAndResponseContains(requests.codes.bad_request, "NoErrorModel",
            await client.http_failure.get_no_model_error)

    @pytest.mark.asyncio
    async def test_success_status_codes_200(self, client):
        await client.http_success.head200()
        assert await client.http_success.get200()
        await client.http_success.put200(True)
        await client.http_success.post200(True)
        await client.http_success.patch200(True)
        await client.http_success.delete200(True)

        # TODO, 4042586: Support options operations in swagger modeler
        #assert await client.http_success.options200()

    @pytest.mark.asyncio
    async def test_success_status_codes_201(self, client):
        await client.http_success.put201(True)
        await client.http_success.post201(True)
    
    @pytest.mark.asyncio
    async def test_success_status_codes_202(self, client):
        await client.http_success.put202(True)
        await client.http_success.post202(True)
        await client.http_success.patch202(True)
        await client.http_success.delete202(True)

    @pytest.mark.asyncio
    async def test_success_status_codes_204(self, client):
        await client.http_success.head204()
        await client.http_success.put204(True)
        await client.http_success.post204(True)
        await client.http_success.delete204(True)
        await client.http_success.patch204(True)

    @pytest.mark.asyncio
    async def test_success_status_codes_404(self, client):
        await client.http_success.head404()
        