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
import pytest
import isodate
from datetime import datetime, timedelta, tzinfo
from bodycomplexlowlevel.aio import AutoRestComplexTestService
from bodycomplexlowlevel.rest import (
    basic,
    array,
    dictionary,
    polymorphicrecursive,
    polymorphism,
    primitive,
    readonlyproperty,
    inheritance,
)
from azure.core.exceptions import HttpResponseError
from msrest import Serializer, Deserializer
from base64 import b64decode, b64encode


class UTC(tzinfo):
    def utcoffset(self,dt):
        return timedelta(hours=0,minutes=0)

    def tzname(self,dt):
        return "Z"

    def dst(self,dt):
        return timedelta(0)

import pytest

@pytest.fixture
@async_generator
async def client():
    async with AutoRestComplexTestService() as client:
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
def min_date():
    min_date = datetime.min
    return min_date.replace(tzinfo=UTC())

@pytest.mark.asyncio
async def test_basic_get_and_put_valid(send_request, send_request_json_response):
    # GET basic/valid
    request = basic.build_get_valid_request()
    basic_result = await send_request_json_response(request)
    assert 2 ==  basic_result['id']
    assert "abc" ==  basic_result['name']
    assert "YELLOW" ==  basic_result['color']

    # PUT basic/valid
    json = {
        "id": 2,
        "name": "abc",
        "color": "Magenta",
    }
    request = basic.build_put_valid_request(json=json)
    await send_request(request)
    json = {
        "id": 2,
        "name": "abc",
        "color": "Magenta",
    }
    request = basic.build_put_valid_request(json=json)
    await send_request(request)

@pytest.mark.asyncio
async def test_basic_get_empty(send_request, send_request_json_response):
    # GET basic/empty
    request = basic.build_get_empty_request()
    basic_result = await send_request_json_response(request)
    assert basic_result == {}

@pytest.mark.asyncio
async def test_basic_get_null(send_request_json_response):
    # GET basic/null
    request = basic.build_get_null_request()
    basic_result = await send_request_json_response(request)
    assert basic_result['id'] is None
    assert basic_result['name'] is None

@pytest.mark.asyncio
async def test_basic_get_not_provided(send_request):
    # GET basic/notprovided
    request = basic.build_get_not_provided_request()
    assert (await send_request(request)).text() == ''

@pytest.mark.asyncio
async def test_basic_get_invalid(send_request_json_response):
    # GET basic/invalid
    request = basic.build_get_invalid_request()
    basic_result = await send_request_json_response(request)
    # it's deserialized as invalid bc the id is not a number
    # with LLC, we don't care thought
    assert basic_result['id'] == 'a'
    assert basic_result['name'] == 'abc'

# COMPLEX TYPE WITH PRIMITIVE PROPERTIES
@pytest.mark.asyncio
async def test_primitive_get_and_put_int(send_request, send_request_json_response):
    # GET primitive/integer
    request = primitive.build_get_int_request()
    int_result = await send_request_json_response(request)
    assert -1 ==  int_result['field1']
    assert 2 ==  int_result['field2']

    # PUT primitive/integer
    int_request = {'field1':-1, 'field2':2}
    request = primitive.build_put_int_request(json=int_request)
    await send_request(request)

@pytest.mark.asyncio
async def test_primitive_get_and_put_long(send_request, send_request_json_response):
    # GET primitive/long
    request = primitive.build_get_long_request()
    long_result = await send_request_json_response(request)
    assert 1099511627775 ==  long_result['field1']
    assert -999511627788 ==  long_result['field2']

    # PUT primitive/long
    json = {'field1':1099511627775, 'field2':-999511627788}
    request = primitive.build_put_long_request(json=json)
    await send_request(request)

@pytest.mark.asyncio
async def test_primitive_get_and_put_float(send_request, send_request_json_response):
    # GET primitive/float
    request = primitive.build_get_float_request()
    float_result = await send_request_json_response(request)
    assert 1.05 ==  float_result['field1']
    assert -0.003 ==  float_result['field2']

    # PUT primitive/float
    json = {
        "field1": 1.05,
        "field2": -0.003
    }
    request = primitive.build_put_float_request(json=json)
    await send_request(request)

