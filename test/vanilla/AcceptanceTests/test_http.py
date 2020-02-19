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

from azure.core.exceptions import HttpResponseError
from azure.core.pipeline.policies import ContentDecodePolicy, RetryPolicy, HeadersPolicy, RedirectPolicy
from msrest.exceptions import DeserializationError

from httpinfrastructure import AutoRestHttpInfrastructureTestService
from httpinfrastructure.models import MyException, B, C, D

import pytest


@pytest.fixture()
def client(cookie_policy):
    """Create a AutoRestHttpInfrastructureTestService client with test server credentials."""
    policies = [
        HeadersPolicy(),
        ContentDecodePolicy(),
        RedirectPolicy(),
        RetryPolicy(),
        cookie_policy
    ]
    with AutoRestHttpInfrastructureTestService(base_url="http://localhost:3000", policies=policies) as client:
        yield client


class TestHttp(object):

    def assert_status(self, code, func, *args, **kwargs):
        def return_status(pipeline_response, data, headers):
            return pipeline_response.http_response.status_code
        kwargs['cls'] = return_status
        status_code = func(*args, **kwargs)
        assert status_code == code

    def assert_raises_with_message(self, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            assert err.message == msg

    def assert_raises_with_model(self, code, model, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            if err.model:
                assert isinstance(err.model, model)
            assert err.response.status_code == code

    def assert_raises_with_status(self, code, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            assert err.response.status_code == code

    def assert_raises_with_status_and_message(self, code, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            assert err.model.message == msg
            assert err.response.status_code == code

    def assert_raises_with_status_and_response_contains(self, code, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            assert err.response.status_code == code
            assert msg in err.response.text()

    def test_get200_model204(self, client):
        r = client.multiple_responses.get200_model204_no_model_default_error200_valid()
        assert '200' ==  r.status_code

        self.assert_raises_with_status(201,
            client.multiple_responses.get200_model204_no_model_default_error201_invalid)

        self.assert_raises_with_status(202,
            client.multiple_responses.get200_model204_no_model_default_error202_none)

        assert client.multiple_responses.get200_model204_no_model_default_error204_valid() is None

        self.assert_raises_with_status_and_message(400, "client error",
            client.multiple_responses.get200_model204_no_model_default_error400_valid)

    def test_get200_model201(self, client):
        self.assert_status(200, client.multiple_responses.get200_model201_model_default_error200_valid)

        b_model = client.multiple_responses.get200_model201_model_default_error201_valid()
        assert b_model is not None
        assert b_model.status_code ==  "201"
        assert b_model.text_status_code ==  "Created"

        self.assert_raises_with_status_and_message(400, "client error",
            client.multiple_responses.get200_model201_model_default_error400_valid)

    def test_get200_model_a201_model_c404(self, client):
        a_model = client.multiple_responses.get200_model_a201_model_c404_model_d_default_error200_valid()
        assert a_model is not None
        assert a_model.status_code ==  "200"

        c_model = client.multiple_responses.get200_model_a201_model_c404_model_d_default_error201_valid()
        assert c_model is not None
        assert c_model.http_code ==  "201"

        d_model = client.multiple_responses.get200_model_a201_model_c404_model_d_default_error404_valid()
        assert d_model is not None
        assert d_model.http_status_code ==  "404"

        self.assert_raises_with_status_and_message(400, "client error",
            client.multiple_responses.get200_model_a201_model_c404_model_d_default_error400_valid)

    def test_get202_none204(self, client):
        client.multiple_responses.get202_none204_none_default_error202_none()
        client.multiple_responses.get202_none204_none_default_error204_none()

        self.assert_raises_with_status_and_message(400, "client error",
            client.multiple_responses.get202_none204_none_default_error400_valid)

        client.multiple_responses.get202_none204_none_default_none202_invalid()
        client.multiple_responses.get202_none204_none_default_none204_none()

        self.assert_raises_with_status(400,
            client.multiple_responses.get202_none204_none_default_none400_none)

        self.assert_raises_with_status(400,
            client.multiple_responses.get202_none204_none_default_none400_invalid)

    def test_get_default_model_a200(self, client):
        self.assert_status(200, client.multiple_responses.get_default_model_a200_valid)

        assert client.multiple_responses.get_default_model_a200_none() is None
        client.multiple_responses.get_default_model_a200_valid()
        client.multiple_responses.get_default_model_a200_none()

    def test_get_default_model_a400(self, client):
        self.assert_raises_with_model(400, MyException,
            client.multiple_responses.get_default_model_a400_valid)

        self.assert_raises_with_model(400, MyException,
            client.multiple_responses.get_default_model_a400_none)

    def test_get_default_none200(self, client):
        client.multiple_responses.get_default_none200_invalid()
        client.multiple_responses.get_default_none200_none()

    def test_get_default_none400(self, client):
        self.assert_raises_with_status(400,
            client.multiple_responses.get_default_none400_invalid)

        self.assert_raises_with_status(400,
            client.multiple_responses.get_default_none400_none)

    def test_get200_model_a200(self, client):
        assert client.multiple_responses.get200_model_a200_none() is None

        self.assert_status(200, client.multiple_responses.get200_model_a200_valid)

        assert client.multiple_responses.get200_model_a200_invalid().status_code is None

    def test_get200_model_a400(self, client):
        self.assert_raises_with_status(400,
            client.multiple_responses.get200_model_a400_none)
        self.assert_raises_with_status(400,
            client.multiple_responses.get200_model_a400_valid)
        self.assert_raises_with_status(400,
            client.multiple_responses.get200_model_a400_invalid)

    def test_get200_model_a202(self, client):
        self.assert_raises_with_status(202,
            client.multiple_responses.get200_model_a202_valid)

    def test_server_error_status_codes_501(self, client):

        self.assert_raises_with_status(requests.codes.not_implemented,
            client.http_server_failure.head501)

        self.assert_raises_with_status(requests.codes.not_implemented,
            client.http_server_failure.get501)

    def test_server_error_status_codes_505(self, client):
        self.assert_raises_with_status(requests.codes.http_version_not_supported,
            client.http_server_failure.post505)

        self.assert_raises_with_status(requests.codes.http_version_not_supported,
            client.http_server_failure.delete505)

    def test_retry_status_codes_408(self, client):
        client.http_retry.head408()

    def test_retry_status_codes_502(self, client):
        client.http_retry.get502()

        # TODO, 4042586: Support options operations in swagger modeler
        #client.http_retry.options429()

    def test_retry_status_codes_500(self, client):
        client.http_retry.put500()
        client.http_retry.patch500()

    def test_retry_status_codes_503(self, client):
        client.http_retry.post503()
        client.http_retry.delete503()

    def test_retry_status_codes_504(self, client):
        client.http_retry.put504()
        client.http_retry.patch504()

    def test_error_status_codes_400(self, client):
        self.assert_raises_with_status(requests.codes.bad_request,
            client.http_client_failure.head400)

        self.assert_raises_with_status(requests.codes.bad_request,
            client.http_client_failure.get400)

        # TODO, 4042586: Support options operations in swagger modeler
        #self.assert_raises_with_status(requests.codes.bad_request,
        #    client.http_client_failure.options400)

        self.assert_raises_with_status(requests.codes.bad_request,
            client.http_client_failure.put400)

        self.assert_raises_with_status(requests.codes.bad_request,
            client.http_client_failure.patch400)

        self.assert_raises_with_status(requests.codes.bad_request,
            client.http_client_failure.post400)

        self.assert_raises_with_status(requests.codes.bad_request,
            client.http_client_failure.delete400)

    def test_error_status_codes_401(self, client):
        self.assert_raises_with_status(requests.codes.unauthorized,
            client.http_client_failure.head401)

    def test_error_status_codes_402(self, client):
        self.assert_raises_with_status(requests.codes.payment_required,
            client.http_client_failure.get402)

    def test_error_status_codes_403(self, client):
        # TODO, 4042586: Support options operations in swagger modeler
        #self.assert_raises_with_status(requests.codes.forbidden,
        #    client.http_client_failure.options403)

        self.assert_raises_with_status(requests.codes.forbidden,
            client.http_client_failure.get403)

    def test_error_status_codes_404(self, client):
        self.assert_raises_with_status(requests.codes.not_found,
            client.http_client_failure.put404)

    def test_error_status_codes_405(self, client):
        self.assert_raises_with_status(requests.codes.method_not_allowed,
            client.http_client_failure.patch405)

    def test_error_status_codes_406(self, client):
        self.assert_raises_with_status(requests.codes.not_acceptable,
            client.http_client_failure.post406)

    def test_error_status_codes_407(self, client):
        self.assert_raises_with_status(requests.codes.proxy_authentication_required,
            client.http_client_failure.delete407)

    def test_error_status_codes_409(self, client):
        self.assert_raises_with_status(requests.codes.conflict,
            client.http_client_failure.put409)

    def test_error_status_codes_410(self, client):
        self.assert_raises_with_status(requests.codes.gone,
            client.http_client_failure.head410)

    def test_error_status_codes_411(self, client):
        self.assert_raises_with_status(requests.codes.length_required,
            client.http_client_failure.get411)

        # TODO, 4042586: Support options operations in swagger modeler
        #self.assert_raises_with_status(requests.codes.precondition_failed,
        #    client.http_client_failure.options412)

        self.assert_raises_with_status(requests.codes.precondition_failed,
            client.http_client_failure.get412)

        self.assert_raises_with_status(requests.codes.request_entity_too_large,
            client.http_client_failure.put413)

        self.assert_raises_with_status(requests.codes.request_uri_too_large,
            client.http_client_failure.patch414)

        self.assert_raises_with_status(requests.codes.unsupported_media,
            client.http_client_failure.post415)

        self.assert_raises_with_status(requests.codes.requested_range_not_satisfiable,
            client.http_client_failure.get416)

        self.assert_raises_with_status(requests.codes.expectation_failed,
            client.http_client_failure.delete417)

        self.assert_raises_with_status(429,
            client.http_client_failure.head429)

    def test_redirect_to_300(self, client):
        self.assert_status(200, client.http_redirects.get300)

    def test_redirect_to_301(self, client):
        self.assert_status(200, client.http_redirects.head301)
        self.assert_status(200, client.http_redirects.get301)
        self.assert_status(requests.codes.moved_permanently, client.http_redirects.put301)

    def test_redirect_to_302(self, client):
        self.assert_status(200, client.http_redirects.head302)
        self.assert_status(200, client.http_redirects.get302)
        self.assert_status(requests.codes.found, client.http_redirects.patch302)

    def test_redicret_to_303(self, client):
        self.assert_status(200, client.http_redirects.post303)

    def test_redirect_to_307(self, client):
        self.assert_status(200, client.http_redirects.head307)
        self.assert_status(200, client.http_redirects.get307)

        # TODO, 4042586: Support options operations in swagger modeler
        #self.assert_status(200, client.http_redirects.options307)
        self.assert_status(200, client.http_redirects.put307)
        self.assert_status(200, client.http_redirects.post307)
        self.assert_status(200, client.http_redirects.patch307)
        self.assert_status(200, client.http_redirects.delete307)



    def test_bad_request_status_assert(self, client):
        self.assert_raises_with_message("Operation returned an invalid status 'Bad Request'",
            client.http_failure.get_empty_error)

    def test_no_error_model_status_assert(self, client):
        self.assert_raises_with_status_and_response_contains(requests.codes.bad_request, "NoErrorModel",
            client.http_failure.get_no_model_error)

    def test_success_status_codes_200(self, client):
        client.http_success.head200()
        assert client.http_success.get200()
        client.http_success.put200()
        client.http_success.post200()
        client.http_success.patch200()
        client.http_success.delete200()

        # TODO, 4042586: Support options operations in swagger modeler
        #assert client.http_success.options200()

    def test_success_status_codes_201(self, client):
        client.http_success.put201()
        client.http_success.post201()

    def test_success_status_codes_202(self, client):
        client.http_success.put202()
        client.http_success.post202()
        client.http_success.patch202()
        client.http_success.delete202()

    def test_success_status_codes_204(self, client):
        client.http_success.head204()
        client.http_success.put204()
        client.http_success.post204()
        client.http_success.delete204()
        client.http_success.patch204()

    def test_success_status_codes_404(self, client):
        client.http_success.head404()

    def test_empty_no_content(self, client):
        self.assert_raises_with_status(requests.codes.bad_request,
            client.http_failure.get_no_model_empty)
