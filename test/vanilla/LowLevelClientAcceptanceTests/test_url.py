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

from datetime import datetime
from url import AutoRestUrlTestService
from url._rest import *
from urlmulticollectionformat import AutoRestUrlMutliCollectionFormatTestService
from urlmulticollectionformat._rest import *
from url.models import UriColor
from msrest.exceptions import ValidationError

import pytest

@pytest.fixture
def client():
    with AutoRestUrlTestService('', base_url="http://localhost:3000") as client:
        yield client

@pytest.fixture
def multi_client():
    with AutoRestUrlMutliCollectionFormatTestService("http://localhost:3000") as client:
        yield client

@pytest.fixture
def make_request(client, base_make_request):
    def _make_request(request):
        return base_make_request(client, request)
    return _make_request

@pytest.fixture
def make_multi_request(multi_client, base_make_request):
    def _make_request(request):
        return base_make_request(multi_client, request)
    return _make_request

@pytest.fixture
def test_array_query():
    return ["ArrayQuery1", r"begin!*'();:@ &=+$,/?#[]end", None, ""]

def test_byte_empty_and_null(make_request):
    request = build_paths_byte_empty_request()
    make_request(request)

    with pytest.raises(ValidationError):
        build_paths_byte_null_request(None)

def test_byte_multi_byte(make_request):
    u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
    request = build_paths_byte_multi_byte_request(u_bytes)
    make_request(request)

def test_date_null(make_request):
    with pytest.raises(ValidationError):
        build_paths_date_null_request(None)

def test_date_time_null(make_request):
    with pytest.raises(ValidationError):
        build_paths_date_time_null_request(None)

def test_date_time_valid(make_request):
    request = build_paths_date_time_valid_request()
    make_request(request)

def test_date_valid(make_request):
    request = build_paths_date_valid_request()
    make_request(request)

def test_unix_time_url(make_request):
    request = build_paths_unix_time_url_request(datetime(year=2016, month=4, day=13))
    make_request(request)

def test_double_decimal(make_request):
    request = build_paths_double_decimal_negative_request()
    make_request(request)
    request = build_paths_double_decimal_positive_request()
    make_request(request)

def test_float_scientific(make_request):
    request = build_paths_float_scientific_negative_request()
    make_request(request)

    request = build_paths_float_scientific_positive_request()
    make_request(request)

def test_get_boolean(make_request):
    request = build_paths_get_boolean_false_request()
    make_request(request)

    request = build_paths_get_boolean_true_request()
    make_request(request)

def test_int(make_request):
    request = build_paths_get_int_negative_one_million_request()
    make_request(request)

    request = build_paths_get_int_one_million_request()
    make_request(request)

def test_get_long(make_request):
    request = build_paths_get_negative_ten_billion_request()
    make_request(request)

    request = build_paths_get_ten_billion_request()
    make_request(request)

def test_string_empty_and_null(make_request):
    request = build_paths_string_empty_request()
    make_request(request)

    with pytest.raises(ValidationError):
        build_paths_string_null_request(None)

def test_array_csv_in_path(make_request):
    test_array = ["ArrayPath1", r"begin!*'();:@ &=+$,/?#[]end", None, ""]
    request = build_paths_array_csv_in_path_request(test_array)
    make_request(request)

def test_string_url_encoded(make_request):
    request = build_paths_string_url_encoded_request()
    make_request(request)

def test_paths_unicode(make_request):
    request = build_paths_string_unicode_request()
    make_request(request)

def test_string_url_non_encoded(make_request):
    request = build_paths_string_url_non_encoded_request()
    make_request(request)

def test_enum_valid(make_request):
    request = build_paths_enum_valid_request(UriColor.GREEN_COLOR)
    make_request(request)

def test_enum_null(make_request):
    with pytest.raises(ValidationError):
        build_paths_enum_null_request(None)

def test_base64_url(make_request):
    request = build_paths_base64_url_request("lorem".encode())
    make_request(request)

def test_queries_byte(make_request):
    request = build_queries_byte_empty_request()
    make_request(request)

    u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
    request = build_queries_byte_multi_byte_request(byte_query=u_bytes)
    make_request(request)

    request = build_queries_byte_null_request()
    make_request(request)

def test_queries_date(make_request):
    request = build_queries_date_null_request()
    make_request(request)

    request = build_queries_date_valid_request()
    make_request(request)

def test_queries_date_time(make_request):
    request = build_queries_date_time_null_request()
    make_request(request)

    request = build_queries_date_time_valid_request()
    make_request(request)

def test_queries_double(make_request):
    request = build_queries_double_null_request()
    make_request(request)

    request = build_queries_double_decimal_negative_request()
    make_request(request)

    request = build_queries_double_decimal_positive_request()
    make_request(request)

