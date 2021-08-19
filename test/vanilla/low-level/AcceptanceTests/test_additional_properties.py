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
from additionalpropertieslowlevel import AdditionalPropertiesClient
from additionalpropertieslowlevel.rest import pets

@pytest.fixture
def client():
    with AdditionalPropertiesClient(endpoint="http://localhost:3000") as client:
        yield client

@pytest.fixture
def send_request_json_response(client, base_send_request_json_response):
    def _send_request(request):
        return base_send_request_json_response(client, request)
    return _send_request

def test_create_ap_true(send_request_json_response):
    json = {
        'birthdate': '2017-12-13T02:29:51Z',
        'complexProperty': {
            'color': 'Red'
        },
        "id": 1,
        "name": "Puppy",
    }
    request = pets.build_create_ap_true_request(json=json)
    response = send_request_json_response(request)
    assert response["birthdate"] == '2017-12-13T02:29:51Z'

def test_create_cat_ap_true(send_request_json_response):
    json = {
        'birthdate': '2017-12-13T02:29:51Z',
        'complexProperty': {'color': 'Red'},
        'id': 1,
        'name': 'Lisa',
        'friendly': True
    }
    request = pets.build_create_cat_ap_true_request(json=json)
    response = send_request_json_response(request)
    assert response['birthdate'] ==  '2017-12-13T02:29:51Z'

def test_create_ap_object(send_request_json_response):
    json = {
        "id": 2,
        "name": "Hira",
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
    request = pets.build_create_ap_object_request(json=json)
    response = send_request_json_response(request)
    assert response['siblings'][0]['birthdate'] ==  '2017-12-13T02:29:51Z'

def test_create_ap_string(send_request_json_response):
    json = {
        "id": 3,
        "name": 'Tommy',
        'color': 'red',
        'weight': '10 kg',
        'city': 'Bombay'
    }
    request = pets.build_create_ap_string_request(json=json)
    response = send_request_json_response(request)
    assert response['color'] ==  'red'

def test_create_ap_in_properties(send_request_json_response):
    json = {
        "id": 4,
        "name": 'Bunny',
        "additionalProperties": {
            'height': 5.61,
            'weight': 599,
            'footsize': 11.5
        }
    }
    request = pets.build_create_ap_in_properties_request(json=json)
    response = send_request_json_response(request)
    assert response["additionalProperties"]['weight'] ==  599

def test_create_ap_in_properties_with_ap_string(send_request_json_response):
    json = {
        "id": 5,
        "name": 'Funny',
        "@odata.location":'westus',
        'color': 'red',
        'city': 'Seattle',
        'food': 'tikka masala',
        "additionalProperties": {
            'height': 5.61,
            'weight': 599,
            'footsize': 11.5
        }
    }
    request = pets.build_create_ap_in_properties_with_ap_string_request(json=json)
    response = send_request_json_response(request)
    assert response['color'] == 'red'
    assert response['additionalProperties']['weight'] == 599