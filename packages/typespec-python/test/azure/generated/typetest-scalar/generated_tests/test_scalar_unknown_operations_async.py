# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import ScalarPreparer
from testpreparer_async import ScalarClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestScalarUnknownOperationsAsync(ScalarClientTestBaseAsync):
    @ScalarPreparer()
    @recorded_by_proxy_async
    async def test_unknown_get(self, scalar_endpoint):
        client = self.create_async_client(endpoint=scalar_endpoint)
        response = await client.unknown.get()

        # please add some check logic here by yourself
        # ...

    @ScalarPreparer()
    @recorded_by_proxy_async
    async def test_unknown_put(self, scalar_endpoint):
        client = self.create_async_client(endpoint=scalar_endpoint)
        response = await client.unknown.put(
            body={},
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...
