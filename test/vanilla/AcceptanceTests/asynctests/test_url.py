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

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "Url"))
sys.path.append(join(tests, "UrlMultiCollectionFormat"))

from msrest.exceptions import DeserializationError, ValidationError

from url.aio import AutoRestUrlTestService
from urlmulticollectionformat.aio import AutoRestUrlMutliCollectionFormatTestService
from url.models import UriColor

import pytest

@pytest.fixture
def client():
    return AutoRestUrlTestService('', base_url="http://localhost:3000")

@pytest.fixture
def multi_client():
    return AutoRestUrlMutliCollectionFormatTestService("http://localhost:3000")

class TestUrl(object):

    @pytest.mark.asyncio
    async def test_url_path(self, client):

        client.config.global_string_path = ''

        await client.paths.byte_empty()

        with pytest.raises(ValidationError):
            await client.paths.byte_null(None)

        u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
        await client.paths.byte_multi_byte(u_bytes)

        with pytest.raises(ValidationError):
            await client.paths.date_null(None)

        with pytest.raises(ValidationError):
            await client.paths.date_time_null(None)

        await client.paths.date_time_valid()
        await client.paths.date_valid()
        await client.paths.unix_time_url(datetime(year=2016, month=4, day=13))

        await client.paths.double_decimal_negative()
        await client.paths.double_decimal_positive()

        await client.paths.float_scientific_negative()
        await client.paths.float_scientific_positive()
        await client.paths.get_boolean_false()
        await client.paths.get_boolean_true()
        await client.paths.get_int_negative_one_million()
        await client.paths.get_int_one_million()
        await client.paths.get_negative_ten_billion()
        await client.paths.get_ten_billion()
        await client.paths.string_empty()

        test_array = ["ArrayPath1", r"begin!*'();:@ &=+$,/?#[]end", None, ""]
        await client.paths.array_csv_in_path(test_array)

        with pytest.raises(ValidationError):
            await client.paths.string_null(None)

        await client.paths.string_url_encoded()
        await client.paths.enum_valid(UriColor.greencolor)

        with pytest.raises(ValidationError):
            await client.paths.enum_null(None)

        await client.paths.base64_url("lorem".encode())

    @pytest.mark.asyncio
    async def test_url_query(self, client, multi_client):

        client.config.global_string_path = ''

        await client.queries.byte_empty()
        u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
        await client.queries.byte_multi_byte(u_bytes)
        await client.queries.byte_null()
        await client.queries.date_null()
        await client.queries.date_time_null()
        await client.queries.date_time_valid()
        await client.queries.date_valid()
        await client.queries.double_null()
        await client.queries.double_decimal_negative()
        await client.queries.double_decimal_positive()
        await client.queries.float_scientific_negative()
        await client.queries.float_scientific_positive()
        await client.queries.float_null()
        await client.queries.get_boolean_false()
        await client.queries.get_boolean_true()
        await client.queries.get_boolean_null()
        await client.queries.get_int_negative_one_million()
        await client.queries.get_int_one_million()
        await client.queries.get_int_null()
        await client.queries.get_negative_ten_billion()
        await client.queries.get_ten_billion()
        await client.queries.get_long_null()
        await client.queries.string_empty()
        await client.queries.string_null()
        await client.queries.string_url_encoded()
        await client.queries.enum_valid(UriColor.greencolor)
        await client.queries.enum_null(None)
        await client.queries.array_string_csv_empty([])
        await client.queries.array_string_csv_null(None)
        test_array = ["ArrayQuery1", r"begin!*'();:@ &=+$,/?#[]end", None, ""]
        await client.queries.array_string_csv_valid(test_array)
        await client.queries.array_string_pipes_valid(test_array)
        await client.queries.array_string_ssv_valid(test_array)
        await client.queries.array_string_tsv_valid(test_array)

        await multi_client.queries.array_string_multi_empty([])
        await multi_client.queries.array_string_multi_null()
        await multi_client.queries.array_string_multi_valid(test_array)

    @pytest.mark.asyncio
    async def test_url_mixed(self, client):

        client.config.global_string_path = "globalStringPath"
        client.config.global_string_query = "globalStringQuery"

        await client.path_items.get_all_with_values("localStringPath", "pathItemStringPath",
                "localStringQuery", "pathItemStringQuery")

        client.config.global_string_query = None
        await client.path_items.get_global_and_local_query_null("localStringPath", "pathItemStringPath",
                None, "pathItemStringQuery")

        await client.path_items.get_global_query_null("localStringPath", "pathItemStringPath",
                "localStringQuery", "pathItemStringQuery")

        client.config.global_string_query = "globalStringQuery"
        await client.path_items.get_local_path_item_query_null("localStringPath", "pathItemStringPath",
                None, None)
