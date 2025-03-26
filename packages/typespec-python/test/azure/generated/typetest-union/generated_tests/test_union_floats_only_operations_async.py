# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import UnionPreparer
from testpreparer_async import UnionClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestUnionFloatsOnlyOperationsAsync(UnionClientTestBaseAsync):
    @UnionPreparer()
    @recorded_by_proxy_async
    async def test_floats_only_get(self, union_endpoint):
        client = self.create_async_client(endpoint=union_endpoint)
        response = await client.floats_only.get()

        # please add some check logic here by yourself
        # ...

    @UnionPreparer()
    @recorded_by_proxy_async
    async def test_floats_only_send(self, union_endpoint):
        client = self.create_async_client(endpoint=union_endpoint)
        response = await client.floats_only.send(
            body={"prop": 1.1},
            prop=1.1,
        )

        # please add some check logic here by yourself
        # ...
