# coding=utf-8
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
import pytest
from bodyformurlencodeddatalowlevel import BodyFormsDataURLEncoded
from bodyformurlencodeddatalowlevel.rest import formdataurlencoded

@pytest.fixture
def client():
    with BodyFormsDataURLEncoded() as client:
        yield client

@pytest.fixture
def send_request(client, base_send_request):
    def _send_request(request):
        return base_send_request(client, request)
    return _send_request

@pytest.mark.skip("We don't do urlencoded bodies anymore.")
def test_update_pet_with_form(send_request):
    request = formdataurlencoded.build_update_pet_with_form_request(
        pet_id=1,
        data={
            "pet_type": "dog",
            "pet_food": "meat",
            "pet_age": 42,
            "name": "Fido",
        }
    )
    send_request(request)

@pytest.mark.skip("We don't do urlencoded bodies anymore.")
def test_partial_constant_body(send_request):
    request = formdataurlencoded.build_partial_constant_body_request(
        data={
            "access_token": "foo",
            "grant_type": "access_token",
            "service": "bar"
        }
    )
    send_request(request)
