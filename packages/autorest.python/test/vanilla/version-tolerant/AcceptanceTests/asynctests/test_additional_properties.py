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

from additionalpropertiesversiontolerant.aio import AdditionalPropertiesClient

import pytest

@pytest.fixture
@async_generator
async def client():
    async with AdditionalPropertiesClient() as client:
        await yield_(client)

@pytest.mark.asyncio
async def test_create_ap_true(client):
    input_ap_true = {
        'birthdate': '2017-12-13T02:29:51Z',
        'complexProperty': {
            'color': 'Red'
        },
        "id": 1,
        "name": "Puppy",
    }
    output_ap_true = await client.pets.create_ap_true(input_ap_true)
    assert output_ap_true['birthdate'] ==  '2017-12-13T02:29:51Z'

@pytest.mark.asyncio
async def test_create_cat_ap_true(client):
    input_ap_true = {
        'birthdate': '2017-12-13T02:29:51Z',
        'complexProperty': {'color': 'Red'},
        'id': 1,
        'name': 'Lisa',
        'friendly': True
    }
    output_ap_true = await client.pets.create_cat_ap_true(input_ap_true)
    assert output_ap_true['birthdate'] ==  '2017-12-13T02:29:51Z'

@pytest.mark.asyncio
async def test_create_ap_object(client):
    input_ap_obj = {
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
    output_ap_obj = await client.pets.create_ap_object(input_ap_obj)
    assert output_ap_obj['siblings'][0]['birthdate'] ==  '2017-12-13T02:29:51Z'

@pytest.mark.asyncio
async def test_create_ap_string(client):
    input_ap_str = {
        "id": 3,
        "name": 'Tommy',
        'color': 'red',
        'weight': '10 kg',
        'city': 'Bombay'
    }
    output_ap_str = await client.pets.create_ap_string(input_ap_str)
    assert output_ap_str['color'] ==  'red'

@pytest.mark.asyncio
async def test_create_ap_in_properties(client):
    input_ap_int = {
        "id": 4,
        "name": 'Bunny',
        "additionalProperties": {
            'height': 5.61,
            'weight': 599,
            'footsize': 11.5
        }
    }
    output_ap_int = await client.pets.create_ap_in_properties(input_ap_int)
    assert output_ap_int['additionalProperties']['weight'] ==  599

@pytest.mark.asyncio
async def test_create_ap_in_properties_with_ap_string(client):
    input_ap_str_add = {
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
    output_ap_str_add = await client.pets.create_ap_in_properties_with_ap_string(input_ap_str_add)
    assert output_ap_str_add['color'] ==  'red'
    assert output_ap_str_add['additionalProperties']['weight'] ==  599
