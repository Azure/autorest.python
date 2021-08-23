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
from datetime import datetime
from msrest.exceptions import ValidationError

from urlversiontolerant.aio import AutoRestUrlTestService
from urlmulticollectionformatversiontolerant.aio import AutoRestUrlMutliCollectionFormatTestService

import pytest

@pytest.fixture
@async_generator
async def client():
    async with AutoRestUrlTestService('') as client:
        await yield_(client)

@pytest.fixture
@async_generator
async def multi_client():
    async with AutoRestUrlMutliCollectionFormatTestService() as client:
        await yield_(client)

@pytest.fixture
def test_array_query():
    return ["ArrayQuery1", r"begin!*'();:@ &=+$,/?#[]end", None, ""]

@pytest.mark.asyncio
async def test_byte_empty_and_null(client):
    await client.paths.byte_empty()

    with pytest.raises(ValidationError):
        await client.paths.byte_null(None)

@pytest.mark.asyncio
async def test_byte_multi_byte(client):
    u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
    await client.paths.byte_multi_byte(u_bytes)

@pytest.mark.asyncio
async def test_date_null(client):
    with pytest.raises(ValidationError):
        await client.paths.date_null(None)

@pytest.mark.asyncio
async def test_date_time_null(client):
    with pytest.raises(ValidationError):
        await client.paths.date_time_null(None)

@pytest.mark.asyncio
async def test_date_time_valid(client):
    await client.paths.date_time_valid()

@pytest.mark.asyncio
async def test_date_valid(client):
    await client.paths.date_valid()

@pytest.mark.asyncio
async def test_unix_time_url(client):
    await client.paths.unix_time_url(datetime(year=2016, month=4, day=13))

@pytest.mark.asyncio
async def test_double_decimal(client):
    await client.paths.double_decimal_negative()
    await client.paths.double_decimal_positive()

@pytest.mark.asyncio
async def test_float_scientific(client):
    await client.paths.float_scientific_negative()
    await client.paths.float_scientific_positive()

@pytest.mark.asyncio
async def test_get_boolean(client):
    await client.paths.get_boolean_false()
    await client.paths.get_boolean_true()

@pytest.mark.asyncio
async def test_int(client):
    await client.paths.get_int_negative_one_million()
    await client.paths.get_int_one_million()

@pytest.mark.asyncio
async def test_get_long(client):
    await client.paths.get_negative_ten_billion()
    await client.paths.get_ten_billion()

@pytest.mark.asyncio
async def test_string_empty_and_null(client):
    await client.paths.string_empty()

    with pytest.raises(ValidationError):
        await client.paths.string_null(None)

@pytest.mark.asyncio
async def test_array_csv_in_path(client):
    test_array = ["ArrayPath1", r"begin!*'();:@ &=+$,/?#[]end", None, ""]
    await client.paths.array_csv_in_path(test_array)

@pytest.mark.asyncio
async def test_string_url_encoded(client):
    await client.paths.string_url_encoded()

@pytest.mark.asyncio
async def test_paths_unicode(client):
    await client.paths.string_unicode()

@pytest.mark.asyncio
async def test_string_url_non_encoded(client):
    await client.paths.string_url_non_encoded()

@pytest.mark.asyncio
async def test_enum_valid(client):
    await client.paths.enum_valid("green color")

@pytest.mark.asyncio
async def test_enum_null(client):
    with pytest.raises(ValidationError):
        await client.paths.enum_null(None)

@pytest.mark.asyncio
async def test_base64_url(client):
    await client.paths.base64_url("lorem".encode())

@pytest.mark.asyncio
async def test_queries_byte(client):
    await client.queries.byte_empty()
    u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
    await client.queries.byte_multi_byte(byte_query=u_bytes)
    await client.queries.byte_null()

@pytest.mark.asyncio
async def test_queries_date(client):
    await client.queries.date_null()
    await client.queries.date_valid()

@pytest.mark.asyncio
async def test_queries_date_time(client):
    await client.queries.date_time_null()
    await client.queries.date_time_valid()