@pytest.mark.asyncio
async def test_primitive_get_and_put_double(send_request, send_request_json_response):
    # GET primitive/double
    request = primitive.build_get_double_request()
    double_result = await send_request_json_response(request)
    assert 3e-100 ==  double_result['field1']
    assert -5e-57 ==  double_result['field_56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose']

    # PUT primitive/double
    json = {
        "field1": 3e-100,
        "field_56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose": -5e-57
    }
    request = primitive.build_put_double_request(json=json)
    await send_request(request)

@pytest.mark.asyncio
async def test_primitive_get_and_put_bool(send_request, send_request_json_response):
    # GET primitive/bool
    request = primitive.build_get_bool_request()
    bool_result = await send_request_json_response(request)
    assert bool_result['field_true']
    assert not bool_result['field_false']

    # PUT primitive/bool
    json = {
        "field_true": True,
        "field_false": False
    }
    request = primitive.build_put_bool_request(json=json)
    await send_request(request)

@pytest.mark.asyncio
async def test_primitive_get_and_put_string(send_request, send_request_json_response):
    # GET primitive/string
    request = primitive.build_get_string_request()
    string_result = await send_request_json_response(request)
    assert "goodrequest" ==  string_result['field']
    assert "" ==  string_result['empty']
    assert string_result['null'] is None

    # PUT primitive/string
    json = {
        "null": None,
        "empty": "",
        "field": "goodrequest"
    }
    request = primitive.build_put_string_request(json=json)
    await send_request(request)

@pytest.mark.asyncio
async def test_primitive_get_and_put_date(send_request, send_request_json_response):
    # GET primitive/date
    request = primitive.build_get_date_request()
    date_result = await send_request_json_response(request)
    assert isodate.parse_date("0001-01-01") == isodate.parse_date(date_result['field'])
    assert isodate.parse_date("2016-02-29") == isodate.parse_date(date_result['leap'])

    json = {
        "field": '0001-01-01',
        "leap": '2016-02-29'
    }
    request = primitive.build_put_date_request(json=json)
    await send_request(request)

@pytest.mark.asyncio
async def test_primitive_get_and_put_date_time(send_request, send_request_json_response, min_date):
    # GET primitive/datetime
    request = primitive.build_get_date_time_request()
    datetime_result = await send_request_json_response(request)

    assert min_date ==  Deserializer.deserialize_iso(datetime_result['field'])

    json = {
        "field": "0001-01-01T00:00:00Z",
        "now": "2015-05-18T18:38:00Z"
    }
    request = primitive.build_put_date_time_request(json=json)
    await send_request(request)

@pytest.mark.asyncio
async def test_primitive_get_and_put_date_time_rfc1123(send_request, send_request_json_response):
    # GET primitive/datetimerfc1123
    request = primitive.build_get_date_time_rfc1123_request()
    datetimerfc1123_result = await send_request_json_response(request)

    # we are not using the min date of year 1 because of the latest msrest update
    # with msrest update, minimal year we can parse is 100, instead of 1
    min_date = datetime(2001, 1, 1)
    assert min_date.replace(tzinfo=UTC()) == Deserializer.deserialize_rfc(datetimerfc1123_result['field'])

    # we can still model year 1 though with the latest msrest update
    json = {
        "field": Serializer.serialize_rfc(isodate.parse_datetime("0001-01-01T00:00:00Z")),
        "now": Serializer.serialize_rfc(isodate.parse_datetime("2015-05-18T11:38:00Z"))
    }
    request = primitive.build_put_date_time_rfc1123_request(json=json)
    await send_request(request)

@pytest.mark.asyncio
async def test_primitive_get_and_put_duration(send_request, send_request_json_response):
    # GET primitive/duration
    expected = timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11)
    request = primitive.build_get_duration_request()
    duration_result = await send_request_json_response(request)
    assert expected == Deserializer.deserialize_duration(duration_result['field'])

    request = primitive.build_put_duration_request(json={"field": Serializer.serialize_duration(expected)})
    await send_request(request)

