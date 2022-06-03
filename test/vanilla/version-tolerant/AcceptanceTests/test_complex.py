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
import isodate
from datetime import datetime, timedelta, tzinfo
from msrest import Serializer, Deserializer
from base64 import b64decode, b64encode
from azure.core.exceptions import HttpResponseError

from bodycomplexversiontolerant import AutoRestComplexTestService
from azure.core.pipeline.policies import CustomHookPolicy

class UTC(tzinfo):
    def utcoffset(self,dt):
        return timedelta(hours=0,minutes=0)

    def tzname(self,dt):
        return "Z"

    def dst(self,dt):
        return timedelta(0)

import pytest

@pytest.fixture
def client():
    with AutoRestComplexTestService() as client:
        yield client

@pytest.fixture
def min_date():
    min_date = datetime.min
    return min_date.replace(tzinfo=UTC())

def test_basic_get_and_put_valid(client: AutoRestComplexTestService):
    # GET basic/valid
    basic_result = client.basic.get_valid()
    assert 2 ==  basic_result['id']
    assert "abc" ==  basic_result['name']
    assert "YELLOW" ==  basic_result['color']

    # PUT basic/valid
    basic_result = {
        "id": 2,
        "name": "abc",
        "color": "Magenta",
    }
    client.basic.put_valid(basic_result)

def test_basic_get_empty(client):
    # GET basic/empty
    basic_result = client.basic.get_empty()
    assert basic_result == {}

def test_basic_get_null(client):
    # GET basic/null
    basic_result = client.basic.get_null()
    assert basic_result['id'] is None
    assert basic_result['name'] is None

def test_basic_get_not_provided(client):
    # GET basic/notprovided
    basic_result = client.basic.get_not_provided()
    assert basic_result is None

def test_basic_get_invalid(client):
    # GET basic/invalid
    basic_result = client.basic.get_invalid()
    # it's deserialized as invalid bc the id is not a number
    # with legacy, we don't care though
    assert basic_result['id'] == 'a'
    assert basic_result['name'] == 'abc'

# COMPLEX TYPE WITH PRIMITIVE PROPERTIES
def test_primitive_get_and_put_int(client):
    # GET primitive/integer
    int_result = client.primitive.get_int()
    assert -1 ==  int_result['field1']
    assert 2 ==  int_result['field2']

    # PUT primitive/integer
    int_request = {'field1':-1, 'field2':2}
    client.primitive.put_int(int_request)

def test_primitive_get_and_put_long(client):
    # GET primitive/long
    long_result = client.primitive.get_long()
    assert 1099511627775 ==  long_result['field1']
    assert -999511627788 ==  long_result['field2']

    # PUT primitive/long
    long_request = {'field1':1099511627775, 'field2':-999511627788}
    client.primitive.put_long(long_request)

def test_primitive_get_and_put_float(client):
    # GET primitive/float
    float_result = client.primitive.get_float()
    assert 1.05 ==  float_result['field1']
    assert -0.003 ==  float_result['field2']

    # PUT primitive/float
    float_request = {
        "field1": 1.05,
        "field2": -0.003
    }
    client.primitive.put_float(float_request)

def test_primitive_get_and_put_double(client):
    # GET primitive/double
    double_result = client.primitive.get_double()
    assert 3e-100 ==  double_result['field1']
    assert -5e-57 ==  double_result['field_56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose']

    # PUT primitive/double
    double_request = {
        "field1": 3e-100,
        "field_56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose": -5e-57
    }
    client.primitive.put_double(double_request)

def test_primitive_get_and_put_bool(client):
    # GET primitive/bool
    bool_result = client.primitive.get_bool()
    assert bool_result['field_true']
    assert not bool_result['field_false']

    # PUT primitive/bool
    bool_request = {
        "field_true": True,
        "field_false": False
    }
    client.primitive.put_bool(bool_request)

def test_primitive_get_and_put_string(client):
    # GET primitive/string
    string_result = client.primitive.get_string()
    assert "goodrequest" ==  string_result['field']
    assert "" ==  string_result['empty']
    assert string_result['null'] is None

    # PUT primitive/string
    string_request = {
        "null": None,
        "empty": "",
        "field": "goodrequest"
    }
    client.primitive.put_string(string_request)

