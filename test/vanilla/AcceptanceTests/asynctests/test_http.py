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

from msrest.exceptions import DeserializationError, HttpOperationError

from httpinfrastructure.aio import AutoRestHttpInfrastructureTestService
from httpinfrastructure.models import (
    A, B, C, D, ErrorException)

import pytest


@pytest.fixture()
def client():
    """Create a AutoRestHttpInfrastructureTestService client with test server credentials."""
    client = AutoRestHttpInfrastructureTestService(base_url="http://localhost:3000")
    return client

@pytest.fixture()
def special_client(client, test_session_callback):
    client.config.session_configuration_callback = test_session_callback
    return client

class TestHttp(object):

    async def assertStatus(self, code, func, *args, **kwargs):
        kwargs['raw'] = True
        raw = await func(*args, **kwargs)
        raw.response.status_code == code

    async def assertRaisesWithMessage(self, msg, func, *args, **kwargs):
        try:
            await func(*args, **kwargs)
            pytest.fail()

        except HttpOperationError as err:
            assert err.message == msg

    async def assertRaisesWithModel(self, code, model, func, *args, **kwargs):
        try:
            await func(*args, **kwargs)
            pytest.fail()

        except HttpOperationError as err:
            assert isinstance(err.error, model)
            assert err.response.status_code == code

    async def assertRaisesWithStatus(self, code, func, *args, **kwargs):
        try:
            await func(*args, **kwargs)
            pytest.fail()

        except HttpOperationError as err:
            assert err.response.status_code == code

    async def assertRaisesWithStatusAndMessage(self, code, msg, func, *args, **kwargs):
        try:
            await func(*args, **kwargs)
            pytest.fail()

        except HttpOperationError as err:
            assert err.message == msg
            assert err.response.status_code == code

    async def assertRaisesWithStatusAndResponseContains(self, code, msg, func, *args, **kwargs):
        try:
            await func(*args, **kwargs)
            pytest.fail()

        except HttpOperationError as err:
            assert err.response.status_code == code
            assert msg in err.response.content.decode("utf-8")

    @pytest.mark.asyncio
    async def test_response_modeling(self, client):

        r = await client.multiple_responses.get200_model204_no_model_default_error200_valid()
        assert '200' ==  r.status_code

        await self.assertRaisesWithStatus(201,
            client.multiple_responses.get200_model204_no_model_default_error201_invalid)

        await self.assertRaisesWithStatus(202,
            client.multiple_responses.get200_model204_no_model_default_error202_none)

        assert await client.multiple_responses.get200_model204_no_model_default_error204_valid() is None

        await self.assertRaisesWithStatusAndMessage(400, "client error",
            client.multiple_responses.get200_model204_no_model_default_error400_valid)

        await self.assertStatus(200, client.multiple_responses.get200_model201_model_default_error200_valid)

        b_model = await client.multiple_responses.get200_model201_model_default_error201_valid()
        assert b_model is not None
        assert b_model.status_code ==  "201"
        assert b_model.text_status_code ==  "Created"

        await self.assertRaisesWithStatusAndMessage(400, "client error",
            client.multiple_responses.get200_model201_model_default_error400_valid)

        a_model = await client.multiple_responses.get200_model_a201_model_c404_model_ddefault_error200_valid()
        assert a_model is not None
        assert a_model.status_code ==  "200"

        c_model = await client.multiple_responses.get200_model_a201_model_c404_model_ddefault_error201_valid()
        assert c_model is not None
        assert c_model.http_code ==  "201"

        d_model = await client.multiple_responses.get200_model_a201_model_c404_model_ddefault_error404_valid()
        assert d_model is not None
        assert d_model.http_status_code ==  "404"

        await self.assertRaisesWithStatusAndMessage(400, "client error",
            client.multiple_responses.get200_model_a201_model_c404_model_ddefault_error400_valid)

        await client.multiple_responses.get202_none204_none_default_error202_none()
        await client.multiple_responses.get202_none204_none_default_error204_none()

        await self.assertRaisesWithStatusAndMessage(400, "client error",
            client.multiple_responses.get202_none204_none_default_error400_valid)

        await client.multiple_responses.get202_none204_none_default_none202_invalid()
        await client.multiple_responses.get202_none204_none_default_none204_none()

        await self.assertRaisesWithStatus(400,
            client.multiple_responses.get202_none204_none_default_none400_none)

        await self.assertRaisesWithStatus(400,
            client.multiple_responses.get202_none204_none_default_none400_invalid)

        await self.assertStatus(200, client.multiple_responses.get_default_model_a200_valid)

        assert await client.multiple_responses.get_default_model_a200_none() is None
        await client.multiple_responses.get_default_model_a200_valid()
        await client.multiple_responses.get_default_model_a200_none()

        await self.assertRaisesWithModel(400, A,
            client.multiple_responses.get_default_model_a400_valid)

        await self.assertRaisesWithModel(400, A,
            client.multiple_responses.get_default_model_a400_none)

        await client.multiple_responses.get_default_none200_invalid()
        await client.multiple_responses.get_default_none200_none()

        await self.assertRaisesWithStatus(400,
            client.multiple_responses.get_default_none400_invalid)

        await self.assertRaisesWithStatus(400,
            client.multiple_responses.get_default_none400_none)

        assert await client.multiple_responses.get200_model_a200_none() is None

        await self.assertStatus(200, client.multiple_responses.get200_model_a200_valid)

        assert (await client.multiple_responses.get200_model_a200_invalid()).status_code is None

        await self.assertRaisesWithStatus(400,
            client.multiple_responses.get200_model_a400_none)
        await self.assertRaisesWithStatus(400,
            client.multiple_responses.get200_model_a400_valid)
        await self.assertRaisesWithStatus(400,
            client.multiple_responses.get200_model_a400_invalid)
        await self.assertRaisesWithStatus(202,
            client.multiple_responses.get200_model_a202_valid)

    @pytest.mark.asyncio
    async def test_server_error_status_codes(self, special_client):
        client = special_client

        await self.assertRaisesWithStatus(requests.codes.not_implemented,
            client.http_server_failure.head501)

        await self.assertRaisesWithStatus(requests.codes.not_implemented,
            client.http_server_failure.get501)

        await self.assertRaisesWithStatus(requests.codes.http_version_not_supported,
            client.http_server_failure.post505, True)

        await self.assertRaisesWithStatus(requests.codes.http_version_not_supported,
            client.http_server_failure.delete505, True)

        await client.http_retry.head408()
        await client.http_retry.get502()

        # TODO, 4042586: Support options operations in swagger modeler
        #await client.http_retry.options429()

        await client.http_retry.put500(True)
        await client.http_retry.patch500(True)
        await client.http_retry.post503(True)
        await client.http_retry.delete503(True)
        await client.http_retry.put504(True)
        await client.http_retry.patch504(True)

    @pytest.mark.asyncio
    async def test_client_error_status_codes(self, client):

        await self.assertRaisesWithStatus(requests.codes.bad_request,
            client.http_client_failure.head400)

        await self.assertRaisesWithStatus(requests.codes.bad_request,
            client.http_client_failure.get400)

        # TODO, 4042586: Support options operations in swagger modeler
        #await self.assertRaisesWithStatus(requests.codes.bad_request,
        #    client.http_client_failure.options400)

        await self.assertRaisesWithStatus(requests.codes.bad_request,
            client.http_client_failure.put400, True)

        await self.assertRaisesWithStatus(requests.codes.bad_request,
            client.http_client_failure.patch400, True)

        await self.assertRaisesWithStatus(requests.codes.bad_request,
            client.http_client_failure.post400, True)

        await self.assertRaisesWithStatus(requests.codes.bad_request,
            client.http_client_failure.delete400, True)

        await self.assertRaisesWithStatus(requests.codes.unauthorized,
            client.http_client_failure.head401)

        await self.assertRaisesWithStatus(requests.codes.payment_required,
            client.http_client_failure.get402)

        # TODO, 4042586: Support options operations in swagger modeler
        #await self.assertRaisesWithStatus(requests.codes.forbidden,
        #    client.http_client_failure.options403)

        await self.assertRaisesWithStatus(requests.codes.forbidden,
            client.http_client_failure.get403)

        await self.assertRaisesWithStatus(requests.codes.not_found,
            client.http_client_failure.put404, True)

        await self.assertRaisesWithStatus(requests.codes.method_not_allowed,
            client.http_client_failure.patch405, True)

        await self.assertRaisesWithStatus(requests.codes.not_acceptable,
            client.http_client_failure.post406, True)

        await self.assertRaisesWithStatus(requests.codes.proxy_authentication_required,
            client.http_client_failure.delete407, True)

        await self.assertRaisesWithStatus(requests.codes.conflict,
            client.http_client_failure.put409, True)

        await self.assertRaisesWithStatus(requests.codes.gone,
            client.http_client_failure.head410)

        await self.assertRaisesWithStatus(requests.codes.length_required,
            client.http_client_failure.get411)

        # TODO, 4042586: Support options operations in swagger modeler
        #await self.assertRaisesWithStatus(requests.codes.precondition_failed,
        #    await client.http_client_failure.options412)

        await self.assertRaisesWithStatus(requests.codes.precondition_failed,
            client.http_client_failure.get412)

        await self.assertRaisesWithStatus(requests.codes.request_entity_too_large,
            client.http_client_failure.put413, True)

        await self.assertRaisesWithStatus(requests.codes.request_uri_too_large,
            client.http_client_failure.patch414, True)

        await self.assertRaisesWithStatus(requests.codes.unsupported_media,
            client.http_client_failure.post415, True)

        await self.assertRaisesWithStatus(requests.codes.requested_range_not_satisfiable,
            client.http_client_failure.get416)

        await self.assertRaisesWithStatus(requests.codes.expectation_failed,
            client.http_client_failure.delete417, True)

        await self.assertRaisesWithStatus(429,
            client.http_client_failure.head429)

    @pytest.mark.asyncio
    async def test_redirect_status_codes(self, client):

        # requests does NOT redirect on 300. We is ok with the HTTP
        # spec that is fuzzy about this. Let's keep it that way for now.
        await self.assertStatus(300, client.http_redirects.get300)

        await self.assertStatus(200, client.http_redirects.head302)
        await self.assertStatus(200, client.http_redirects.head301)
        await self.assertStatus(200, client.http_redirects.get301)

        await self.assertStatus(requests.codes.moved_permanently, client.http_redirects.put301, True)
        await self.assertStatus(200, client.http_redirects.get302)
        await self.assertStatus(requests.codes.found, client.http_redirects.patch302, True)

        await self.assertStatus(200, client.http_redirects.post303, True)
        await self.assertStatus(200, client.http_redirects.head307)
        await self.assertStatus(200, client.http_redirects.get307)

        # TODO, 4042586: Support options operations in swagger modeler
        #await self.assertStatus(200, client.http_redirects.options307)
        await self.assertStatus(200, client.http_redirects.put307, True)
        await self.assertStatus(200, client.http_redirects.post307, True)
        await self.assertStatus(200, client.http_redirects.patch307, True)
        await self.assertStatus(200, client.http_redirects.delete307, True)

    @pytest.mark.asyncio
    async def test_success_status_codes(self, client):

        await self.assertRaisesWithMessage("Operation returned an invalid status code 'Bad Request'",
            client.http_failure.get_empty_error)
        await self.assertRaisesWithStatusAndResponseContains(requests.codes.bad_request, "NoErrorModel",
            client.http_failure.get_no_model_error)
        await client.http_success.head200()
        assert await client.http_success.get200()
        await client.http_success.put200(True)
        await client.http_success.post200(True)
        await client.http_success.patch200(True)
        await client.http_success.delete200(True)

        # TODO, 4042586: Support options operations in swagger modeler
        #assert await client.http_success.options200()

        await client.http_success.put201(True)
        await client.http_success.post201(True)
        await client.http_success.put202(True)
        await client.http_success.post202(True)
        await client.http_success.patch202(True)
        await client.http_success.delete202(True)
        await client.http_success.head204()
        await client.http_success.put204(True)
        await client.http_success.post204(True)
        await client.http_success.delete204(True)
        await client.http_success.head404()
        await client.http_success.patch204(True)
