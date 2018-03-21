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

from url import AutoRestUrlTestService
from urlmulticollectionformat import AutoRestUrlMutliCollectionFormatTestService
from url.models.auto_rest_url_test_service_enums import UriColor

import pytest

@pytest.fixture
def client():
    return AutoRestUrlTestService('', base_url="http://localhost:3000")

@pytest.fixture
def multi_client():
    return AutoRestUrlMutliCollectionFormatTestService("http://localhost:3000")

class TestUrl(object):

    def test_url_path(self, client):

        client.config.global_string_path = ''

        client.paths.byte_empty()

        with pytest.raises(ValidationError):
            client.paths.byte_null(None)

        u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
        client.paths.byte_multi_byte(u_bytes)

        with pytest.raises(ValidationError):
            client.paths.date_null(None)

        with pytest.raises(ValidationError):
            client.paths.date_time_null(None)

        client.paths.date_time_valid()
        client.paths.date_valid()
        client.paths.unix_time_url(datetime(year=2016, month=4, day=13))

        client.paths.double_decimal_negative()
        client.paths.double_decimal_positive()

        client.paths.float_scientific_negative()
        client.paths.float_scientific_positive()
        client.paths.get_boolean_false()
        client.paths.get_boolean_true()
        client.paths.get_int_negative_one_million()
        client.paths.get_int_one_million()
        client.paths.get_negative_ten_billion()
        client.paths.get_ten_billion()
        client.paths.string_empty()

        test_array = ["ArrayPath1", r"begin!*'();:@ &=+$,/?#[]end", None, ""]
        client.paths.array_csv_in_path(test_array)

        with pytest.raises(ValidationError):
            client.paths.string_null(None)

        client.paths.string_url_encoded()
        client.paths.enum_valid(UriColor.greencolor)

        with pytest.raises(ValidationError):
            client.paths.enum_null(None)

        client.paths.base64_url("lorem".encode())

    def test_url_query(self, client, multi_client):

        client.config.global_string_path = ''

        client.queries.byte_empty()
        u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
        client.queries.byte_multi_byte(u_bytes)
        client.queries.byte_null()
        client.queries.date_null()
        client.queries.date_time_null()
        client.queries.date_time_valid()
        client.queries.date_valid()
        client.queries.double_null()
        client.queries.double_decimal_negative()
        client.queries.double_decimal_positive()
        client.queries.float_scientific_negative()
        client.queries.float_scientific_positive()
        client.queries.float_null()
        client.queries.get_boolean_false()
        client.queries.get_boolean_true()
        client.queries.get_boolean_null()
        client.queries.get_int_negative_one_million()
        client.queries.get_int_one_million()
        client.queries.get_int_null()
        client.queries.get_negative_ten_billion()
        client.queries.get_ten_billion()
        client.queries.get_long_null()
        client.queries.string_empty()
        client.queries.string_null()
        client.queries.string_url_encoded()
        client.queries.enum_valid(UriColor.greencolor)
        client.queries.enum_null(None)
        client.queries.array_string_csv_empty([])
        client.queries.array_string_csv_null(None)
        test_array = ["ArrayQuery1", r"begin!*'();:@ &=+$,/?#[]end", None, ""]
        client.queries.array_string_csv_valid(test_array)
        client.queries.array_string_pipes_valid(test_array)
        client.queries.array_string_ssv_valid(test_array)
        client.queries.array_string_tsv_valid(test_array)

        multi_client.queries.array_string_multi_empty([])
        multi_client.queries.array_string_multi_null()
        multi_client.queries.array_string_multi_valid(test_array)

    def test_url_mixed(self, client):

        client.config.global_string_path = "globalStringPath"
        client.config.global_string_query = "globalStringQuery"

        client.path_items.get_all_with_values("localStringPath", "pathItemStringPath",
                "localStringQuery", "pathItemStringQuery")

        client.config.global_string_query = None
        client.path_items.get_global_and_local_query_null("localStringPath", "pathItemStringPath",
                None, "pathItemStringQuery")

        client.path_items.get_global_query_null("localStringPath", "pathItemStringPath",
                "localStringQuery", "pathItemStringQuery")

        client.config.global_string_query = "globalStringQuery"
        client.path_items.get_local_path_item_query_null("localStringPath", "pathItemStringPath",
                None, None)

if __name__ == '__main__':
    unittest.main()