def test_primitive_get_and_put_date(client):
    # GET primitive/date
    date_result = client.primitive.get_date()
    assert isodate.parse_date("0001-01-01") == isodate.parse_date(date_result['field'])
    assert isodate.parse_date("2016-02-29") == isodate.parse_date(date_result['leap'])

    date_request = {
        "field": '0001-01-01',
        "leap": '2016-02-29'
    }
    client.primitive.put_date(date_request)

def test_primitive_get_and_put_date_time(client, min_date):
    # GET primitive/datetime
    datetime_result = client.primitive.get_date_time()

    assert min_date ==  Deserializer.deserialize_iso(datetime_result['field'])

    datetime_request = {
        "field": "0001-01-01T00:00:00Z",
        "now": "2015-05-18T18:38:00Z"
    }
    client.primitive.put_date_time(datetime_request)

def test_primitive_get_and_put_date_time_rfc1123(client):
    # GET primitive/datetimerfc1123
    datetimerfc1123_result = client.primitive.get_date_time_rfc1123()

    # we are not using the min date of year 1 because of the latest msrest update
    # with msrest update, minimal year we can parse is 100, instead of 1
    min_date = datetime(2001, 1, 1)
    assert min_date.replace(tzinfo=UTC()) == Deserializer.deserialize_rfc(datetimerfc1123_result['field'])

    # we can still model year 1 though with the latest msrest update
    datetime_request = {
        "field": Serializer.serialize_rfc(isodate.parse_datetime("0001-01-01T00:00:00Z")),
        "now": Serializer.serialize_rfc(isodate.parse_datetime("2015-05-18T11:38:00Z"))
    }
    client.primitive.put_date_time_rfc1123(datetime_request)

def test_primitive_get_and_put_duration(client):
    # GET primitive/duration
    expected = timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11)
    duration_result = client.primitive.get_duration()
    assert expected == Deserializer.deserialize_duration(duration_result['field'])

    client.primitive.put_duration({"field": Serializer.serialize_duration(expected)})

def test_primitive_get_and_put_byte(client):
    # GET primitive/byte
    byte_result = client.primitive.get_byte()
    valid_bytes = bytearray([0x0FF, 0x0FE, 0x0FD, 0x0FC, 0x000, 0x0FA, 0x0F9, 0x0F8, 0x0F7, 0x0F6])
    assert valid_bytes == bytearray(b64decode(byte_result['field']))

    # PUT primitive/byte
    client.primitive.put_byte({"field": b64encode(valid_bytes).decode()})

# COMPLEX TYPE WITH READ ONLY PROPERTIES

def test_readonlyproperty_get_and_put_valid(client):
    # GET readonly/valid
    valid_obj = {"size": 2, 'id': '1234'}
    readonly_result = client.readonlyproperty.get_valid()
    assert readonly_result ==  valid_obj

    # PUT readonly/valid
    readonly_result = client.readonlyproperty.put_valid(2)
    assert readonly_result is None

# COMPLEX TYPE WITH ARRAY PROPERTIES

def test_array_get_and_put_valid(client):
    # GET array/valid
    array_result = client.array.get_valid()
    assert 5 == len(array_result['array'])

    array_value = ["1, 2, 3, 4", "", None, "&S#$(*Y",
                    "The quick brown fox jumps over the lazy dog"]
    assert array_result['array'] ==  array_value

    # PUT array/valid
    client.array.put_valid({"array": array_value})

def test_array_get_and_put_empty(client):

    # GET array/empty
    array_result = client.array.get_empty()
    assert 0 ==  len(array_result['array'])

    # PUT array/empty
    client.array.put_empty({"array": []})

def test_array_get_not_provided(client):
    # Get array/notprovided
    assert client.array.get_not_provided() == {}

# COMPLEX TYPE WITH DICTIONARY PROPERTIES

def test_dictionary_get_and_put_valid(client):
    # GET dictionary/valid
    dict_result = client.dictionary.get_valid()
    assert 5 ==  len(dict_result['defaultProgram'])

    dict_val = {'txt':'notepad', 'bmp':'mspaint', 'xls':'excel', 'exe':'', '':None}
    assert dict_val ==  dict_result['defaultProgram']

    # PUT dictionary/valid
    client.dictionary.put_valid({"defaultProgram": dict_val})

def test_dictionary_get_and_put_empty(client):
    # GET dictionary/empty
    dict_result = client.dictionary.get_empty()
    assert 0 ==  len(dict_result['defaultProgram'])

    # PUT dictionary/empty
    client.dictionary.put_empty({"defaultProgram": {}})

