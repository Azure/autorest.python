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

import requests
from async_generator import yield_, async_generator

from azure.core.exceptions import HttpResponseError
from azure.core.pipeline.policies import ContentDecodePolicy, AsyncRetryPolicy, HeadersPolicy, AsyncRedirectPolicy

from httpinfrastructurelowlevel.aio import AutoRestHttpInfrastructureTestService
from httpinfrastructurelowlevel.rest import (
    multiple_responses,
    http_server_failure,
    http_failure,
    http_redirects,
    http_retry,
    http_success,
    http_client_failure,
)

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

@pytest.fixture
def send_request(client, base_send_request):
    async def _send_request(request):
        return await base_send_request(client, request)
    return _send_request

@pytest.fixture
def send_request_json_response(client, base_send_request_json_response):
    async def _send_request(request):
        return await base_send_request_json_response(client, request)
    return _send_request

@pytest.fixture
def send_request_assert_status(client, base_send_request):
    async def _send_request(request, status_code):
        response = await base_send_request(client, request)
        assert response.status_code == status_code
    return _send_request

@pytest.fixture
def send_request_assert_raises_with_message(client, base_send_request):
    async def _send_request(request, message):
        with pytest.raises(HttpResponseError) as ex:
            await base_send_request(client, request)
        assert ex.value.message == message
    return _send_request

@pytest.fixture
def send_request_assert_raises_with_status(client, base_send_request):
    async def _send_request(request, status_code):
        with pytest.raises(HttpResponseError) as ex:
            await base_send_request(client, request)
        assert ex.value.status_code == status_code
    return _send_request

@pytest.fixture
def send_request_assert_raises_with_status_and_message(client, base_send_request):
    async def _send_request(request, status_code, message):
        with pytest.raises(HttpResponseError) as ex:
            await base_send_request(client, request)
        assert ex.value.status_code == status_code
        assert ex.value.message == message
        assert message in str(ex.value)
    return _send_request

@pytest.fixture
def send_request_assert_raises_with_status_and_response_contains_message(client, base_send_request):
    async def _send_request(request, status_code, message):
        with pytest.raises(HttpResponseError) as ex:
            await base_send_request(client, request)
        assert ex.value.status_code == status_code
        assert ex.value.response.json()['message'] == message
    return _send_request

@pytest.mark.asyncio
async def test_get200_model204(send_request, send_request_assert_status, send_request_assert_raises_with_status_and_response_contains_message):
    # a lot of these tests raised in high level bc we made some 200 status codes errors in high level
    # can't do this in low level, so these don't actually raise
    request = multiple_responses.build_get200_model204_no_model_default_error200_valid_request()
    await send_request_assert_status(request, 200)

    request = multiple_responses.build_get200_model204_no_model_default_error201_invalid_request()
    await send_request_assert_status(request, 201)

    request = multiple_responses.build_get200_model204_no_model_default_error202_none_request()
    await send_request_assert_status(request, 202)

    request = multiple_responses.build_get200_model204_no_model_default_error204_valid_request()

    assert (await send_request(request)).text == ''

    request = multiple_responses.build_get200_model204_no_model_default_error400_valid_request()
    await send_request_assert_raises_with_status_and_response_contains_message(request, 400, "client error")

@pytest.mark.asyncio
async def test_get200_model201(send_request_json_response, send_request_assert_status, send_request_assert_raises_with_status_and_response_contains_message):
    request = multiple_responses.build_get200_model201_model_default_error200_valid_request()
    await send_request_assert_status(request, 200)

    request = multiple_responses.build_get200_model201_model_default_error201_valid_request()
    b_model = await send_request_json_response(request)
    assert b_model is not None
    assert b_model['statusCode'] ==  "201"
    assert b_model['textStatusCode'] ==  "Created"

    request = multiple_responses.build_get200_model201_model_default_error400_valid_request()
    await send_request_assert_raises_with_status_and_response_contains_message(request, 400, "client error")

@pytest.mark.asyncio
async def test_get200_model_a201_model_c404(send_request_json_response, send_request_assert_raises_with_status_and_response_contains_message, send_request_assert_raises_with_status):
    request = multiple_responses.build_get200_model_a201_model_c404_model_d_default_error200_valid_request()
    a_model = await send_request_json_response(request)
    assert a_model['statusCode']==  "200"

    request = multiple_responses.build_get200_model_a201_model_c404_model_d_default_error201_valid_request()

    c_model = await send_request_json_response(request)
    assert c_model['httpCode'] ==  "201"

    request = multiple_responses.build_get200_model_a201_model_c404_model_d_default_error404_valid_request()
    await send_request_assert_raises_with_status(request, 404)  # in high level, this doesn't raise and returns a model since we've made 404 a valid status code. can't do that in llc

    request = multiple_responses.build_get200_model_a201_model_c404_model_d_default_error400_valid_request()
    await send_request_assert_raises_with_status_and_response_contains_message(request, 400, "client error")

