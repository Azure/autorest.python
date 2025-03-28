# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import DictionaryPreparer
from testpreparer_async import DictionaryClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDictionaryStringValueOperationsAsync(DictionaryClientTestBaseAsync):
    @DictionaryPreparer()
    @recorded_by_proxy_async
    async def test_string_value_get(self, dictionary_endpoint):
        client = self.create_async_client(endpoint=dictionary_endpoint)
        response = await client.string_value.get()

        # please add some check logic here by yourself
        # ...

    @DictionaryPreparer()
    @recorded_by_proxy_async
    async def test_string_value_put(self, dictionary_endpoint):
        client = self.create_async_client(endpoint=dictionary_endpoint)
        response = await client.string_value.put(
            body={"str": "str"},
        )

        # please add some check logic here by yourself
        # ...
