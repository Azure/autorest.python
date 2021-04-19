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

from typing import Dict
import pytest
import isodate
from datetime import date, datetime, timedelta, tzinfo
from msrest.exceptions import DeserializationError, SerializationError, ValidationError
from bodycomplex import AutoRestComplexTestService
from bodycomplex.models import *
from bodycomplex._rest import (
    basic,
    primitive,
    readonlyproperty,
    array,
    dictionary,
    polymorphism,
    polymorphicrecursive,
    inheritance,
)
from azure.core.exceptions import HttpResponseError

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
    with AutoRestComplexTestService(base_url="http://localhost:3000") as client:
        yield client

@pytest.fixture
def make_request(client, base_make_request):
    def _make_request(request):
        return base_make_request(client, request)
    return _make_request

@pytest.fixture
def make_request_json_response(client, base_make_request_json_response):
    def _make_request(request):
        return base_make_request_json_response(client, request)
    return _make_request

@pytest.fixture
def min_date():
    min_date = datetime.min
    return min_date.replace(tzinfo=UTC())

def test_basic_get_and_put_valid(make_request, make_request_json_response):
    # GET basic/valid
    request = basic.build_get_valid_request()
    basic_result = Basic.deserialize(make_request_json_response(request))
    assert 2 ==  basic_result.id
    assert "abc" ==  basic_result.name
    assert CMYKColors.yellow.value ==  basic_result.color

    # PUT basic/valid
    basic_result = Basic(id=2, name='abc', color="Magenta")
    request = basic.build_put_valid_request(json=basic_result.serialize())
    make_request(request)
    basic_result = Basic(id=2, name='abc', color=CMYKColors.magenta)
    request = basic.build_put_valid_request(json=basic_result.serialize())
    make_request(request)

def test_basic_get_empty(make_request, make_request_json_response):
    # GET basic/empty
    request = basic.build_get_empty_request()
    basic_result = Basic.deserialize(make_request_json_response(request))
    assert basic_result.id is None
    assert basic_result.name is None

def test_basic_get_null(make_request, make_request_json_response):
    # GET basic/null
    request = basic.build_get_null_request()
    basic_result = Basic.deserialize(make_request_json_response(request))
    assert basic_result.id is None
    assert basic_result.name is None

def test_basic_get_not_provided(make_request):
    # GET basic/notprovided
    request = basic.build_get_not_provided_request()
    assert make_request(request).text == ''

def test_basic_get_invalid(make_request, make_request_json_response):
    # GET basic/invalid
    request = basic.build_get_invalid_request()
    with pytest.raises(DeserializationError):
        Basic.deserialize(make_request_json_response(request))

# COMPLEX TYPE WITH PRIMITIVE PROPERTIES
def test_primitive_get_and_put_int(make_request, make_request_json_response):
    # GET primitive/integer
    request = primitive.build_get_int_request()
    int_result = IntWrapper.deserialize(make_request_json_response(request))
    assert -1 ==  int_result.field1
    assert 2 ==  int_result.field2

    # PUT primitive/integer
    int_request = {'field1':-1, 'field2':2}
    request = primitive.build_put_int_request(json=int_request)
    make_request(request)

def test_primitive_get_and_put_long(make_request, make_request_json_response):
    # GET primitive/long
    request = primitive.build_get_long_request()
    long_result = LongWrapper.deserialize(make_request_json_response(request))
    assert 1099511627775 ==  long_result.field1
    assert -999511627788 ==  long_result.field2

    # PUT primitive/long
    long_request = {'field1':1099511627775, 'field2':-999511627788}
    request = primitive.build_put_long_request(json=long_request)
    make_request(request)

