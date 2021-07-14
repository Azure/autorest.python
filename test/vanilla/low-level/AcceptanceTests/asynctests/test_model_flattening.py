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
from modelflatteninglowlevel.aio import AutoRestResourceFlatteningTestService
from modelflatteninglowlevel import rest

import pytest

@pytest.fixture
@async_generator
async def client():
    async with AutoRestResourceFlatteningTestService(base_url="http://localhost:3000") as client:
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


@pytest.mark.asyncio
async def test_flattening_array(send_request, send_request_json_response):
    #Array
    request = rest.build_get_array_request()
    result = await send_request_json_response(request)
    assert 3 ==  len(result)
    # Resource 1
    assert "1" ==  result[0]['id']
    assert "OK" ==  result[0]['properties']['provisioningStateValues']
    assert "Product1" ==  result[0]['properties']['p.name']
    assert "Flat" ==  result[0]['properties']['type']
    assert "Building 44" ==  result[0]['location']
    assert "Resource1" ==  result[0]['name']
    assert "Succeeded" ==  result[0]['properties']['provisioningState']
    assert "Microsoft.Web/sites" ==  result[0]['type']
    assert "value1" ==  result[0]['tags']["tag1"]
    assert "value3" ==  result[0]['tags']["tag2"]
    # Resource 2
    assert "2" ==  result[1]['id']
    assert "Resource2" ==  result[1]['name']
    assert "Building 44" ==  result[1]['location']
    # Resource 3
    assert "3" ==  result[2]['id']
    assert "Resource3" ==  result[2]['name']

    json = [
        {
            'tags': {
                'tag1': 'value1',
                'tag2': 'value3'
            },
            'location': 'West US'
        },
        {
            'location': 'Building 44'
        }
    ]
    request = rest.build_put_array_request(json=json)
    await send_request(request)

@pytest.mark.asyncio
async def test_flattening_dictionary(send_request, send_request_json_response):

    request = rest.build_get_dictionary_request()
    result = await send_request_json_response(request)
    assert 3 ==  len(result)
    # Resource 1
    assert "1" ==  result["Product1"]['id']
    assert "OK" ==  result["Product1"]['properties']['provisioningStateValues']
    assert "Product1" ==  result["Product1"]['properties']['p.name']
    assert "Flat" ==  result["Product1"]['properties']['type']
    assert "Building 44" ==  result["Product1"]['location']
    assert "Resource1" ==  result["Product1"]['name']
    assert "Succeeded" ==  result["Product1"]['properties']['provisioningState']
    assert "Microsoft.Web/sites" ==  result["Product1"]['type']
    assert "value1" ==  result["Product1"]['tags']["tag1"]
    assert "value3" ==  result["Product1"]['tags']["tag2"]
    # Resource 2
    assert "2" ==  result["Product2"]['id']
    assert "Resource2" ==  result["Product2"]['name']
    assert "Building 44" ==  result["Product2"]['location']
    # Resource 3
    assert "3" ==  result["Product3"]['id']
    assert "Resource3" ==  result["Product3"]['name']

    json = {
        "Resource1": {
            "tags": {
                "tag1": "value1",
                "tag2": "value3"
            },
            "location": "West US",
            "properties": {
                "p.name": "Product1",
                "type": "Flat"
            }
        },
        "Resource2": {
            "location": "Building 44",
            "properties": {
                "p.name": "Product2",
                "type": "Flat"
            }
        }
    }

    request = rest.build_put_dictionary_request(json=json)
    await send_request(request)

