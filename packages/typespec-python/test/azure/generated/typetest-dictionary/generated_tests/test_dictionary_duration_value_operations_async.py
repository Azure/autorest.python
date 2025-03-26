# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import DictionaryPreparer
from testpreparer_async import DictionaryClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDictionaryDurationValueOperationsAsync(DictionaryClientTestBaseAsync):
    @DictionaryPreparer()
    @recorded_by_proxy_async
    async def test_duration_value_get(self, dictionary_endpoint):
        client = self.create_async_client(endpoint=dictionary_endpoint)
        response = await client.duration_value.get()

        # please add some check logic here by yourself
        # ...

    @DictionaryPreparer()
    @recorded_by_proxy_async
    async def test_duration_value_put(self, dictionary_endpoint):
        client = self.create_async_client(endpoint=dictionary_endpoint)
        response = await client.duration_value.put(
            body={"str": "1 day, 0:00:00"},
        )

        # please add some check logic here by yourself
        # ...