def test_primitive_get_and_put_float(make_request, make_request_json_response):
    # GET primitive/float
    request = primitive.build_get_float_request()
    float_result = FloatWrapper.deserialize(make_request_json_response(request))
    assert 1.05 ==  float_result.field1
    assert -0.003 ==  float_result.field2

    # PUT primitive/float
    float_request = FloatWrapper(field1=1.05, field2=-0.003)
    request = primitive.build_put_float_request(json=float_request.serialize())
    make_request(request)

def test_primitive_get_and_put_double(make_request, make_request_json_response):
    # GET primitive/double
    request = primitive.build_get_double_request()
    double_result = DoubleWrapper.deserialize(make_request_json_response(request))
    assert 3e-100 ==  double_result.field1
    assert -5e-57 ==  double_result.field56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose

    # PUT primitive/double
    double_request = DoubleWrapper(
        field1=3e-100,
        field56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose=-5e-57
    )
    request = primitive.build_put_double_request(json=double_request.serialize())
    make_request(request)

def test_primitive_get_and_put_bool(make_request, make_request_json_response):
    # GET primitive/bool
    request = primitive.build_get_bool_request()
    bool_result = BooleanWrapper.deserialize(make_request_json_response(request))
    assert bool_result.field_true
    assert not bool_result.field_false

    # PUT primitive/bool
    bool_request = BooleanWrapper(field_true=True, field_false=False)
    request = primitive.build_put_bool_request(json=bool_request.serialize())
    make_request(request)

def test_primitive_get_and_put_string(make_request, make_request_json_response):
    # GET primitive/string
    request = primitive.build_get_string_request()
    string_result = StringWrapper.deserialize(make_request_json_response(request))
    assert "goodrequest" ==  string_result.field
    assert "" ==  string_result.empty
    assert string_result.null is None

    # PUT primitive/string
    string_request = StringWrapper(null=None, empty="", field="goodrequest")
    request = primitive.build_put_string_request(json=string_request.serialize())
    make_request(request)

def test_primitive_get_and_put_date(make_request, make_request_json_response):
    # GET primitive/date
    request = primitive.build_get_date_request()
    date_result = DateWrapper.deserialize(make_request_json_response(request))
    assert isodate.parse_date("0001-01-01") ==  date_result.field
    assert isodate.parse_date("2016-02-29") ==  date_result.leap

    date_request = DateWrapper(
        field=isodate.parse_date('0001-01-01'),
        leap=isodate.parse_date('2016-02-29'))
    request = primitive.build_put_date_request(json=date_request.serialize())
    make_request(request)

def test_primitive_get_and_put_date_time(make_request, make_request_json_response, min_date):
    # GET primitive/datetime
    request = primitive.build_get_date_time_request()
    datetime_result = DatetimeWrapper.deserialize(make_request_json_response(request))

    assert min_date ==  datetime_result.field

    datetime_request = DatetimeWrapper(
        field=isodate.parse_datetime("0001-01-01T00:00:00Z"),
        now=isodate.parse_datetime("2015-05-18T18:38:00Z"))
    request = primitive.build_put_date_time_request(json=datetime_request.serialize())
    make_request(request)

def test_primitive_get_and_put_date_time_rfc1123(make_request, make_request_json_response):
    # GET primitive/datetimerfc1123
    request = primitive.build_get_date_time_rfc1123_request()
    datetimerfc1123_result = Datetimerfc1123Wrapper.deserialize(make_request_json_response(request))

    # we are not using the min date of year 1 because of the latest msrest update
    # with msrest update, minimal year we can parse is 100, instead of 1
    min_date = datetime(2001, 1, 1)
    assert min_date.replace(tzinfo=UTC()) ==  datetimerfc1123_result.field

    # we can still model year 1 though with the latest msrest update
    datetime_request = Datetimerfc1123Wrapper(
        field=isodate.parse_datetime("0001-01-01T00:00:00Z"),
        now=isodate.parse_datetime("2015-05-18T11:38:00Z"))
    request = primitive.build_put_date_time_rfc1123_request(json=datetime_request.serialize())
    make_request(request)

