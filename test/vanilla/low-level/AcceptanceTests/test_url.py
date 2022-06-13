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
from urllowlevel import AutoRestUrlTestService
from urllowlevel.rest import queries, paths, path_items
from urlmulticollectionformatlowlevel import AutoRestUrlMutliCollectionFormatTestService
from urlmulticollectionformatlowlevel.rest import queries as multiqueries

import pytest

@pytest.fixture
def client():
    with AutoRestUrlTestService('') as client:
        yield client

@pytest.fixture
def multi_client():
    with AutoRestUrlMutliCollectionFormatTestService() as client:
        yield client

@pytest.fixture
def send_request(client, base_send_request):
    def _send_request(request):
        return base_send_request(client, request)
    return _send_request

@pytest.fixture
def make_multi_request(multi_client, base_send_request):
    def _send_request(request):
        return base_send_request(multi_client, request)
    return _send_request

@pytest.fixture
def test_array_query():
    return ["ArrayQuery1", r"begin!*'();:@ &=+$,/?#[]end", None, ""]

def test_byte_empty_and_null(send_request):
    request = paths.build_byte_empty_request()
    send_request(request)

    with pytest.raises(ValueError):
        paths.build_byte_null_request(None)

def test_byte_multi_byte(send_request):
    u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
    request = paths.build_byte_multi_byte_request(u_bytes)
    send_request(request)

def test_date_null(send_request):
    with pytest.raises(ValueError):
        paths.build_date_null_request(None)

def test_date_time_null(send_request):
    with pytest.raises(ValueError):
        paths.build_date_time_null_request(None)

def test_date_time_valid(send_request):
    request = paths.build_date_time_valid_request()
    send_request(request)

def test_date_valid(send_request):
    request = paths.build_date_valid_request()
    send_request(request)

def test_unix_time_url(send_request):
    request = paths.build_unix_time_url_request(datetime(year=2016, month=4, day=13))
    send_request(request)

def test_double_decimal(send_request):
    request = paths.build_double_decimal_negative_request()
    send_request(request)
    request = paths.build_double_decimal_positive_request()
    send_request(request)

def test_float_scientific(send_request):
    request = paths.build_float_scientific_negative_request()
    send_request(request)

    request = paths.build_float_scientific_positive_request()
    send_request(request)

def test_get_boolean(send_request):
    request = paths.build_get_boolean_false_request()
    send_request(request)

    request = paths.build_get_boolean_true_request()
    send_request(request)

def test_int(send_request):
    request = paths.build_get_int_negative_one_million_request()
    send_request(request)

    request = paths.build_get_int_one_million_request()
    send_request(request)

def test_get_long(send_request):
    request = paths.build_get_negative_ten_billion_request()
    send_request(request)

    request = paths.build_get_ten_billion_request()
    send_request(request)

def test_string_empty_and_null(send_request):
    request = paths.build_string_empty_request()
    send_request(request)

    with pytest.raises(ValueError):
        paths.build_string_null_request(None)

def test_array_csv_in_path(send_request):
    test_array = ["ArrayPath1", r"begin!*'();:@ &=+$,/?#[]end", None, ""]
    request = paths.build_array_csv_in_path_request(test_array)
    send_request(request)

def test_string_url_encoded(send_request):
    request = paths.build_string_url_encoded_request()
    send_request(request)

def test_paths_unicode(send_request):
    request = paths.build_string_unicode_request()
    send_request(request)

def test_string_url_non_encoded(send_request):
    request = paths.build_string_url_non_encoded_request()
    send_request(request)

def test_enum_valid(send_request):
    request = paths.build_enum_valid_request("green color")
    send_request(request)

def test_enum_null(send_request):
    with pytest.raises(ValueError):
        paths.build_enum_null_request(None)

def test_base64_url(send_request):
    request = paths.build_base64_url_request("lorem".encode())
    send_request(request)

def test_queries_byte(send_request):
    request = queries.build_byte_empty_request()
    send_request(request)

    u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
    request = queries.build_byte_multi_byte_request(byte_query=u_bytes)
    send_request(request)

    request = queries.build_byte_null_request()
    send_request(request)

def test_queries_date(send_request):
    request = queries.build_date_null_request()
    send_request(request)

    request = queries.build_date_valid_request()
    send_request(request)

def test_queries_date_time(send_request):
    request = queries.build_date_time_null_request()
    send_request(request)

    request = queries.build_date_time_valid_request()
    send_request(request)

def test_queries_double(send_request):
    request = queries.build_double_null_request()
    send_request(request)

    request = queries.build_double_decimal_negative_request()
    send_request(request)

    request = queries.build_double_decimal_positive_request()
    send_request(request)