@pytest.mark.asyncio
async def test_primitive_get_and_put_byte(send_request, send_request_json_response):
    # GET primitive/byte
    request = primitive.build_get_byte_request()
    byte_result = await send_request_json_response(request)
    valid_bytes = bytearray([0x0FF, 0x0FE, 0x0FD, 0x0FC, 0x000, 0x0FA, 0x0F9, 0x0F8, 0x0F7, 0x0F6])
    assert valid_bytes == bytearray(b64decode(byte_result['field']))

    # PUT primitive/byte
    request = primitive.build_put_byte_request(json={"field": b64encode(valid_bytes).decode()})
    await send_request(request)

# COMPLEX TYPE WITH READ ONLY PROPERTIES

@pytest.mark.asyncio
async def test_readonlyproperty_get_and_put_valid(send_request, send_request_json_response):
    # GET readonly/valid
    valid_obj = {"size": 2, 'id': '1234'}
    request = readonlyproperty.build_get_valid_request()
    readonly_result = await send_request_json_response(request)
    assert readonly_result ==  valid_obj

    # PUT readonly/valid
    request = readonlyproperty.build_put_valid_request(json=2)
    assert (await send_request(request)).text() == ''

# COMPLEX TYPE WITH ARRAY PROPERTIES

@pytest.mark.asyncio
async def test_array_get_and_put_valid(send_request, send_request_json_response):
    # GET array/valid
    request = array.build_get_valid_request()
    array_result = await send_request_json_response(request)
    assert 5 ==  len(array_result['array'])

    array_value = ["1, 2, 3, 4", "", None, "&S#$(*Y",
                    "The quick brown fox jumps over the lazy dog"]
    assert array_result['array'] ==  array_value

    # PUT array/valid
    request = array.build_put_valid_request(json={"array": array_value})
    await send_request(request)

@pytest.mark.asyncio
async def test_array_get_and_put_empty(send_request, send_request_json_response):

    # GET array/empty
    request = array.build_get_empty_request()
    array_result = await send_request_json_response(request)
    assert 0 ==  len(array_result['array'])

    # PUT array/empty
    request = array.build_put_empty_request(json={"array": []})
    await send_request(request)

@pytest.mark.asyncio
async def test_array_get_not_provided(send_request_json_response):
    # Get array/notprovided
    request = array.build_get_not_provided_request()
    assert await send_request_json_response(request) == {}

# COMPLEX TYPE WITH DICTIONARY PROPERTIES

@pytest.mark.asyncio
async def test_dictionary_get_and_put_valid(send_request, send_request_json_response):
    # GET dictionary/valid
    request = dictionary.build_get_valid_request()
    dict_result = await send_request_json_response(request)
    assert 5 ==  len(dict_result['defaultProgram'])

    dict_val = {'txt':'notepad', 'bmp':'mspaint', 'xls':'excel', 'exe':'', '':None}
    assert dict_val ==  dict_result['defaultProgram']

    # PUT dictionary/valid
    request = dictionary.build_put_valid_request(json={"defaultProgram": dict_val})
    await send_request(request)

@pytest.mark.asyncio
async def test_dictionary_get_and_put_empty(send_request, send_request_json_response):
    # GET dictionary/empty
    request = dictionary.build_get_empty_request()
    dict_result = await send_request_json_response(request)
    assert 0 ==  len(dict_result['defaultProgram'])

    # PUT dictionary/empty
    request = dictionary.build_put_empty_request(json={"defaultProgram": {}})
    await send_request(request)

@pytest.mark.asyncio
async def test_dictionary_get_and_null(send_request_json_response):
    # GET dictionary/null
    request = dictionary.build_get_null_request()
    dictionary_result = await send_request_json_response(request)
    assert dictionary_result['defaultProgram'] is None

@pytest.mark.asyncio
async def test_dictionary_get_not_provided(send_request_json_response):
    # GET dictionary/notprovided
    request = dictionary.build_get_not_provided_request()
    assert await send_request_json_response(request) == {}


# COMPLEX TYPES THAT INVOLVE INHERITANCE