@pytest.mark.asyncio
async def test_get202_none204(send_request, send_request_assert_raises_with_status, send_request_assert_raises_with_status_and_response_contains_message):
    request = multiple_responses.build_get202_none204_none_default_error202_none_request()
    await send_request(request)

    request = multiple_responses.build_get202_none204_none_default_error204_none_request()
    await send_request(request)

    request = multiple_responses.build_get202_none204_none_default_error400_valid_request()
    await send_request_assert_raises_with_status_and_response_contains_message(request, 400, "client error")

    request = multiple_responses.build_get202_none204_none_default_none202_invalid_request()
    await send_request(request)

    request = multiple_responses.build_get202_none204_none_default_none204_none_request()
    await send_request(request)

    request = multiple_responses.build_get202_none204_none_default_none400_none_request()
    await send_request_assert_raises_with_status(request, 400)

    request = multiple_responses.build_get202_none204_none_default_none400_invalid_request()
    await send_request_assert_raises_with_status(request, 400)

@pytest.mark.asyncio
async def test_get_default_model_a200(send_request, send_request_assert_status):
    request = multiple_responses.build_get_default_model_a200_valid_request()
    await send_request_assert_status(request, 200)

    request = multiple_responses.build_get_default_model_a200_none_request()
    assert (await send_request(request)).text == ''

    request = multiple_responses.build_get_default_model_a200_valid_request()
    await send_request(request)
    request = multiple_responses.build_get_default_model_a200_none_request()
    await send_request(request)

@pytest.mark.asyncio
async def test_get_default_none200(send_request):
    request = multiple_responses.build_get_default_none200_invalid_request()
    await send_request(request)

    requst = multiple_responses.build_get_default_none200_none_request()
    await send_request(request)

@pytest.mark.asyncio
async def test_get_default_none400(send_request_assert_raises_with_status):
    request = multiple_responses.build_get_default_none400_invalid_request()
    await send_request_assert_raises_with_status(request, 400)

    request = multiple_responses.build_get_default_none400_none_request()
    await send_request_assert_raises_with_status(request, 400)

@pytest.mark.asyncio
async def test_get200_model_a200(send_request, send_request_assert_status):
    request = multiple_responses.build_get200_model_a200_none_request()
    assert (await send_request(request)).text == ''

    request = multiple_responses.build_get200_model_a200_valid_request()
    await send_request_assert_status(request, 200)

    request = multiple_responses.build_get200_model_a200_invalid_request()
    await send_request_assert_status(request, 200) # in high level it's supposed to deserialize as exception model "MyException", can't do that in LLC

@pytest.mark.asyncio
async def test_get200_model_a400(send_request_assert_raises_with_status):
    request = multiple_responses.build_get200_model_a400_none_request()
    await send_request_assert_raises_with_status(request, 400)

    request = multiple_responses.build_get200_model_a400_valid_request()
    await send_request_assert_raises_with_status(request, 400)

    request = multiple_responses.build_get200_model_a400_invalid_request()
    await send_request_assert_raises_with_status(request, 400)

@pytest.mark.asyncio
async def test_get200_model_a202(send_request_assert_status):
    request = multiple_responses.build_get200_model_a202_valid_request()
    await send_request_assert_status(request, 202)  # raises in HLC bc we've marked all status codes that are not "200" as errors

@pytest.mark.asyncio
async def test_server_error_status_codes_501(send_request_assert_raises_with_status):
    request = http_server_failure.build_head501_request()
    await send_request_assert_raises_with_status(request, requests.codes.not_implemented)

    request = http_server_failure.build_get501_request()
    await send_request_assert_raises_with_status(request, requests.codes.not_implemented)

@pytest.mark.asyncio
async def test_server_error_status_codes_505(send_request_assert_raises_with_status):
    request = http_server_failure.build_post505_request()
    await send_request_assert_raises_with_status(request, requests.codes.http_version_not_supported)

    request = http_server_failure.build_delete505_request()
    await send_request_assert_raises_with_status(request, requests.codes.http_version_not_supported)

@pytest.mark.asyncio
async def test_retry_status_codes_408(send_request):
    request = http_retry.build_head408_request()
    await send_request(request)

@pytest.mark.asyncio
async def test_retry_status_codes_502(send_request):
    request = http_retry.build_get502_request()
    await send_request(request)

    # TODO, 4042586: Support options operations in swagger modeler
    #client.http_retry.options429()

