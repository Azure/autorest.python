# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import DictionaryPreparer
from testpreparer_async import DictionaryClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDictionaryNullableFloatValueOperationsAsync(DictionaryClientTestBaseAsync):
    @DictionaryPreparer()
    @recorded_by_proxy_async
    async def test_nullable_float_value_get(self, dictionary_endpoint):
        client = self.create_async_client(endpoint=dictionary_endpoint)
        response = await client.nullable_float_value.get()

        # please add some check logic here by yourself
        # ...

    @DictionaryPreparer()
    @recorded_by_proxy_async
    async def test_nullable_float_value_put(self, dictionary_endpoint):
        client = self.create_async_client(endpoint=dictionary_endpoint)
        response = await client.nullable_float_value.put(
            body={"str": 0.0},
        )

        # please add some check logic here by yourself
        # ...
