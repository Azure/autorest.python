# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import UnionPreparer
from testpreparer_async import UnionClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestUnionMixedTypesOperationsAsync(UnionClientTestBaseAsync):
    @UnionPreparer()
    @recorded_by_proxy_async
    async def test_mixed_types_get(self, union_endpoint):
        client = self.create_async_client(endpoint=union_endpoint)
        response = await client.mixed_types.get()

        # please add some check logic here by yourself
        # ...

    @UnionPreparer()
    @recorded_by_proxy_async
    async def test_mixed_types_send(self, union_endpoint):
        client = self.create_async_client(endpoint=union_endpoint)
        response = await client.mixed_types.send(
            body={
                "prop": {
                    "array": [{"name": "str"}],
                    "boolean": {"name": "str"},
                    "int": {"name": "str"},
                    "literal": {"name": "str"},
                    "model": {"name": "str"},
                }
            },
            prop={
                "array": [{"name": "str"}],
                "boolean": {"name": "str"},
                "int": {"name": "str"},
                "literal": {"name": "str"},
                "model": {"name": "str"},
            },
        )

        # please add some check logic here by yourself
        # ...