def test_queries_float_scientific(send_request):
    request = queries.build_float_scientific_negative_request()
    send_request(request)

    request = queries.build_float_scientific_positive_request()
    send_request(request)
    request = queries.build_float_null_request()
    send_request(request)

def test_queries_boolean(send_request):
    request = queries.build_get_boolean_false_request()
    send_request(request)

    request = queries.build_get_boolean_true_request()
    send_request(request)

    request = queries.build_get_boolean_null_request()
    send_request(request)

def test_queries_int(send_request):
    request = queries.build_get_int_negative_one_million_request()
    send_request(request)

    request = queries.build_get_int_one_million_request()
    send_request(request)

    request = queries.build_get_int_null_request()
    send_request(request)

def test_queries_long(send_request):
    request = queries.build_get_negative_ten_billion_request()
    send_request(request)

    request = queries.build_get_ten_billion_request()
    send_request(request)

    request = queries.build_get_long_null_request()
    send_request(request)

def test_queries_string(send_request):
    request = queries.build_string_empty_request()
    send_request(request)

    request = queries.build_string_null_request()
    send_request(request)

    request = queries.build_string_url_encoded_request()
    send_request(request)

def test_queries_enum(send_request):
    request = queries.build_enum_valid_request(enum_query="green color")
    send_request(request)

    request = queries.build_enum_null_request(enum_query=None)
    send_request(request)

def test_queries_unicode(send_request):
    request = queries.build_string_unicode_request()
    send_request(request)

def test_array_string_csv(send_request, test_array_query):
    request = queries.build_array_string_csv_empty_request(array_query=[])
    send_request(request)

    request = queries.build_array_string_csv_null_request(array_query=None)
    send_request(request)

    request = queries.build_array_string_csv_valid_request(array_query=test_array_query)
    send_request(request)

def test_array_string_miscellaneous(send_request, test_array_query):
    request = queries.build_array_string_pipes_valid_request(array_query=test_array_query)
    send_request(request)

    request = queries.build_array_string_ssv_valid_request(array_query=test_array_query)
    send_request(request)

    request = queries.build_array_string_tsv_valid_request(array_query=test_array_query)
    send_request(request)

def test_array_string_multi(make_multi_request, test_array_query):
    request = multiqueries.build_array_string_multi_empty_request(array_query=[])
    make_multi_request(request)

    request = multiqueries.build_array_string_multi_null_request()
    make_multi_request(request)

    request = multiqueries.build_array_string_multi_valid_request(array_query=test_array_query)
    make_multi_request(request)

def test_array_string_no_collection_format(send_request):
    request = queries.build_array_string_no_collection_format_empty_request(array_query=['hello', 'nihao', 'bonjour'])
    send_request(request)

def test_get_all_with_values(send_request):
    # In LLC, we have to pass in global variables to individual operations; we don't have access to the client in the request builders
    global_string_path = "globalStringPath"
    global_string_query = "globalStringQuery"

    request = path_items.build_get_all_with_values_request(
        path_item_string_path="pathItemStringPath",
        global_string_path=global_string_path,
        local_string_path="localStringPath",
        path_item_string_query="pathItemStringQuery",
        global_string_query=global_string_query,
        local_string_query="localStringQuery",
    )

    send_request(request)

def test_get_global_and_local_query_null(send_request):
    # In LLC, we have to pass in global variables to individual operations; we don't have access to the client in the request builders
    global_string_path = "globalStringPath"

    request = path_items.build_get_global_and_local_query_null_request(
        path_item_string_path="pathItemStringPath",
        global_string_path=global_string_path,
        local_string_path="localStringPath",
        path_item_string_query="pathItemStringQuery",
        global_string_query=None
    )
    send_request(request)

def test_get_global_query_null(send_request):
    # In LLC, we have to pass in global variables to individual operations; we don't have access to the client in the request builders
    global_string_path = "globalStringPath"

    request = path_items.build_get_global_query_null_request(
        path_item_string_path="pathItemStringPath",
        global_string_path=global_string_path,
        local_string_path="localStringPath",
        path_item_string_query="pathItemStringQuery",
        local_string_query="localStringQuery",
    )
    send_request(request)

def test_get_local_path_item_query_null(send_request):
    # In LLC, we have to pass in global variables to individual operations; we don't have access to the client in the request builders
    global_string_path = "globalStringPath"
    global_string_query = "globalStringQuery"

    request = path_items.build_get_local_path_item_query_null_request(
        path_item_string_path="pathItemStringPath",
        global_string_path=global_string_path,
        local_string_path="localStringPath",
        path_item_string_query=None,
        global_string_query=global_string_query,
        local_string_query=None,
    )
    send_request(request)
