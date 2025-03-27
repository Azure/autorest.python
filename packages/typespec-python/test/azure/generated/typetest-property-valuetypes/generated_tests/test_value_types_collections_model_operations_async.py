# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import ValueTypesPreparer
from testpreparer_async import ValueTypesClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestValueTypesCollectionsModelOperationsAsync(ValueTypesClientTestBaseAsync):
    @ValueTypesPreparer()
    @recorded_by_proxy_async
    async def test_collections_model_get(self, valuetypes_endpoint):
        client = self.create_async_client(endpoint=valuetypes_endpoint)
        response = await client.collections_model.get()

        # please add some check logic here by yourself
        # ...

    @ValueTypesPreparer()
    @recorded_by_proxy_async
    async def test_collections_model_put(self, valuetypes_endpoint):
        client = self.create_async_client(endpoint=valuetypes_endpoint)
        response = await client.collections_model.put(
            body={"property": [{"property": "str"}]},
        )

        # please add some check logic here by yourself
        # ...