@pytest.mark.asyncio
async def test_queries_double(client):
    await client.queries.double_null()
    await client.queries.double_decimal_negative()
    await client.queries.double_decimal_positive()

@pytest.mark.asyncio
async def test_queries_float_scientific(client):
    await client.queries.float_scientific_negative()
    await client.queries.float_scientific_positive()
    await client.queries.float_null()

@pytest.mark.asyncio
async def test_queries_boolean(client):
    await client.queries.get_boolean_false()
    await client.queries.get_boolean_true()
    await client.queries.get_boolean_null()

@pytest.mark.asyncio
async def test_queries_int(client):
    await client.queries.get_int_negative_one_million()
    await client.queries.get_int_one_million()
    await client.queries.get_int_null()

@pytest.mark.asyncio
async def test_queries_long(client):
    await client.queries.get_negative_ten_billion()
    await client.queries.get_ten_billion()
    await client.queries.get_long_null()

@pytest.mark.asyncio
async def test_queries_string(client):
    await client.queries.string_empty()
    await client.queries.string_null()
    await client.queries.string_url_encoded()

@pytest.mark.asyncio
async def test_queries_enum(client):
    await client.queries.enum_valid(enum_query="green color")
    await client.queries.enum_null(enum_query=None)

@pytest.mark.asyncio
async def test_queries_unicode(client):
    await client.queries.string_unicode()

@pytest.mark.asyncio
async def test_array_string_csv(client, test_array_query):
    await client.queries.array_string_csv_empty(array_query=[])
    await client.queries.array_string_csv_null(array_query=None)
    await client.queries.array_string_csv_valid(array_query=test_array_query)

@pytest.mark.asyncio
async def test_array_string_miscellaneous(client, test_array_query):
    await client.queries.array_string_pipes_valid(array_query=test_array_query)
    await client.queries.array_string_ssv_valid(array_query=test_array_query)

@pytest.mark.asyncio
@pytest.mark.skip(reason="https://github.com/aio-libs/aiohttp/issues/5904")
async def test_array_string_tsv_valid(client, test_array_query):
    await client.queries.array_string_tsv_valid(test_array_query)

@pytest.mark.asyncio
async def test_array_string_multi(multi_client, test_array_query):
    await multi_client.queries.array_string_multi_empty(array_query=[])
    await multi_client.queries.array_string_multi_null()
    await multi_client.queries.array_string_multi_valid(array_query=test_array_query)

@pytest.mark.asyncio
async def test_array_string_no_collection_format(client):
    await client.queries.array_string_no_collection_format_empty(array_query=['hello', 'nihao', 'bonjour'])

@pytest.mark.asyncio
async def test_get_all_with_values(client):
    client._config.global_string_path = "globalStringPath"
    client._config.global_string_query = "globalStringQuery"
    await client.path_items.get_all_with_values(
        "pathItemStringPath",
        "localStringPath",
        path_item_string_query="pathItemStringQuery",
        local_string_query="localStringQuery",
    )

@pytest.mark.asyncio
async def test_get_global_and_local_query_null(client):
    client._config.global_string_path = "globalStringPath"
    await client.path_items.get_global_and_local_query_null(
        "pathItemStringPath",
        "localStringPath",
        path_item_string_query="pathItemStringQuery",
        local_string_query=None,
    )

@pytest.mark.asyncio
async def test_get_global_query_null(client):
    client._config.global_string_path = "globalStringPath"
    await client.path_items.get_global_query_null(
        "pathItemStringPath",
        "localStringPath",
        path_item_string_query="pathItemStringQuery",
        local_string_query="localStringQuery",
    )

@pytest.mark.asyncio
async def test_get_local_path_item_query_null(client):
    client._config.global_string_path = "globalStringPath"
    client._config.global_string_query = "globalStringQuery"
    await client.path_items.get_local_path_item_query_null(
        "pathItemStringPath",
        "localStringPath",
        path_item_string_query=None,
        local_string_query=None,
    )
