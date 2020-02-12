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
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

from msrest.exceptions import DeserializationError, ValidationError

from url.aio import AutoRestUrlTestService
from urlmulticollectionformat.aio import AutoRestUrlMutliCollectionFormatTestService
from url.models import UriColor

import pytest


@pytest.fixture
async def client():
    async with AutoRestUrlTestService('', base_url="http://localhost:3000") as client:
        yield client

@pytest.fixture
async def multi_client():
    async with AutoRestUrlMutliCollectionFormatTestService("http://localhost:3000") as client:
        yield client

@pytest.fixture
def test_array_query():
    return ["ArrayQuery1", r"begin!*'();:@ &=+$,/?#[]end", None, ""]

class TestUrl(object):

    @pytest.mark.asyncio
    async def test_byte_empty_and_null(self, client):
        await client.paths.byte_empty()

        with pytest.raises(ValidationError):
            await client.paths.byte_null(None)

    @pytest.mark.asyncio
    async def test_byte_multi_byte(self, client):
        u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
        await client.paths.byte_multi_byte(u_bytes)

    @pytest.mark.asyncio
    async def test_date_null(self, client):
        with pytest.raises(ValidationError):
            await client.paths.date_null(None)

    @pytest.mark.asyncio
    async def test_date_time_null(self, client):
        with pytest.raises(ValidationError):
            await client.paths.date_time_null(None)

    @pytest.mark.asyncio
    async def test_date_time_valid(self, client):
        await client.paths.date_time_valid()

    @pytest.mark.asyncio
    async def test_date_valid(self, client):
        await client.paths.date_valid()

    @pytest.mark.asyncio
    async def test_unix_time_url(self, client):
        await client.paths.unix_time_url(datetime(year=2016, month=4, day=13))

    @pytest.mark.asyncio
    async def test_double_decimal(self, client):
        await client.paths.double_decimal_negative()
        await client.paths.double_decimal_positive()

    @pytest.mark.asyncio
    async def test_float_scientific(self, client):
        await client.paths.float_scientific_negative()
        await client.paths.float_scientific_positive()

    @pytest.mark.asyncio
    async def test_get_boolean(self, client):
        await client.paths.get_boolean_false()
        await client.paths.get_boolean_true()

    @pytest.mark.asyncio
    async def test_int(self, client):
        await client.paths.get_int_negative_one_million()
        await client.paths.get_int_one_million()

    @pytest.mark.asyncio
    async def test_get_long(self, client):
        await client.paths.get_negative_ten_billion()
        await client.paths.get_ten_billion()

    @pytest.mark.asyncio
    async def test_string_empty_and_null(self, client):
        await client.paths.string_empty()

        with pytest.raises(ValidationError):
            await client.paths.string_null(None)

    @pytest.mark.asyncio
    async def test_array_csv_in_path(self, client):
        test_array = ["ArrayPath1", r"begin!*'();:@ &=+$,/?#[]end", None, ""]
        await client.paths.array_csv_in_path(test_array)

    @pytest.mark.asyncio
    async def test_string_url_encoded(self, client):
        await client.paths.string_url_encoded()

    @pytest.mark.asyncio
    async def test_string_url_non_encoded(self, client):
        await client.paths.string_url_non_encoded()

    @pytest.mark.asyncio
    async def test_enum_valid(self, client):
        await client.paths.enum_valid(UriColor.green_color)

    @pytest.mark.asyncio
    async def test_enum_null(self, client):
        with pytest.raises(ValidationError):
            await client.paths.enum_null(None)

    @pytest.mark.asyncio
    async def test_base64_url(self, client):
        await client.paths.base64_url("lorem".encode())

    @pytest.mark.asyncio
    async def test_queries_byte(self, client):
        await client.queries.byte_empty()
        u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
        await client.queries.byte_multi_byte(u_bytes)
        await client.queries.byte_null()

    @pytest.mark.asyncio
    async def test_queries_date(self, client):
        await client.queries.date_null()
        await client.queries.date_valid()

    @pytest.mark.asyncio
    async def test_queries_date_time(self, client):
        await client.queries.date_time_null()
        await client.queries.date_time_valid()

    @pytest.mark.asyncio
    async def test_queries_double(self, client):
        await client.queries.double_null()
        await client.queries.double_decimal_negative()
        await client.queries.double_decimal_positive()

    @pytest.mark.asyncio
    async def test_queries_float_scientific(self, client):
        await client.queries.float_scientific_negative()
        await client.queries.float_scientific_positive()
        await client.queries.float_null()

    @pytest.mark.asyncio
    async def test_queries_boolean(self, client):
        await client.queries.get_boolean_false()
        await client.queries.get_boolean_true()
        await client.queries.get_boolean_null()

    @pytest.mark.asyncio
    async def test_queries_int(self, client):
        await client.queries.get_int_negative_one_million()
        await client.queries.get_int_one_million()
        await client.queries.get_int_null()

    @pytest.mark.asyncio
    async def test_queries_long(self, client):
        await client.queries.get_negative_ten_billion()
        await client.queries.get_ten_billion()
        await client.queries.get_long_null()

    @pytest.mark.asyncio
    async def test_queries_string(self, client):
        await client.queries.string_empty()
        await client.queries.string_null()
        await client.queries.string_url_encoded()

    @pytest.mark.asyncio
    async def test_queries_enum(self, client):
        await client.queries.enum_valid(UriColor.green_color)
        await client.queries.enum_null(None)

    @pytest.mark.asyncio
    async def test_array_string_csv(self, client, test_array_query):
        await client.queries.array_string_csv_empty([])
        await client.queries.array_string_csv_null(None)
        await client.queries.array_string_csv_valid(test_array_query)

    @pytest.mark.asyncio
    async def test_array_string_miscellaneous(self, client, test_array_query):
        await client.queries.array_string_pipes_valid(test_array_query)
        await client.queries.array_string_ssv_valid(test_array_query)
        await client.queries.array_string_tsv_valid(test_array_query)

    @pytest.mark.asyncio
    async def test_array_string_multi(self, multi_client, test_array_query):
        await multi_client.queries.array_string_multi_empty([])
        await multi_client.queries.array_string_multi_null()
        await multi_client.queries.array_string_multi_valid(test_array_query)

    @pytest.mark.asyncio
    async def test_get_all_with_values(self, client):
        client._config.global_string_path = "globalStringPath"
        client._config.global_string_query = "globalStringQuery"
        await client.path_items.get_all_with_values(
            "pathItemStringPath",
            "localStringPath",
            "pathItemStringQuery",
            "localStringQuery",
        )

    @pytest.mark.asyncio
    async def test_get_global_and_local_query_null(self, client):
        client._config.global_string_path = "globalStringPath"
        await client.path_items.get_global_and_local_query_null(
            "pathItemStringPath",
            "localStringPath",
            "pathItemStringQuery",
            None,
        )

    @pytest.mark.asyncio
    async def test_get_global_query_null(self, client):
        client._config.global_string_path = "globalStringPath"
        await client.path_items.get_global_query_null(
            "pathItemStringPath",
            "localStringPath",
            "pathItemStringQuery",
            "localStringQuery",
        )

    @pytest.mark.asyncio
    async def test_get_local_path_item_query_null(self, client):
        client._config.global_string_path = "globalStringPath"
        client._config.global_string_query = "globalStringQuery"
        await client.path_items.get_local_path_item_query_null(
            "pathItemStringPath",
            "localStringPath",
            None,
            None,
        )