def test_primitive_get_and_put_duration(make_request, make_request_json_response):
    # GET primitive/duration
    expected = timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11)
    request = primitive.build_get_duration_request()
    duration_result = DurationWrapper.deserialize(make_request_json_response(request))
    assert expected ==  duration_result.field

    request = primitive.build_put_duration_request(json=DurationWrapper(field=expected).serialize())

def test_primitive_get_and_put_byte(make_request, make_request_json_response):
    # GET primitive/byte
    request = primitive.build_get_byte_request()
    byte_result = ByteWrapper.deserialize(make_request_json_response(request))
    valid_bytes = bytearray([0x0FF, 0x0FE, 0x0FD, 0x0FC, 0x000, 0x0FA, 0x0F9, 0x0F8, 0x0F7, 0x0F6])
    assert valid_bytes ==  byte_result.field

    # PUT primitive/byte
    request = primitive.build_put_byte_request(json=ByteWrapper(field=valid_bytes).serialize())
    make_request(request)

# COMPLEX TYPE WITH READ ONLY PROPERTIES

def test_readonlyproperty_get_and_put_valid(make_request, make_request_json_response):
    # GET readonly/valid
    valid_obj = ReadonlyObj(size=2)
    valid_obj.id = '1234'
    request = readonlyproperty.build_get_valid_request()
    readonly_result = ReadonlyObj.deserialize(make_request_json_response(request))
    assert readonly_result ==  valid_obj

    # PUT readonly/valid
    request = readonlyproperty.build_put_valid_request(json=2)
    assert make_request(request).text == ''

# COMPLEX TYPE WITH ARRAY PROPERTIES

def test_array_get_and_put_valid(make_request, make_request_json_response):
    # GET array/valid
    request = array.build_get_valid_request()
    array_result = ArrayWrapper.deserialize(make_request_json_response(request))
    assert 5 ==  len(array_result.array)

    array_value = ["1, 2, 3, 4", "", None, "&S#$(*Y",
                    "The quick brown fox jumps over the lazy dog"]
    assert array_result.array ==  array_value

    # PUT array/valid
    request = array.build_put_valid_request(json=ArrayWrapper(array=array_value).serialize())
    make_request(request)

def test_array_get_and_put_empty(make_request, make_request_json_response):

    # GET array/empty
    request = array.build_get_empty_request()
    array_result = ArrayWrapper.deserialize(make_request_json_response(request))
    assert 0 ==  len(array_result.array)

    # PUT array/empty
    request = array.build_put_empty_request(json=ArrayWrapper(array=[]).serialize())
    make_request(request)

def test_array_get_not_provided(make_request_json_response):
    # Get array/notprovided
    request = array.build_get_not_provided_request()
    assert make_request_json_response(request) == {}

# COMPLEX TYPE WITH DICTIONARY PROPERTIES

def test_dictionary_get_and_put_valid(make_request, make_request_json_response):
    # GET dictionary/valid
    request = dictionary.build_get_valid_request()
    dict_result = DictionaryWrapper.deserialize(make_request_json_response(request))
    assert 5 ==  len(dict_result.default_program)

    dict_val = {'txt':'notepad', 'bmp':'mspaint', 'xls':'excel', 'exe':'', '':None}
    assert dict_val ==  dict_result.default_program

    # PUT dictionary/valid
    request = dictionary.build_put_valid_request(json=DictionaryWrapper(default_program=dict_val).serialize())
    make_request(request)

def test_dictionary_get_and_put_empty(make_request, make_request_json_response):
    # GET dictionary/empty
    request = dictionary.build_get_empty_request()
    dict_result = DictionaryWrapper.deserialize(make_request_json_response(request))
    assert 0 ==  len(dict_result.default_program)

    # PUT dictionary/empty
    request = dictionary.build_put_empty_request(json=DictionaryWrapper(default_program={}).serialize())
    make_request(request)