def test_queries_float_scientific(make_request):
    request = build_queries_float_scientific_negative_request()
    make_request(request)

    request = build_queries_float_scientific_positive_request()
    make_request(request)
    request = build_queries_float_null_request()
    make_request(request)

def test_queries_boolean(make_request):
    request = build_queries_get_boolean_false_request()
    make_request(request)

    request = build_queries_get_boolean_true_request()
    make_request(request)

    request = build_queries_get_boolean_null_request()
    make_request(request)

def test_queries_int(make_request):
    request = build_queries_get_int_negative_one_million_request()
    make_request(request)

    request = build_queries_get_int_one_million_request()
    make_request(request)

    request = build_queries_get_int_null_request()
    make_request(request)

def test_queries_long(make_request):
    request = build_queries_get_negative_ten_billion_request()
    make_request(request)

    request = build_queries_get_ten_billion_request()
    make_request(request)

    request = build_queries_get_long_null_request()
    make_request(request)

def test_queries_string(make_request):
    request = build_queries_string_empty_request()
    make_request(request)

    request = build_queries_string_null_request()
    make_request(request)

    request = build_queries_string_url_encoded_request()
    make_request(request)

def test_queries_enum(make_request):
    request = build_queries_enum_valid_request(enum_query=UriColor.GREEN_COLOR)
    make_request(request)

    request = build_queries_enum_null_request(enum_query=None)
    make_request(request)

def test_queries_unicode(make_request):
    request = build_queries_string_unicode_request()
    make_request(request)

def test_array_string_csv(make_request, test_array_query):
    request = build_queries_array_string_csv_empty_request(array_query=[])
    make_request(request)

    request = build_queries_array_string_csv_null_request(array_query=None)
    make_request(request)

    request = build_queries_array_string_csv_valid_request(array_query=test_array_query)
    make_request(request)

def test_array_string_miscellaneous(make_request, test_array_query):
    request = build_queries_array_string_pipes_valid_request(array_query=test_array_query)
    make_request(request)

    request = build_queries_array_string_ssv_valid_request(array_query=test_array_query)
    make_request(request)

    request = build_queries_array_string_tsv_valid_request(array_query=test_array_query)
    make_request(request)

def test_array_string_multi(make_multi_request, test_array_query):
    request = build_queries_array_string_multi_empty_request(array_query=[])
    make_multi_request(request)

    request = build_queries_array_string_multi_null_request()
    make_multi_request(request)

    requst = build_queries_array_string_multi_valid_request(array_query=test_array_query)
    make_multi_request(request)

def test_array_string_no_collection_format(make_request):
    request = build_queries_array_string_no_collection_format_empty_request(array_query=['hello', 'nihao', 'bonjour'])
    make_request(request)

def test_get_all_with_values(make_request):
    # In LLC, we have to pass in global variables to individual operations; we don't have access to the client in the request builders
    global_string_path = "globalStringPath"
    global_string_query = "globalStringQuery"

    request = build_pathitems_get_all_with_values_request(
        path_item_string_path="pathItemStringPath",
        global_string_path=global_string_path,
        local_string_path="localStringPath",
        path_item_string_query="pathItemStringQuery",
        global_string_query=global_string_query,
        local_string_query="localStringQuery",
    )

    make_request(request)

def test_get_global_and_local_query_null(make_request):
    # In LLC, we have to pass in global variables to individual operations; we don't have access to the client in the request builders
    global_string_path = "globalStringPath"

    request = build_pathitems_get_global_and_local_query_null_request(
        path_item_string_path="pathItemStringPath",
        global_string_path=global_string_path,
        local_string_path="localStringPath",
        path_item_string_query="pathItemStringQuery",
        global_string_query=None
    )
    make_request(request)

def test_get_global_query_null(make_request):
    # In LLC, we have to pass in global variables to individual operations; we don't have access to the client in the request builders
    global_string_path = "globalStringPath"

    request = build_pathitems_get_global_query_null_request(
        path_item_string_path="pathItemStringPath",
        global_string_path=global_string_path,
        local_string_path="localStringPath",
        path_item_string_query="pathItemStringQuery",
        local_string_query="localStringQuery",
    )
    make_request(request)

def test_get_local_path_item_query_null(make_request):
    # In LLC, we have to pass in global variables to individual operations; we don't have access to the client in the request builders
    global_string_path = "globalStringPath"
    global_string_query = "globalStringQuery"

    request = build_pathitems_get_local_path_item_query_null_request(
        path_item_string_path="pathItemStringPath",
        global_string_path=global_string_path,
        local_string_path="localStringPath",
        path_item_string_query=None,
        global_string_query=global_string_query,
        local_string_query=None,
    )
    make_request(request)
