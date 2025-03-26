# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import JsonPreparer
from testpreparer_async import JsonClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestJsonPropertyOperationsAsync(JsonClientTestBaseAsync):
    @JsonPreparer()
    @recorded_by_proxy_async
    async def test_property_send(self, json_endpoint):
        client = self.create_async_client(endpoint=json_endpoint)
        response = await client.property.send(
            body={"wireName": bool},
        )

        # please add some check logic here by yourself
        # ...

    @JsonPreparer()
    @recorded_by_proxy_async
    async def test_property_get(self, json_endpoint):
        client = self.create_async_client(endpoint=json_endpoint)
        response = await client.property.get()

        # please add some check logic here by yourself
        # ...