def test_dictionary_get_and_null(make_request_json_response):
    # GET dictionary/null
    request = dictionary.build_get_null_request()
    dictionary_result = DictionaryWrapper.deserialize(make_request_json_response(request))
    assert dictionary_result.default_program is None

def test_dictionary_get_not_provided(make_request_json_response):
    # GET dictionary/notprovided
    request = dictionary.build_get_not_provided_request()
    assert make_request_json_response(request) == {}


# COMPLEX TYPES THAT INVOLVE INHERITANCE

def test_inheritance_get_and_put_valid(make_request, make_request_json_response):
    # GET inheritance/valid
    request = inheritance.build_get_valid_request()
    inheritance_result = Siamese.deserialize(make_request_json_response(request))
    assert 2 ==  inheritance_result.id
    assert "Siameeee" ==  inheritance_result.name
    assert -1 ==  inheritance_result.hates[1].id
    assert "Tomato" ==  inheritance_result.hates[1].name

    # PUT inheritance/valid
    siamese_request = {
        'id': 2,
        'name': "Siameeee",
        'color': "green",
        'breed': "persian",
        'hates': [Dog(id=1, name="Potato", food="tomato").serialize(),
                Dog(id=-1, name="Tomato", food="french fries").serialize()]
        }
    request = inheritance.build_put_valid_request(json=siamese_request)
    make_request(request)

# COMPLEX TYPES THAT INVOLVE POLYMORPHISM

def test_get_composed_with_discriminator(make_request_json_response):
    request = polymorphism.build_get_composed_with_discriminator_request()
    result = DotFishMarket.deserialize(make_request_json_response(request))
    assert isinstance(result.sample_fish, DotSalmon)

def test_get_composed_without_discriminator(make_request_json_response):
    request = polymorphism.build_get_composed_without_discriminator_request()
    result = DotFishMarket.deserialize(make_request_json_response(request))
    assert isinstance(result.sample_fish, DotFish)

def test_polymorphism_get_and_put_valid(make_request, make_request_json_response):
    # GET polymorphism/valid
    request = polymorphism.build_get_valid_request()
    result = Fish.deserialize(make_request_json_response(request))
    assert result is not None
    assert result.location ==  "alaska"
    assert len(result.siblings) ==  3
    assert isinstance(result.siblings[0],  Shark)
    assert isinstance(result.siblings[1],  Sawshark)
    assert isinstance(result.siblings[2],  Goblinshark)
    assert result.siblings[0].age ==  6
    assert result.siblings[1].age ==  105
    assert result.siblings[2].age ==  1


    # PUT polymorphism/valid
    request = Salmon(length=1,
        iswild = True,
        location = "alaska",
        species = "king",
        siblings = [Shark(length=20,
                            birthday=isodate.parse_datetime("2012-01-05T01:00:00Z"),
                            age=6, species="predator"),
                    Sawshark(length=10,
                                birthday=isodate.parse_datetime("1900-01-05T01:00:00Z"),
                                age=105, species="dangerous",
                                picture=bytearray([255, 255, 255, 255, 254])),
                    Goblinshark(length=30,
                                birthday=isodate.parse_datetime("2015-08-08T00:00:00Z"),
                                age=1, species="scary", jawsize=5, color='pinkish-gray')]
        )
    request = polymorphism.build_put_valid_request(json=request.serialize())
    make_request(request)

def test_polymorphism_put_valid_missing_required(make_request, make_request_json_response):
    bad_request = Salmon(length=1,
        iswild=True,
        location="alaska",
        species="king",
        siblings = [
            Shark(length=20,
                    birthday=isodate.parse_datetime("2012-01-05T01:00:00Z"),
                    age=6, species="predator"),
            Sawshark(length=10, birthday=None, age=105, species="dangerous",
                        picture=bytearray([255, 255, 255, 255, 254]))]
        )

    request = polymorphism.build_put_valid_missing_required_request(json=bad_request.serialize())

    # in convenience layer, this raises a ValidationError (when generated with client side validation)
    with pytest.raises(HttpResponseError) as e:
        make_request(request)
    assert "Reached server in scenario: /complex/polymorphism/missingrequired/invalid" in str(e.value)