@pytest.mark.asyncio
async def test_inheritance_get_and_put_valid(send_request, send_request_json_response):
    # GET inheritance/valid
    request = inheritance.build_get_valid_request()
    inheritance_result = await send_request_json_response(request)
    assert 2 ==  inheritance_result['id']
    assert "Siameeee" ==  inheritance_result['name']
    assert -1 ==  inheritance_result['hates'][1]['id']
    assert "Tomato" ==  inheritance_result['hates'][1]['name']

    # PUT inheritance/valid
    json = {
        'id': 2,
        'name': "Siameeee",
        'color': "green",
        'breed': "persian",
        'hates': [{"id": 1, "name": "Potato", "food": "tomato"},
                  {"id": -1, "name": "Tomato", "food": "french fries"}]
        }
    request = inheritance.build_put_valid_request(json=json)
    await send_request(request)

# COMPLEX TYPES THAT INVOLVE POLYMORPHISM

@pytest.mark.asyncio
async def test_get_composed_with_discriminator(send_request_json_response):
    request = polymorphism.build_get_composed_with_discriminator_request()
    result = await send_request_json_response(request)
    assert result['sampleSalmon']['fish.type'] == "DotSalmon"

@pytest.mark.asyncio
async def test_get_composed_without_discriminator(send_request_json_response):
    request = polymorphism.build_get_composed_without_discriminator_request()
    result = await send_request_json_response(request)
    with pytest.raises(KeyError):
        result['sampleSalmon']['fish.type']  # shouldn't have a discriminator

@pytest.mark.asyncio
async def test_polymorphism_get_and_put_valid(send_request, send_request_json_response):
    # GET polymorphism/valid
    request = polymorphism.build_get_valid_request()
    result = await send_request_json_response(request)
    assert result is not None
    assert result['location'] ==  "alaska"
    assert len(result['siblings']) ==  3
    assert result['siblings'][0]['fishtype'] == 'shark'
    assert result['siblings'][1]['fishtype'] == 'sawshark'
    assert result['siblings'][2]['fishtype'] == 'goblin'
    assert result['siblings'][0]['age'] ==  6
    assert result['siblings'][1]['age'] ==  105
    assert result['siblings'][2]['age'] ==  1


    # PUT polymorphism/valid
    json = {
        "fishtype": "salmon",
        "species": "king",
        "length": 1.0,
        "siblings": [
            {
                "fishtype": "shark",
                "species": "predator",
                "length": 20.0,
                "age": 6,
                "birthday": "2012-01-05T01:00:00.000Z"
            },
            {
                "fishtype": "sawshark",
                "species": "dangerous",
                "length": 10.0,
                "age": 105,
                "birthday": "1900-01-05T01:00:00.000Z",
                "picture": "//////4="
            },
            {
                "fishtype": "goblin",
                "species": "scary",
                "length": 30.0,
                "age": 1,
                "birthday": "2015-08-08T00:00:00.000Z",
                "jawsize": 5,
                "color": "pinkish-gray"
            }
        ],
        "location": "alaska",
        "iswild": True
    }
    request = polymorphism.build_put_valid_request(json=json)
    await send_request(request)

@pytest.mark.asyncio
async def test_polymorphism_put_valid_missing_required(send_request):
    json = {
        "fishtype": "salmon",
        "species": "king",
        "length": 1.0,
        "siblings": [
            {
                "fishtype": "shark",
                "species": "predator",
                "length": 20.0,
                "age": 6,
                "birthday": "2012-01-05T01:00:00.000Z"
            },
            {
                "fishtype": "sawshark",
                "species": "dangerous",
                "length": 10.0,
                "age": 105,
                "picture": "//////4="
            }
        ],
        "location": "alaska",
        "iswild": True
    }

    request = polymorphism.build_put_valid_missing_required_request(json=json)

    # in convenience layer, this raises a ValidationError (when generated with client side validation)
    with pytest.raises(HttpResponseError) as e:
        await send_request(request)
    assert "Reached server in scenario: /complex/polymorphism/missingrequired/invalid" in str(e.value.response.text())

# COMPLEX TYPES THAT INVOLVE RECURSIVE REFERENCE

