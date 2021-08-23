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
from msrest.exceptions import ValidationError

from urlversiontolerant import AutoRestUrlTestService
from urlmulticollectionformatversiontolerant import AutoRestUrlMutliCollectionFormatTestService

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
def test_array_query():
    return ["ArrayQuery1", r"begin!*'();:@ &=+$,/?#[]end", None, ""]

def test_byte_empty_and_null(client):
    client.paths.byte_empty()

    with pytest.raises(ValidationError):
        client.paths.byte_null(None)

def test_byte_multi_byte(client):
    u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
    client.paths.byte_multi_byte(u_bytes)

def test_date_null(client):
    with pytest.raises(ValidationError):
        client.paths.date_null(None)

def test_date_time_null(client):
    with pytest.raises(ValidationError):
        client.paths.date_time_null(None)

def test_date_time_valid(client):
    client.paths.date_time_valid()

def test_date_valid(client):
    client.paths.date_valid()

def test_unix_time_url(client):
    client.paths.unix_time_url(datetime(year=2016, month=4, day=13))

def test_double_decimal(client):
    client.paths.double_decimal_negative()
    client.paths.double_decimal_positive()

def test_float_scientific(client):
    client.paths.float_scientific_negative()
    client.paths.float_scientific_positive()

def test_get_boolean(client):
    client.paths.get_boolean_false()
    client.paths.get_boolean_true()

def test_int(client):
    client.paths.get_int_negative_one_million()
    client.paths.get_int_one_million()

def test_get_long(client):
    client.paths.get_negative_ten_billion()
    client.paths.get_ten_billion()

def test_string_empty_and_null(client):
    client.paths.string_empty()

    with pytest.raises(ValidationError):
        client.paths.string_null(None)

def test_array_csv_in_path(client):
    test_array = ["ArrayPath1", r"begin!*'();:@ &=+$,/?#[]end", None, ""]
    client.paths.array_csv_in_path(test_array)

def test_string_url_encoded(client):
    client.paths.string_url_encoded()

def test_paths_unicode(client):
    client.paths.string_unicode()

def test_string_url_non_encoded(client):
    client.paths.string_url_non_encoded()

def test_enum_valid(client):
    client.paths.enum_valid("green color")

def test_enum_null(client):
    with pytest.raises(ValidationError):
        client.paths.enum_null(None)

def test_base64_url(client):
    client.paths.base64_url("lorem".encode())

def test_queries_byte(client):
    client.queries.byte_empty()
    u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
    client.queries.byte_multi_byte(byte_query=u_bytes)
    client.queries.byte_null()

def test_queries_date(client):
    client.queries.date_null()
    client.queries.date_valid()

def test_queries_date_time(client):
    client.queries.date_time_null()
    client.queries.date_time_valid()

def test_queries_double(client):
    client.queries.double_null()
    client.queries.double_decimal_negative()
    client.queries.double_decimal_positive()

def test_queries_float_scientific(client):
    client.queries.float_scientific_negative()
    client.queries.float_scientific_positive()
    client.queries.float_null()

def test_queries_boolean(client):
    client.queries.get_boolean_false()
    client.queries.get_boolean_true()
    client.queries.get_boolean_null()

def test_queries_int(client):
    client.queries.get_int_negative_one_million()
    client.queries.get_int_one_million()
    client.queries.get_int_null()

def test_queries_long(client):
    client.queries.get_negative_ten_billion()
    client.queries.get_ten_billion()
    client.queries.get_long_null()

def test_queries_string(client):
    client.queries.string_empty()
    client.queries.string_null()
    client.queries.string_url_encoded()

def test_queries_enum(client):
    client.queries.enum_valid(enum_query="green color")
    client.queries.enum_null(enum_query=None)

def test_queries_unicode(client):
    client.queries.string_unicode()

def test_array_string_csv(client, test_array_query):
    client.queries.array_string_csv_empty(array_query=[])
    client.queries.array_string_csv_null(array_query=None)
    client.queries.array_string_csv_valid(array_query=test_array_query)

def test_array_string_miscellaneous(client, test_array_query):
    client.queries.array_string_pipes_valid(array_query=test_array_query)
    client.queries.array_string_ssv_valid(array_query=test_array_query)
    client.queries.array_string_tsv_valid(array_query=test_array_query)

def test_array_string_multi(multi_client, test_array_query):
    multi_client.queries.array_string_multi_empty(array_query=[])
    multi_client.queries.array_string_multi_null()
    multi_client.queries.array_string_multi_valid(array_query=test_array_query)

def test_array_string_no_collection_format(client):
    client.queries.array_string_no_collection_format_empty(array_query=['hello', 'nihao', 'bonjour'])

def test_get_all_with_values(client):
    client._config.global_string_path = "globalStringPath"
    client._config.global_string_query = "globalStringQuery"
    client.path_items.get_all_with_values(
        "pathItemStringPath",
        "localStringPath",
        path_item_string_query="pathItemStringQuery",
        local_string_query="localStringQuery",
    )

def test_get_global_and_local_query_null(client):
    client._config.global_string_path = "globalStringPath"
    client.path_items.get_global_and_local_query_null(
        "pathItemStringPath",
        "localStringPath",
        path_item_string_query="pathItemStringQuery",
        local_string_query=None,
    )

def test_get_global_query_null(client):
    client._config.global_string_path = "globalStringPath"
    client.path_items.get_global_query_null(
        "pathItemStringPath",
        "localStringPath",
        path_item_string_query="pathItemStringQuery",
        local_string_query="localStringQuery",
    )

def test_get_local_path_item_query_null(client):
    client._config.global_string_path = "globalStringPath"
    client._config.global_string_query = "globalStringQuery"
    client.path_items.get_local_path_item_query_null(
        "pathItemStringPath",
        "localStringPath",
        path_item_string_query=None,
        local_string_query=None,
    )

def test_operation_groups():
    from urlversiontolerant.operations import QueriesOperations
    from urlmulticollectionformatversiontolerant.operations import QueriesOperations as MultiCollectionFormatQueriesOperations

    with pytest.raises(ImportError):
        from urlversiontolerant.operations import _combine_operations_py3

    with pytest.raises(ImportError):
        from urlmulticollectionformatversiontolerant.operations import _combine_operations_py3

    from urlversiontolerant.operations._combine_operations import QueriesOperations as QueriesOperationsPy2
    assert QueriesOperations == QueriesOperationsPy2

    from urlmulticollectionformatversiontolerant.operations._combine_operations import QueriesOperations as QueriesOperationsPy2
    assert MultiCollectionFormatQueriesOperations == QueriesOperationsPy2