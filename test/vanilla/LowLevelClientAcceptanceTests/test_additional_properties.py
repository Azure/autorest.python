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
from additionalproperties import AdditionalPropertiesClient
from additionalproperties.models import (
    PetAPTrue,
    CatAPTrue,
    PetAPObject,
    PetAPString,
    PetAPInProperties,
    PetAPInPropertiesWithAPString
)
from additionalproperties.rest.pets import *

@pytest.fixture
def client():
    with AdditionalPropertiesClient(base_url="http://localhost:3000") as client:
        yield client

@pytest.fixture
def make_request_json_response(client, base_make_request_json_response):
    def _make_request(request):
        return base_make_request_json_response(client, request)
    return _make_request

def test_create_ap_true(make_request_json_response):
    input_ap_true = PetAPTrue(
        id = 1,
        name = 'Puppy',
        additional_properties = {
            'birthdate': '2017-12-13T02:29:51Z',
            'complexProperty': {
                'color': 'Red'
            }
        }
    )
    request = build_create_ap_true_request(json=input_ap_true.serialize())
    response = make_request_json_response(request)
    assert response["birthdate"] == '2017-12-13T02:29:51Z'

def test_create_cat_ap_true(make_request_json_response):
    input_ap_true = CatAPTrue(
        id = 1,
        name = 'Lisa',
        friendly = True,
        additional_properties = {
            'birthdate': '2017-12-13T02:29:51Z',
            'complexProperty': {
                'color': 'Red'
            }
        }
    )
    request = build_create_cat_ap_true_request(json=input_ap_true.serialize())
    response = make_request_json_response(request)
    assert response['birthdate'] ==  '2017-12-13T02:29:51Z'

def test_create_ap_object(make_request_json_response):
    input_ap_obj = PetAPObject(
        id = 2,
        name = 'Hira',
        additional_properties = {
            'siblings': [{
                'id': 1,
                'name': 'Puppy',
                'birthdate': '2017-12-13T02:29:51Z',
                'complexProperty': {
                    'color': 'Red'
                }
            }],
            'picture': '//////4='
        }
    )
    request = build_create_ap_object_request(json=input_ap_obj.serialize())
    response = make_request_json_response(request)
    assert response['siblings'][0]['birthdate'] ==  '2017-12-13T02:29:51Z'

def test_create_ap_string(make_request_json_response):
    input_ap_str = PetAPString(
        id = 3,
        name = 'Tommy',
        additional_properties = {
            'color': 'red',
            'weight': '10 kg',
            'city': 'Bombay'
        }
    )
    request = build_create_ap_string_request(json=input_ap_str.serialize())
    response = make_request_json_response(request)
    assert response['color'] ==  'red'

def test_create_ap_in_properties(make_request_json_response):
    input_ap_int = PetAPInProperties(
        id = 4,
        name = 'Bunny',
        additional_properties = {
            'height': 5.61,
            'weight': 599,
            'footsize': 11.5
        }
    )
    request = build_create_ap_in_properties_request(json=input_ap_int.serialize())
    response = make_request_json_response(request)
    assert response["additionalProperties"]['weight'] ==  599

def test_create_ap_in_properties_with_ap_string(make_request_json_response):
    input_ap_str_add = PetAPInPropertiesWithAPString(
        id = 5,
        name = 'Funny',
        odata_location = 'westus',
        additional_properties = {
            'color': 'red',
            'city': 'Seattle',
            'food': 'tikka masala'
        },
        additional_properties1 = {
            'height': 5.61,
            'weight': 599,
            'footsize': 11.5
        }
    )
    request = build_create_ap_in_properties_with_ap_string_request(json=input_ap_str_add.serialize())
    response = make_request_json_response(request)
    assert response['color'] == 'red'
    assert response['additionalProperties']['weight'] == 599