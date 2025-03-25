# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import RoutesPreparer
from testpreparer_async import RoutesClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRoutesAsync(RoutesClientTestBaseAsync):
    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_fixed(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.fixed()

        # please add some check logic here by yourself
        # ...
