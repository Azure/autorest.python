# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import UnionPreparer
from testpreparer_async import UnionClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestUnionMixedLiteralsOperationsAsync(UnionClientTestBaseAsync):
    @UnionPreparer()
    @recorded_by_proxy_async
    async def test_mixed_literals_get(self, union_endpoint):
        client = self.create_async_client(endpoint=union_endpoint)
        response = await client.mixed_literals.get()

        # please add some check logic here by yourself
        # ...

    @UnionPreparer()
    @recorded_by_proxy_async
    async def test_mixed_literals_send(self, union_endpoint):
        client = self.create_async_client(endpoint=union_endpoint)
        response = await client.mixed_literals.send(
            body={"prop": {"booleanLiteral": "a", "floatLiteral": "a", "intLiteral": "a", "stringLiteral": "a"}},
            prop={"booleanLiteral": "a", "floatLiteral": "a", "intLiteral": "a", "stringLiteral": "a"},
        )

        # please add some check logic here by yourself
        # ...
