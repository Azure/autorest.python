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
from msrest.exceptions import DeserializationError

from httpinfrastructure import AutoRestHttpInfrastructureTestService
from httpinfrastructure.models import (
    A, B, C, D, ErrorException)

import pytest


@pytest.fixture()
def client():
    """Create a AutoRestHttpInfrastructureTestService client with test server credentials."""
    with AutoRestHttpInfrastructureTestService(base_url="http://localhost:3000") as client:
        yield client


class TestHttp(object):

    def assertStatus(self, code, func, *args, **kwargs):
        def return_status(response, data, headers):
            return response.status_code
        kwargs['cls'] = return_status
        status_code = func(*args, **kwargs)
        assert status_code == code

    def assertRaisesWithMessage(self, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            assert err.message == msg

    def assertRaisesWithModel(self, code, model, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            assert isinstance(err.error, model)
            assert err.response.status_code == code

    def assertRaisesWithStatus(self, code, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            assert err.response.status_code == code

    def assertRaisesWithStatusAndMessage(self, code, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            assert err.message == msg
            assert err.response.status_code == code

    def assertRaisesWithStatusAndResponseContains(self, code, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            pytest.fail()

        except HttpResponseError as err:
            assert err.response.status_code == code
            assert msg in err.response.text()

    def test_response_modeling(self, client):

        r = client.multiple_responses.get200_model204_no_model_default_error200_valid()
        assert '200' ==  r.status_code

        self.assertRaisesWithStatus(201,
            client.multiple_responses.get200_model204_no_model_default_error201_invalid)

        self.assertRaisesWithStatus(202,
            client.multiple_responses.get200_model204_no_model_default_error202_none)

        assert client.multiple_responses.get200_model204_no_model_default_error204_valid() is None

        self.assertRaisesWithStatusAndMessage(400, "client error",
            client.multiple_responses.get200_model204_no_model_default_error400_valid)

        self.assertStatus(200, client.multiple_responses.get200_model201_model_default_error200_valid)

        b_model = client.multiple_responses.get200_model201_model_default_error201_valid()
        assert b_model is not None
        assert b_model.status_code ==  "201"
        assert b_model.text_status_code ==  "Created"

        self.assertRaisesWithStatusAndMessage(400, "client error",
            client.multiple_responses.get200_model201_model_default_error400_valid)

        a_model = client.multiple_responses.get200_model_a201_model_c404_model_ddefault_error200_valid()
        assert a_model is not None
        assert a_model.status_code ==  "200"

        c_model = client.multiple_responses.get200_model_a201_model_c404_model_ddefault_error201_valid()
        assert c_model is not None
        assert c_model.http_code ==  "201"

        d_model = client.multiple_responses.get200_model_a201_model_c404_model_ddefault_error404_valid()
        assert d_model is not None
        assert d_model.http_status_code ==  "404"

        self.assertRaisesWithStatusAndMessage(400, "client error",
            client.multiple_responses.get200_model_a201_model_c404_model_ddefault_error400_valid)

        client.multiple_responses.get202_none204_none_default_error202_none()
        client.multiple_responses.get202_none204_none_default_error204_none()

        self.assertRaisesWithStatusAndMessage(400, "client error",
            client.multiple_responses.get202_none204_none_default_error400_valid)

        client.multiple_responses.get202_none204_none_default_none202_invalid()
        client.multiple_responses.get202_none204_none_default_none204_none()

        self.assertRaisesWithStatus(400,
            client.multiple_responses.get202_none204_none_default_none400_none)

        self.assertRaisesWithStatus(400,
            client.multiple_responses.get202_none204_none_default_none400_invalid)

        self.assertStatus(200, client.multiple_responses.get_default_model_a200_valid)

        assert client.multiple_responses.get_default_model_a200_none() is None
        client.multiple_responses.get_default_model_a200_valid()
        client.multiple_responses.get_default_model_a200_none()

        self.assertRaisesWithModel(400, A,
            client.multiple_responses.get_default_model_a400_valid)

        self.assertRaisesWithModel(400, A,
            client.multiple_responses.get_default_model_a400_none)

        client.multiple_responses.get_default_none200_invalid()
        client.multiple_responses.get_default_none200_none()

        self.assertRaisesWithStatus(400,
            client.multiple_responses.get_default_none400_invalid)

        self.assertRaisesWithStatus(400,
            client.multiple_responses.get_default_none400_none)

        assert client.multiple_responses.get200_model_a200_none() is None

        self.assertStatus(200, client.multiple_responses.get200_model_a200_valid)

        assert client.multiple_responses.get200_model_a200_invalid().status_code is None

        self.assertRaisesWithStatus(400,
            client.multiple_responses.get200_model_a400_none)
        self.assertRaisesWithStatus(400,
            client.multiple_responses.get200_model_a400_valid)
        self.assertRaisesWithStatus(400,
            client.multiple_responses.get200_model_a400_invalid)
        self.assertRaisesWithStatus(202,
            client.multiple_responses.get200_model_a202_valid)

    def test_server_error_status_codes(self, client):

        self.assertRaisesWithStatus(requests.codes.not_implemented,
            client.http_server_failure.head501)

        self.assertRaisesWithStatus(requests.codes.not_implemented,
            client.http_server_failure.get501)

        self.assertRaisesWithStatus(requests.codes.http_version_not_supported,
            client.http_server_failure.post505, True)

        self.assertRaisesWithStatus(requests.codes.http_version_not_supported,
            client.http_server_failure.delete505, True)

        client.http_retry.head408()
        client.http_retry.get502()

        # TODO, 4042586: Support options operations in swagger modeler
        #client.http_retry.options429()

        client.http_retry.put500(True)
        client.http_retry.patch500(True)
        client.http_retry.post503(True)
        client.http_retry.delete503(True)
        client.http_retry.put504(True)
        client.http_retry.patch504(True)

    def test_client_error_status_codes(self, client):

        self.assertRaisesWithStatus(requests.codes.bad_request,
            client.http_client_failure.head400)

        self.assertRaisesWithStatus(requests.codes.bad_request,
            client.http_client_failure.get400)

        # TODO, 4042586: Support options operations in swagger modeler
        #self.assertRaisesWithStatus(requests.codes.bad_request,
        #    client.http_client_failure.options400)

        self.assertRaisesWithStatus(requests.codes.bad_request,
            client.http_client_failure.put400, True)

        self.assertRaisesWithStatus(requests.codes.bad_request,
            client.http_client_failure.patch400, True)

        self.assertRaisesWithStatus(requests.codes.bad_request,
            client.http_client_failure.post400, True)

        self.assertRaisesWithStatus(requests.codes.bad_request,
            client.http_client_failure.delete400, True)

        self.assertRaisesWithStatus(requests.codes.unauthorized,
            client.http_client_failure.head401)

        self.assertRaisesWithStatus(requests.codes.payment_required,
            client.http_client_failure.get402)

        # TODO, 4042586: Support options operations in swagger modeler
        #self.assertRaisesWithStatus(requests.codes.forbidden,
        #    client.http_client_failure.options403)

        self.assertRaisesWithStatus(requests.codes.forbidden,
            client.http_client_failure.get403)

        self.assertRaisesWithStatus(requests.codes.not_found,
            client.http_client_failure.put404, True)

        self.assertRaisesWithStatus(requests.codes.method_not_allowed,
            client.http_client_failure.patch405, True)

        self.assertRaisesWithStatus(requests.codes.not_acceptable,
            client.http_client_failure.post406, True)

        self.assertRaisesWithStatus(requests.codes.proxy_authentication_required,
            client.http_client_failure.delete407, True)

        self.assertRaisesWithStatus(requests.codes.conflict,
            client.http_client_failure.put409, True)

        self.assertRaisesWithStatus(requests.codes.gone,
            client.http_client_failure.head410)

        self.assertRaisesWithStatus(requests.codes.length_required,
            client.http_client_failure.get411)

        # TODO, 4042586: Support options operations in swagger modeler
        #self.assertRaisesWithStatus(requests.codes.precondition_failed,
        #    client.http_client_failure.options412)

        self.assertRaisesWithStatus(requests.codes.precondition_failed,
            client.http_client_failure.get412)

        self.assertRaisesWithStatus(requests.codes.request_entity_too_large,
            client.http_client_failure.put413, True)

        self.assertRaisesWithStatus(requests.codes.request_uri_too_large,
            client.http_client_failure.patch414, True)

        self.assertRaisesWithStatus(requests.codes.unsupported_media,
            client.http_client_failure.post415, True)

        self.assertRaisesWithStatus(requests.codes.requested_range_not_satisfiable,
            client.http_client_failure.get416)

        self.assertRaisesWithStatus(requests.codes.expectation_failed,
            client.http_client_failure.delete417, True)

        self.assertRaisesWithStatus(429,
            client.http_client_failure.head429)

    def test_redirect_status_codes(self, client):

        self.assertStatus(200, client.http_redirects.get300)
        self.assertStatus(200, client.http_redirects.head302)
        self.assertStatus(200, client.http_redirects.head301)
        self.assertStatus(200, client.http_redirects.get301)

        self.assertStatus(requests.codes.moved_permanently, client.http_redirects.put301, True)
        self.assertStatus(200, client.http_redirects.get302)
        self.assertStatus(requests.codes.found, client.http_redirects.patch302, True)

        self.assertStatus(200, client.http_redirects.post303, True)
        self.assertStatus(200, client.http_redirects.head307)
        self.assertStatus(200, client.http_redirects.get307)

        # TODO, 4042586: Support options operations in swagger modeler
        #self.assertStatus(200, client.http_redirects.options307)
        self.assertStatus(200, client.http_redirects.put307, True)
        self.assertStatus(200, client.http_redirects.post307, True)
        self.assertStatus(200, client.http_redirects.patch307, True)
        self.assertStatus(200, client.http_redirects.delete307, True)

    def test_success_status_codes(self, client):

        self.assertRaisesWithMessage("Operation returned an invalid status code 'Bad Request'",
            client.http_failure.get_empty_error)
        self.assertRaisesWithStatusAndResponseContains(requests.codes.bad_request, "NoErrorModel",
            client.http_failure.get_no_model_error)
        client.http_success.head200()
        assert client.http_success.get200()
        client.http_success.put200(True)
        client.http_success.post200(True)
        client.http_success.patch200(True)
        client.http_success.delete200(True)

        # TODO, 4042586: Support options operations in swagger modeler
        #assert client.http_success.options200()

        client.http_success.put201(True)
        client.http_success.post201(True)
        client.http_success.put202(True)
        client.http_success.post202(True)
        client.http_success.patch202(True)
        client.http_success.delete202(True)
        client.http_success.head204()
        client.http_success.put204(True)
        client.http_success.post204(True)
        client.http_success.delete204(True)
        client.http_success.head404()
        client.http_success.patch204(True)


if __name__ == '__main__':
    unittest.main()
