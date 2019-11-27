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
import json
from datetime import date, datetime, timedelta, tzinfo
import os
from os.path import dirname, pardir, join, realpath

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "BodyComplex"))

from msrest.serialization import Deserializer
from msrest.exceptions import DeserializationError, SerializationError, ValidationError

from bodycomplex.aio import AutoRestComplexTestService
from bodycomplex.models import *

class UTC(tzinfo):
    def utcoffset(self,dt):
        return timedelta(hours=0,minutes=0)

    def tzname(self,dt):
        return "Z"

    def dst(self,dt):
        return timedelta(0)

import pytest


@pytest.fixture()
async def client():
    async with AutoRestComplexTestService(base_url="http://localhost:3000") as client:
        yield client

@pytest.fixture
def min_date():
    min_date = datetime.min
    return min_date.replace(tzinfo=UTC())

class TestComplex(object):

    @pytest.mark.asyncio
    async def test_basic_get_and_put_valid(self, client):
        # GET basic/valid
        basic_result = await client.basic.get_valid()
        assert 2 ==  basic_result.id
        assert "abc" ==  basic_result.name
        assert CMYKColors.yellow.value ==  basic_result.color

        # PUT basic/valid
        basic_result = Basic(id=2, name='abc', color="Magenta")
        await client.basic.put_valid(basic_result)
        basic_result = Basic(id=2, name='abc', color=CMYKColors.magenta)
        await client.basic.put_valid(basic_result)

    @pytest.mark.asyncio
    async def test_basic_get_empty(self, client):
        # GET basic/empty
        basic_result = await client.basic.get_empty()
        assert basic_result.id is None
        assert basic_result.name is None

    @pytest.mark.asyncio
    async def test_basic_get_null(self, client):
        # GET basic/null
        basic_result = await client.basic.get_null()
        assert basic_result.id is None
        assert basic_result.name is None

    @pytest.mark.asyncio
    async def test_basic_get_not_provided(self, client):
        # GET basic/notprovided
        basic_result = await client.basic.get_not_provided()
        assert basic_result is None

    @pytest.mark.asyncio
    async def test_basic_get_invalid(self, client):
        # GET basic/invalid
        with pytest.raises(DeserializationError):
            await client.basic.get_invalid()

    # COMPLEX TYPE WITH PRIMITIVE PROPERTIES

    @pytest.mark.asyncio
    async def test_primitive_get_and_put_int(self, client):
        # GET primitive/integer
        intResult = await client.primitive.get_int()
        assert -1 ==  intResult.field1
        assert 2 ==  intResult.field2

        # PUT primitive/integer
        intRequest = {'field1':-1, 'field2':2}
        await client.primitive.put_int(intRequest)

    @pytest.mark.asyncio
    async def test_primitive_get_and_put_long(self, client):
        # GET primitive/long
        longResult = await client.primitive.get_long()
        assert 1099511627775 ==  longResult.field1
        assert -999511627788 ==  longResult.field2

        # PUT primitive/long
        longRequest = {'field1':1099511627775, 'field2':-999511627788}
        await client.primitive.put_long(longRequest)

    @pytest.mark.asyncio
    async def test_primitive_get_and_put_float(self, client):
        # GET primitive/float
        floatResult = await client.primitive.get_float()
        assert 1.05 ==  floatResult.field1
        assert -0.003 ==  floatResult.field2

        # PUT primitive/float
        floatRequest = FloatWrapper(field1=1.05, field2=-0.003)
        await client.primitive.put_float(floatRequest)

    @pytest.mark.asyncio
    async def test_primitive_get_and_put_double(self, client):
        # GET primitive/double
        doubleResult = await client.primitive.get_double()
        assert 3e-100 ==  doubleResult.field1
        assert -5e-57 ==  doubleResult.field_56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose

        # PUT primitive/double
        doubleRequest = {'field1':3e-100}
        doubleRequest['field_56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose'] = -5e-57
        await client.primitive.put_double(doubleRequest)

    @pytest.mark.asyncio
    async def test_primitive_get_and_put_bool(self, client):
        # GET primitive/bool
        boolResult = await client.primitive.get_bool()
        assert boolResult.field_true
        assert not boolResult.field_false

        # PUT primitive/bool
        boolRequest = BooleanWrapper(field_true=True, field_false=False)
        await client.primitive.put_bool(boolRequest)

    @pytest.mark.asyncio
    async def test_primitive_get_and_put_string(self, client):
        # GET primitive/string
        stringResult = await client.primitive.get_string()
        assert "goodrequest" ==  stringResult.field
        assert "" ==  stringResult.empty
        assert stringResult.null is None

        # PUT primitive/string
        stringRequest = StringWrapper(null=None, empty="", field="goodrequest")
        await client.primitive.put_string(stringRequest)

    @pytest.mark.asyncio
    async def test_primitive_get_and_put_date(self, client):
        # GET primitive/date
        dateResult = await client.primitive.get_date()
        assert isodate.parse_date("0001-01-01") ==  dateResult.field
        assert isodate.parse_date("2016-02-29") ==  dateResult.leap

        dateRequest = DateWrapper(
            field=isodate.parse_date('0001-01-01'),
            leap=isodate.parse_date('2016-02-29'))
        await client.primitive.put_date(dateRequest)

    @pytest.mark.asyncio
    async def test_primitive_get_and_put_date_time(self, client, min_date):
        # GET primitive/datetime
        datetimeResult = await client.primitive.get_date_time()

        assert min_date ==  datetimeResult.field

        datetime_request = DatetimeWrapper(
            field=isodate.parse_datetime("0001-01-01T00:00:00Z"),
            now=isodate.parse_datetime("2015-05-18T18:38:00Z"))
        await client.primitive.put_date_time(datetime_request)

    @pytest.mark.asyncio
    async def test_primitive_get_and_put_date_time_rfc1123(self, client, min_date):
        # GET primitive/datetimerfc1123
        datetimeRfc1123Result = await client.primitive.get_date_time_rfc1123()
        assert min_date ==  datetimeRfc1123Result.field

        datetime_request = Datetimerfc1123Wrapper(
            field=isodate.parse_datetime("0001-01-01T00:00:00Z"),
            now=isodate.parse_datetime("2015-05-18T11:38:00Z"))
        await client.primitive.put_date_time_rfc1123(datetime_request)

    @pytest.mark.asyncio
    async def test_primitive_get_and_put_duration(self, client):
        # GET primitive/duration
        expected = timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11)
        assert expected ==  (await client.primitive.get_duration()).field

        await client.primitive.put_duration(expected)

    @pytest.mark.asyncio
    async def test_primitive_get_and_put_byte(self, client):
        # GET primitive/byte
        byteResult = await client.primitive.get_byte()
        valid_bytes = bytearray([0x0FF, 0x0FE, 0x0FD, 0x0FC, 0x000, 0x0FA, 0x0F9, 0x0F8, 0x0F7, 0x0F6])
        assert valid_bytes ==  byteResult.field

        # PUT primitive/byte
        await client.primitive.put_byte(valid_bytes)

    # COMPLEX TYPE WITH READ ONLY PROPERTIES

    @pytest.mark.asyncio
    async def test_readonlyproperty_get_and_put_valid(self, client):
        # GET readonly/valid
        valid_obj = ReadonlyObj(size=2)
        valid_obj.id = '1234'
        readonly_result = await client.readonlyproperty.get_valid()
        assert readonly_result ==  valid_obj

        # PUT readonly/valid
        readonly_result = await client.readonlyproperty.put_valid(2)
        assert readonly_result is None

    # COMPLEX TYPE WITH ARRAY PROPERTIES

    @pytest.mark.asyncio
    async def test_array_get_and_put_valid(self, client):
        # GET array/valid
        array_result = await client.array.get_valid()
        assert 5 ==  len(array_result.array)

        array_value = ["1, 2, 3, 4", "", None, "&S#$(*Y",
                       "The quick brown fox jumps over the lazy dog"]
        assert array_result.array ==  array_value

        # PUT array/valid
        await client.array.put_valid(array_value)

    @pytest.mark.asyncio
    async def test_array_get_and_put_empty(self, client):

        # GET array/empty
        array_result = await client.array.get_empty()
        assert 0 ==  len(array_result.array)

        # PUT array/empty
        await client.array.put_empty([])

    async def test_array_get_not_provided(self, client):
        # Get array/notprovided
        assert await client.array.get_not_provided().array is None

    # COMPLEX TYPE WITH DICTIONARY PROPERTIES

    @pytest.mark.asyncio
    async def test_dictionary_get_and_put_valid(self, client):
        # GET dictionary/valid
        dict_result = await client.dictionary.get_valid()
        assert 5 ==  len(dict_result.default_program)

        dict_val = {'txt':'notepad', 'bmp':'mspaint', 'xls':'excel', 'exe':'', '':None}
        assert dict_val ==  dict_result.default_program

        # PUT dictionary/valid
        await client.dictionary.put_valid(dict_val)

    @pytest.mark.asyncio
    async def test_dictionary_get_and_put_empty(self, client):
        # GET dictionary/empty
        dict_result = await client.dictionary.get_empty()
        assert 0 ==  len(dict_result.default_program)

        # PUT dictionary/empty
        await client.dictionary.put_empty(default_program={})

    @pytest.mark.asyncio
    async def test_dictionary_get_and_null(self, client):
        # GET dictionary/null
        assert (await client.dictionary.get_null()).default_program is None

    @pytest.mark.asyncio
    async def test_dictionary_get_not_provided(self, client):
        # GET dictionary/notprovided
        assert (await client.dictionary.get_not_provided()).default_program is None

    # COMPLEX TYPES THAT INVOLVE INHERITANCE

    @pytest.mark.asyncio
    async def test_inheritance_get_and_put_valid(self, client):
        # GET inheritance/valid
        inheritanceResult = await client.inheritance.get_valid()
        assert 2 ==  inheritanceResult.id
        assert "Siameeee" ==  inheritanceResult.name
        assert -1 ==  inheritanceResult.hates[1].id
        assert "Tomato" ==  inheritanceResult.hates[1].name

        # PUT inheritance/valid
        request = {
            'id': 2,
            'name': "Siameeee",
            'color': "green",
            'breed': "persian",
            'hates': [Dog(id=1, name="Potato", food="tomato"),
                   Dog(id=-1, name="Tomato", food="french fries")]
            }
        await client.inheritance.put_valid(request)

    # COMPLEX TYPES THAT INVOLVE POLYMORPHISM

    @pytest.mark.asyncio
    async def test_polymorphism_get_and_put_valid(self, client):
        # GET polymorphism/valid
        result = await client.polymorphism.get_valid()
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
        await client.polymorphism.put_valid(request)

    @pytest.mark.asyncio
    async def test_polymorphism_put_valid_missing_required(self, client):
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

        with pytest.raises(ValidationError):
            await client.polymorphism.put_valid_missing_required(bad_request)

    # COMPLEX TYPES THAT INVOLVE RECURSIVE REFERENCE

    @pytest.mark.asyncio
    async def test_polymorphismrecursive_get_and_put_valid(self, client):
        # GET polymorphicrecursive/valid
        result = await client.polymorphicrecursive.get_valid()
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
        await client.polymorphicrecursive.put_valid(request)


    # Complex types that uses additional properties and polymorphism

    @pytest.mark.asyncio
    async def test_polymorphism_get_and_put_complicated(self, client):
        smart_salmon = await client.polymorphism.get_complicated()
        await client.polymorphism.put_complicated(smart_salmon)

    # Complex types that uses missing discriminator

    @pytest.mark.asyncio
    async def test_polymorphism_get_and_put_missing_discriminator(self, client):
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
        await client.polymorphism.put_missing_discriminator(regular_salmon)

        # Dot syntax
        dot_salmon = await client.polymorphism.get_dot_syntax()
        assert dot_salmon.fishtype == "DotSalmon"
        assert dot_salmon.location == "sweden"