def test_dictionary_get_and_null(client):
    # GET dictionary/null
    assert client.dictionary.get_null()['defaultProgram'] is None

def test_dictionary_get_not_provided(client):
    # GET dictionary/notprovided
    assert client.dictionary.get_not_provided() == {}

# COMPLEX TYPES THAT INVOLVE INHERITANCE

def test_inheritance_get_and_put_valid(client):
    # GET inheritance/valid
    inheritance_result = client.inheritance.get_valid()
    assert 2 ==  inheritance_result['id']
    assert "Siameeee" ==  inheritance_result['name']
    assert -1 ==  inheritance_result['hates'][1]['id']
    assert "Tomato" ==  inheritance_result['hates'][1]['name']

    # PUT inheritance/valid
    request = {
        'id': 2,
        'name': "Siameeee",
        'color': "green",
        'breed': "persian",
        'hates': [{"id": 1, "name": "Potato", "food": "tomato"},
                  {"id": -1, "name": "Tomato", "food": "french fries"}]
        }
    client.inheritance.put_valid(request)

# COMPLEX TYPES THAT INVOLVE POLYMORPHISM

def test_get_composed_with_discriminator(client):
    result = client.polymorphism.get_composed_with_discriminator()
    assert result['sampleSalmon']['fish.type'] == "DotSalmon"

def test_get_composed_without_discriminator(client):
    result = client.polymorphism.get_composed_without_discriminator()
    with pytest.raises(KeyError):
        result['sampleSalmon']['fish.type']  # shouldn't have a discriminator

def test_polymorphism_get_and_put_valid(client):
    # GET polymorphism/valid
    result = client.polymorphism.get_valid()
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
    request = {
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
    client.polymorphism.put_valid(request)

def test_polymorphism_put_valid_missing_required(client):
    bad_request = {
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
    # in legacy, this raises a ValidationError (when generated with client side validation)
    with pytest.raises(HttpResponseError) as e:
        client.polymorphism.put_valid_missing_required(bad_request)
    assert "Reached server in scenario: /complex/polymorphism/missingrequired/invalid" in str(e.value.response.text())

# COMPLEX TYPES THAT INVOLVE RECURSIVE REFERENCE

def test_polymorphismrecursive_get_and_put_valid(client):
    # GET polymorphicrecursive/valid
    result = client.polymorphicrecursive.get_valid()
    assert result['fishtype'] == 'salmon'
    assert result['siblings'][0]['fishtype'] == 'shark'
    assert result['siblings'][0]['siblings'][0]['fishtype'] == 'salmon'
    assert result['siblings'][0]['siblings'][0]['location'] ==  "atlantic"

    request = {
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
    client.polymorphicrecursive.put_valid(request)


# Complex types that uses additional properties and polymorphism
def test_polymorphism_get_and_put_complicated(client):
    smart_salmon = client.polymorphism.get_complicated()
    client.polymorphism.put_complicated(smart_salmon)

# Complex types that uses missing discriminator

def test_polymorphism_get_and_put_missing_discriminator(client):
    regular_salmon = {
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
    client.polymorphism.put_missing_discriminator(regular_salmon)

    # Dot syntax
    dot_salmon = client.polymorphism.get_dot_syntax()
    assert dot_salmon['fish.type'] == "DotSalmon"
    assert dot_salmon['location'] == "sweden"

def test_pass_in_api_version(client):
    assert client._config.api_version == "2016-02-29"
    with AutoRestComplexTestService(api_version="2021-10-01") as client:
        assert client._config.api_version == "2021-10-01"

def test_client_api_version():
    api_version = "2021-10-01"
    def check_api_version(pipeline_request):
        assert pipeline_request.http_request.query["api-version"] == "2021-10-01"
        raise ValueError("Succeeded")
    client = AutoRestComplexTestService(
        api_version=api_version,
        policies=[CustomHookPolicy(raw_request_hook=check_api_version)]
    )

    # PUT basic/valid
    basic_result = {
        "id": 2,
        "name": "abc",
        "color": "Magenta",
    }
    # Even though we override the client api version on the method level
    # DPG doesn't allow that, so should be the api version we passed to the client
    with pytest.raises(ValueError):
        client.basic.put_valid(basic_result, api_version="2016-02-29")