@pytest.mark.asyncio
async def test_polymorphismrecursive_get_and_put_valid(send_request, send_request_json_response):
    # GET polymorphicrecursive/valid
    request = polymorphicrecursive.build_get_valid_request()
    result = await send_request_json_response(request)
    assert result['fishtype'] == 'salmon'
    assert result['siblings'][0]['fishtype'] == 'shark'
    assert result['siblings'][0]['siblings'][0]['fishtype'] == 'salmon'
    assert result['siblings'][0]['siblings'][0]['location'] ==  "atlantic"

    json = {
        "fishtype": "salmon",
        "species": "king",
        "length": 1.0,
        "siblings": [
            {
                "fishtype": "shark",
                "species": "predator",
                "length": 20.0,
                "siblings": [
                    {
                        "fishtype": "salmon",
                        "species": "coho",
                        "length": 2.0,
                        "siblings": [
                            {
                                "fishtype": "shark",
                                "species": "predator",
                                "length": 20.0,
                                "age": 6,
                                "birthday": "2012-01-05T01:00:00.000Z"
                            },
                            {
                                "fishtype": "sawshark",
                                "species": "dangerous",
                                "length": 10.0,
                                "age": 105,
                                "birthday": "1900-01-05T01:00:00.000Z",
                                "picture": "//////4="
                            }
                        ],
                        "location": "atlantic",
                        "iswild": True
                    },
                    {
                        "fishtype": "sawshark",
                        "species": "dangerous",
                        "length": 10.0,
                        "siblings": [],
                        "age": 105,
                        "birthday": "1900-01-05T01:00:00.000Z",
                        "picture": "//////4="
                    }
                ],
                "age": 6,
                "birthday": "2012-01-05T01:00:00.000Z"
            },
            {
                "fishtype": "sawshark",
                "species": "dangerous",
                "length": 10.0,
                "siblings": [],
                "age": 105,
                "birthday": "1900-01-05T01:00:00.000Z",
                "picture": "//////4="
            }
        ],
        "location": "alaska",
        "iswild": True
    }

    # PUT polymorphicrecursive/valid
    request = polymorphicrecursive.build_put_valid_request(json=json)
    await send_request(request)


# Complex types that uses additional properties and polymorphism
@pytest.mark.asyncio
async def test_polymorphism_get_and_put_complicated(send_request, send_request_json_response):
    request = polymorphism.build_get_complicated_request()
    response = await send_request_json_response(request)
    request = polymorphism.build_put_complicated_request(json=response)
    await send_request(request)

# Complex types that uses missing discriminator

@pytest.mark.asyncio
async def test_polymorphism_get_and_put_missing_discriminator(send_request, send_request_json_response):
    json = {
        "fishtype": "salmon",
        "species": "king",
        "length": 1.0,
        "siblings": [
            {
                "fishtype": "shark",
                "species": "predator",
                "length": 20.0,
                "age": 6,
                "birthday": "2012-01-05T01:00:00.000Z"
            },
            {
                "fishtype": "sawshark",
                "species": "dangerous",
                "length": 10.0,
                "age": 105,
                "birthday": "1900-01-05T01:00:00.000Z",
                "picture": "//////4="
            },
            {
                "fishtype": "goblin",
                "species": "scary",
                "length": 30.0,
                "age": 1,
                "birthday": "2015-08-08T00:00:00.000Z",
                "jawsize": 5,
                "color": "pinkish-gray"
            }
        ],
        "location": "alaska",
        "iswild": True
    }
    # Not raise is enough of a test
    request = polymorphism.build_put_missing_discriminator_request(json=json)
    await send_request(request)

    # Dot syntax
    request = polymorphism.build_get_dot_syntax_request()
    dot_salmon = await send_request_json_response(request)
    assert dot_salmon['fish.type'] == "DotSalmon"
    assert dot_salmon['location'] == "sweden"

@pytest.mark.asyncio
async def test_pass_in_api_version(client):
    assert client._config.api_version == "2016-02-29"
    async with AutoRestComplexTestService(api_version="2021-10-01") as client:
        assert client._config.api_version == "2021-10-01"
