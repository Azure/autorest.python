# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import ValueTypesPreparer
from testpreparer_async import ValueTypesClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestValueTypesDatetimeOperationsAsync(ValueTypesClientTestBaseAsync):
    @ValueTypesPreparer()
    @recorded_by_proxy_async
    async def test_datetime_get(self, valuetypes_endpoint):
        client = self.create_async_client(endpoint=valuetypes_endpoint)
        response = await client.datetime.get()

        # please add some check logic here by yourself
        # ...

    @ValueTypesPreparer()
    @recorded_by_proxy_async
    async def test_datetime_put(self, valuetypes_endpoint):
        client = self.create_async_client(endpoint=valuetypes_endpoint)
        response = await client.datetime.put(
            body={"property": "2020-02-20 00:00:00"},
        )

        # please add some check logic here by yourself
        # ...