@pytest.mark.asyncio
async def test_retry_status_codes_500(send_request):
    request = http_retry.build_put500_request()
    await send_request(request)
    request = http_retry.build_patch500_request()
    await send_request(request)

@pytest.mark.asyncio
async def test_retry_status_codes_503(send_request):
    request = http_retry.build_post503_request()
    await send_request(request)

    request = http_retry.build_delete503_request()
    await send_request(request)

@pytest.mark.asyncio
async def test_retry_status_codes_504(send_request):
    request = http_retry.build_put504_request()
    await send_request(request)

    request = http_retry.build_patch504_request()
    await send_request(request)

@pytest.mark.asyncio
async def test_error_status_codes_400(send_request_assert_raises_with_status):
    request = http_client_failure.build_head400_request()
    await send_request_assert_raises_with_status(request, requests.codes.bad_request)

    request = http_client_failure.build_get400_request()
    await send_request_assert_raises_with_status(request, requests.codes.bad_request)

    # TODO, 4042586: Support options operations in swagger modeler
    #self.assert_raises_with_status(requests.codes.bad_request,
    #    client.http_client_failure.options400)

    request = http_client_failure.build_put400_request()
    await send_request_assert_raises_with_status(request, requests.codes.bad_request)

    request = http_client_failure.build_patch400_request()
    await send_request_assert_raises_with_status(request, requests.codes.bad_request)

    request = http_client_failure.build_post400_request()
    await send_request_assert_raises_with_status(request, requests.codes.bad_request)

    request = http_client_failure.build_delete400_request()
    await send_request_assert_raises_with_status(request, requests.codes.bad_request)

@pytest.mark.asyncio
async def test_error_status_codes_401(send_request_assert_raises_with_status):
    request = http_client_failure.build_head401_request()
    await send_request_assert_raises_with_status(request, requests.codes.unauthorized)

@pytest.mark.asyncio
async def test_error_status_codes_402(send_request_assert_raises_with_status):
    request = http_client_failure.build_get402_request()
    await send_request_assert_raises_with_status(request, requests.codes.payment_required)

@pytest.mark.asyncio
async def test_error_status_codes_403(send_request_assert_raises_with_status):
    # TODO, 4042586: Support options operations in swagger modeler
    #self.assert_raises_with_status(requests.codes.forbidden,
    #    client.http_client_failure.options403)

    request = http_client_failure.build_get403_request()
    await send_request_assert_raises_with_status(request, requests.codes.forbidden)

@pytest.mark.asyncio
async def test_error_status_codes_404(send_request_assert_raises_with_status):
    request = http_client_failure.build_put404_request()
    await send_request_assert_raises_with_status(request, requests.codes.not_found)

@pytest.mark.asyncio
async def test_error_status_codes_405(send_request_assert_raises_with_status):
    request = http_client_failure.build_patch405_request()
    await send_request_assert_raises_with_status(request, requests.codes.method_not_allowed)

@pytest.mark.asyncio
async def test_error_status_codes_406(send_request_assert_raises_with_status):
    request = http_client_failure.build_post406_request()
    await send_request_assert_raises_with_status(request, requests.codes.not_acceptable)

@pytest.mark.asyncio
async def test_error_status_codes_407(send_request_assert_raises_with_status):
    request = http_client_failure.build_delete407_request()
    await send_request_assert_raises_with_status(request, requests.codes.proxy_authentication_required)

@pytest.mark.asyncio
async def test_error_status_codes_409(send_request_assert_raises_with_status):
    request = http_client_failure.build_put409_request()
    await send_request_assert_raises_with_status(request, requests.codes.conflict)

@pytest.mark.asyncio
async def test_error_status_codes_410(send_request_assert_raises_with_status):
    request = http_client_failure.build_head410_request()
    await send_request_assert_raises_with_status(request, requests.codes.gone)

@pytest.mark.asyncio
async def test_error_status_codes_411(send_request_assert_raises_with_status):

    request = http_client_failure.build_get411_request()
    await send_request_assert_raises_with_status(request, requests.codes.length_required)

    # TODO, 4042586: Support options operations in swagger modeler
    #self.assert_raises_with_status(requests.codes.precondition_failed,
    #    client.http_client_failure.options412)

    request = http_client_failure.build_get412_request()
    await send_request_assert_raises_with_status(request, requests.codes.precondition_failed)

    request = http_client_failure.build_put413_request()
    await send_request_assert_raises_with_status(request, requests.codes.request_entity_too_large)

    request = http_client_failure.build_patch414_request()
    await send_request_assert_raises_with_status(request, requests.codes.request_uri_too_large)

    request = http_client_failure.build_post415_request()
    await send_request_assert_raises_with_status(request, requests.codes.unsupported_media)

    request = http_client_failure.build_get416_request()
    await send_request_assert_raises_with_status(request, requests.codes.requested_range_not_satisfiable)

    request = http_client_failure.build_delete417_request()
    await send_request_assert_raises_with_status(request, requests.codes.expectation_failed)

    request = http_client_failure.build_head429_request()
    await send_request_assert_raises_with_status(request, 429)

