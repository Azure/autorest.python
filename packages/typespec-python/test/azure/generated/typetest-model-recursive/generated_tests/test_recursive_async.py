# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import RecursivePreparer
from testpreparer_async import RecursiveClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRecursiveAsync(RecursiveClientTestBaseAsync):
    @RecursivePreparer()
    @recorded_by_proxy_async
    async def test_put(self, recursive_endpoint):
        client = self.create_async_client(endpoint=recursive_endpoint)
        response = await client.put(
            input={"level": 0, "extension": [...]},
        )

        # please add some check logic here by yourself
        # ...

    @RecursivePreparer()
    @recorded_by_proxy_async
    async def test_get(self, recursive_endpoint):
        client = self.create_async_client(endpoint=recursive_endpoint)
        response = await client.get()

        # please add some check logic here by yourself
        # ...
