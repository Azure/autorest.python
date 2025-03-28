# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import FlattenPropertyPreparer
from testpreparer_async import FlattenPropertyClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestFlattenPropertyAsync(FlattenPropertyClientTestBaseAsync):
    @FlattenPropertyPreparer()
    @recorded_by_proxy_async
    async def test_put_flatten_model(self, flattenproperty_endpoint):
        client = self.create_async_client(endpoint=flattenproperty_endpoint)
        response = await client.put_flatten_model(
            input={"name": "str", "properties": {"age": 0, "description": "str"}},
        )

        # please add some check logic here by yourself
        # ...

    @FlattenPropertyPreparer()
    @recorded_by_proxy_async
    async def test_put_nested_flatten_model(self, flattenproperty_endpoint):
        client = self.create_async_client(endpoint=flattenproperty_endpoint)
        response = await client.put_nested_flatten_model(
            input={"name": "str", "properties": {"properties": {"age": 0, "description": "str"}, "summary": "str"}},
        )

        # please add some check logic here by yourself
        # ...