@pytest.mark.asyncio
async def test_redirect_to_300(send_request_assert_status):
    request = http_redirects.build_get300_request()
    await send_request_assert_status(request, 200)

@pytest.mark.asyncio
async def test_redirect_to_301(send_request_assert_status):
    request = http_redirects.build_head301_request()
    await send_request_assert_status(request, 200)


    request = http_redirects.build_get301_request()
    await send_request_assert_status(request, 200)

    request = http_redirects.build_put301_request()
    await send_request_assert_status(request, requests.codes.moved_permanently)

@pytest.mark.asyncio
async def test_redirect_to_302(send_request_assert_status):
    request = http_redirects.build_head302_request()
    await send_request_assert_status(request, 200)

    request = http_redirects.build_get302_request()
    await send_request_assert_status(request, 200)

    request = http_redirects.build_patch302_request()
    await send_request_assert_status(request, requests.codes.found)

@pytest.mark.asyncio
async def test_redicret_to_303(send_request_assert_status):
    request = http_redirects.build_post303_request()
    await send_request_assert_status(request, 200)

@pytest.mark.asyncio
async def test_redirect_to_307(send_request_assert_status):
    request = http_redirects.build_head307_request()
    await send_request_assert_status(request, 200)

    request = http_redirects.build_get307_request()
    await send_request_assert_status(request, 200)

    # TODO, 4042586: Support options operations in swagger modeler
    #self.assert_status(200, client.http_redirects.options307)
    request = http_redirects.build_put307_request()
    await send_request_assert_status(request, 200)

    request = http_redirects.build_post307_request()
    await send_request_assert_status(request, 200)

    request = http_redirects.build_patch307_request()
    await send_request_assert_status(request, 200)

    request = http_redirects.build_delete307_request()
    await send_request_assert_status(request, 200)

@pytest.mark.asyncio
async def test_bad_request_status_assert(send_request_assert_raises_with_message):
    request = http_failure.build_get_empty_error_request()
    await send_request_assert_raises_with_message(request, "Operation returned an invalid status 'Bad Request'")

@pytest.mark.asyncio
async def test_no_error_model_status_assert(send_request_assert_raises_with_status_and_response_contains_message):
    request = http_failure.build_get_no_model_error_request()
    await send_request_assert_raises_with_status_and_response_contains_message(request, requests.codes.bad_request, "NoErrorModel")

@pytest.mark.asyncio
async def test_success_status_codes_200(send_request):
    request = http_success.build_head200_request()
    await send_request(request)
    request = http_success.build_get200_request()
    assert (await send_request(request)).text

    request = http_success.build_put200_request()
    await send_request(request)

    request = http_success.build_post200_request()
    await send_request(request)

    request = http_success.build_patch200_request()
    await send_request(request)

    request = http_success.build_delete200_request()
    await send_request(request)

    # TODO, 4042586: Support options operations in swagger modeler
    #assert client.http_success.options200()

@pytest.mark.asyncio
async def test_success_status_codes_201(send_request):
    request = http_success.build_put201_request()
    await send_request(request)

    request = http_success.build_post201_request()
    await send_request(request)

@pytest.mark.asyncio
async def test_success_status_codes_202(send_request):
    request = http_success.build_put202_request()
    await send_request(request)

    request = http_success.build_post202_request()
    await send_request(request)

    request = http_success.build_patch202_request()
    await send_request(request)

    request = http_success.build_delete202_request()
    await send_request(request)

@pytest.mark.asyncio
async def test_success_status_codes_204(send_request):
    request = http_success.build_head204_request()
    await send_request(request)

    request = http_success.build_put204_request()
    await send_request(request)

    request = http_success.build_post204_request()
    await send_request(request)

    request = http_success.build_delete204_request()
    await send_request(request)

    request = http_success.build_patch204_request()
    await send_request(request)

@pytest.mark.asyncio
async def test_success_status_codes_404(send_request_assert_raises_with_status):
    # raises bc in high level we're able to mark 404 as a valid status code, but can't do that in llc
    request = http_success.build_head404_request()
    await send_request_assert_raises_with_status(request, 404)

@pytest.mark.asyncio
async def test_empty_no_content(send_request_assert_raises_with_status):
    request = http_failure.build_get_no_model_empty_request()
    await send_request_assert_raises_with_status(request, requests.codes.bad_request)
