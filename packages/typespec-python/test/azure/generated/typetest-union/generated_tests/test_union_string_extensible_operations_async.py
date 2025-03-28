# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import UnionPreparer
from testpreparer_async import UnionClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestUnionStringExtensibleOperationsAsync(UnionClientTestBaseAsync):
    @UnionPreparer()
    @recorded_by_proxy_async
    async def test_string_extensible_get(self, union_endpoint):
        client = self.create_async_client(endpoint=union_endpoint)
        response = await client.string_extensible.get()

        # please add some check logic here by yourself
        # ...

    @UnionPreparer()
    @recorded_by_proxy_async
    async def test_string_extensible_send(self, union_endpoint):
        client = self.create_async_client(endpoint=union_endpoint)
        response = await client.string_extensible.send(
            body={"prop": "b"},
            prop="b",
        )

        # please add some check logic here by yourself
        # ...