@pytest.mark.asyncio
async def test_flattening_complex_object(send_request, send_request_json_response):

    #ResourceCollection
    request = rest.build_get_resource_collection_request()
    result = await send_request_json_response(request)

    #dictionaryofresources
    assert 3 ==  len(result['dictionaryofresources'])
    # Resource 1
    assert "1" ==  result['dictionaryofresources']["Product1"]['id']
    assert "OK" ==  result['dictionaryofresources']["Product1"]['properties']['provisioningStateValues']
    assert "Product1" ==  result['dictionaryofresources']["Product1"]['properties']['p.name']
    assert "Flat" ==  result['dictionaryofresources']["Product1"]['properties']['type']
    assert "Building 44" ==  result['dictionaryofresources']["Product1"]['location']
    assert "Resource1" ==  result['dictionaryofresources']["Product1"]['name']
    assert "Succeeded" ==  result['dictionaryofresources']["Product1"]['properties']['provisioningState']
    assert "Microsoft.Web/sites" ==  result['dictionaryofresources']["Product1"]['type']
    assert "value1" ==  result['dictionaryofresources']["Product1"]['tags']["tag1"]
    assert "value3" ==  result['dictionaryofresources']["Product1"]['tags']["tag2"]
    # Resource 2
    assert "2" ==  result['dictionaryofresources']["Product2"]['id']
    assert "Resource2" ==  result['dictionaryofresources']["Product2"]['name']
    assert "Building 44" ==  result['dictionaryofresources']["Product2"]['location']
    # Resource 3
    assert "3" ==  result['dictionaryofresources']["Product3"]['id']
    assert "Resource3" ==  result['dictionaryofresources']["Product3"]['name']

    #arrayofresources
    assert 3 ==  len(result['arrayofresources'])
    # Resource 1
    assert "4" ==  result['arrayofresources'][0]['id']
    assert "OK" ==  result['arrayofresources'][0]['properties']['provisioningStateValues']
    assert "Product4" ==  result['arrayofresources'][0]['properties']['p.name']
    assert "Flat" ==  result['arrayofresources'][0]['properties']['type']
    assert "Building 44" ==  result['arrayofresources'][0]['location']
    assert "Resource4" ==  result['arrayofresources'][0]['name']
    assert "Succeeded" ==  result['arrayofresources'][0]['properties']['provisioningState']
    assert "Microsoft.Web/sites" ==  result['arrayofresources'][0]['type']
    assert "value1" ==  result['arrayofresources'][0]['tags']["tag1"]
    assert "value3" ==  result['arrayofresources'][0]['tags']["tag2"]
    # Resource 2
    assert "5" ==  result['arrayofresources'][1]['id']
    assert "Resource5" ==  result['arrayofresources'][1]['name']
    assert "Building 44" ==  result['arrayofresources'][1]['location']
    # Resource 3
    assert "6" ==  result['arrayofresources'][2]['id']
    assert "Resource6" ==  result['arrayofresources'][2]['name']

    #productresource
    assert "7" ==  result['productresource']['id']
    assert "Resource7" ==  result['productresource']['name']

    json = {
        "productresource": {
            "location": "India",
            "properties": {
                "p.name": "Azure",
                "type": "Flat"
            }
        },
        "arrayofresources": [
            {
                "tags": {
                    "tag1": "value1",
                    "tag2": "value3"
                },
                "location": "West US",
                "properties": {
                    "p.name": "Product1",
                    "type": "Flat"
                }
            },
            {
                "location": "East US",
                "properties": {
                    "p.name": "Product2",
                    "type": "Flat"
                }
            }
        ],
        "dictionaryofresources": {
            "Resource1": {
                "tags": {
                    "tag1": "value1",
                    "tag2": "value3"
                },
                "location": "West US",
                "properties": {
                    "p.name": "Product1",
                    "type": "Flat"
                }
            },
            "Resource2": {
                "location": "Building 44",
                "properties": {
                    "p.name": "Product2",
                    "type": "Flat"
                }
            }
        }
    }
    request = rest.build_put_resource_collection_request(json=json)
    await send_request(request)

@pytest.mark.asyncio
async def test_model_flattening_simple(send_request_json_response):
    json = {
        "base_product_id": "123",
        "base_product_description": "product description",
        "details": {
            "max_product_display_name": "max name",
            "max_product_capacity": "Large",
            "max_product_image": {
                "generic_value": "https://generic",
                "@odata.value": "http://foo"
            }
        }
    }
    request = rest.build_put_simple_product_request(json=json)
    result = await send_request_json_response(request)
    assert json == result

@pytest.mark.asyncio
async def test_model_flattening_with_parameter_flattening(send_request_json_response):

    json = {
        "base_product_id": "123",
        "base_product_description": "product description",
        "details": {
            "max_product_display_name": "max name",
            "max_product_capacity": "Large",
            "max_product_image": {
                "@odata.value": "http://foo"
            }
        }
    }

    request = rest.build_post_flattened_simple_product_request(json=json)
    result = await send_request_json_response(request)
    assert result == json

@pytest.mark.asyncio
async def test_model_flattening_with_grouping(send_request_json_response):
    json = {
        "base_product_id": "123",
        "base_product_description": "product description",
        "details": {
            "max_product_display_name": "max name",
            "max_product_capacity": "Large",
            "max_product_image": {
                "@odata.value": "http://foo"
            }
        }
    }
    request = rest.build_put_simple_product_with_grouping_request(
        name='groupproduct',
        json=json
    )
    result = await send_request_json_response(request)
    assert result == json
