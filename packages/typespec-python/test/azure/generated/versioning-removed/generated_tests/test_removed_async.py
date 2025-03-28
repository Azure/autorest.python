# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import RemovedPreparer
from testpreparer_async import RemovedClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRemovedAsync(RemovedClientTestBaseAsync):
    @RemovedPreparer()
    @recorded_by_proxy_async
    async def test_v2(self, removed_endpoint):
        client = self.create_async_client(endpoint=removed_endpoint)
        response = await client.v2(
            body={"enumProp": "str", "prop": "str", "unionProp": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @RemovedPreparer()
    @recorded_by_proxy_async
    async def test_model_v3(self, removed_endpoint):
        client = self.create_async_client(endpoint=removed_endpoint)
        response = await client.model_v3(
            body={"enumProp": "str", "id": "str"},
        )

        # please add some check logic here by yourself
        # ...