# COMPLEX TYPES THAT INVOLVE RECURSIVE REFERENCE

def test_polymorphismrecursive_get_and_put_valid(make_request, make_request_json_response):
    # GET polymorphicrecursive/valid
    request = polymorphicrecursive.build_get_valid_request()
    result = Fish.deserialize(make_request_json_response(request))
    assert isinstance(result,  Salmon)
    assert isinstance(result.siblings[0],  Shark)
    assert isinstance(result.siblings[0].siblings[0],  Salmon)
    assert result.siblings[0].siblings[0].location ==  "atlantic"

    request = Salmon(
        iswild=True,
        length=1,
        species="king",
        location="alaska",
        siblings=[
            Shark(
                age=6,
                length=20,
                species="predator",
                siblings=[
                    Salmon(
                        iswild=True,
                        length=2,
                        location="atlantic",
                        species="coho",
                        siblings=[
                            Shark(
                                age=6,
                                length=20,
                                species="predator",
                                birthday=isodate.parse_datetime("2012-01-05T01:00:00Z")),
                            Sawshark(
                                age=105,
                                length=10,
                                species="dangerous",
                                birthday=isodate.parse_datetime("1900-01-05T01:00:00Z"),
                                picture=bytearray([255, 255, 255, 255, 254]))]),
                    Sawshark(
                        age=105,
                        length=10,
                        species="dangerous",
                        siblings=[],
                        birthday=isodate.parse_datetime("1900-01-05T01:00:00Z"),
                        picture=bytearray([255, 255, 255, 255, 254]))],
                birthday=isodate.parse_datetime("2012-01-05T01:00:00Z")),
            Sawshark(
                age=105,
                length=10,
                species="dangerous",
                siblings=[],
                birthday=isodate.parse_datetime("1900-01-05T01:00:00Z"),
                picture=bytearray([255, 255, 255, 255, 254]))])

    # PUT polymorphicrecursive/valid
    request = polymorphicrecursive.build_put_valid_request(json=request.serialize())
    make_request(request)


# Complex types that uses additional properties and polymorphism
def test_polymorphism_get_and_put_complicated(make_request, make_request_json_response):
    request = polymorphism.build_get_complicated_request()
    response = make_request_json_response(request)
    request = polymorphism.build_put_complicated_request(json=response)
    make_request(request)

# Complex types that uses missing discriminator

def test_polymorphism_get_and_put_missing_discriminator(make_request, make_request_json_response):
    regular_salmon = Salmon(
        iswild=True,
        location='alaska',
        species='king',
        length=1.0,
        siblings=[Shark(
            age=6,
            birthday=isodate.parse_datetime("2012-01-05T01:00:00Z"),
            length=20,
            species='predator'
        ), Sawshark(
            age=105,
            length=10,
            species="dangerous",
            birthday=isodate.parse_datetime("1900-01-05T01:00:00Z"),
            picture=bytearray([255, 255, 255, 255, 254])
        ), Goblinshark(
            length=30,
            birthday=isodate.parse_datetime("2015-08-08T00:00:00Z"),
            age=1,
            species="scary",
            jawsize=5,
            color='pinkish-gray'
        )]
    )
    # Not raise is enough of a test
    request = polymorphism.build_put_missing_discriminator_request(json=regular_salmon.serialize())
    make_request(request)

    # Dot syntax
    request = polymorphism.build_get_dot_syntax_request()
    dot_salmon = DotFish.deserialize(make_request_json_response(request))
    assert dot_salmon.fish_type == "DotSalmon"
    assert dot_salmon.location == "sweden"
