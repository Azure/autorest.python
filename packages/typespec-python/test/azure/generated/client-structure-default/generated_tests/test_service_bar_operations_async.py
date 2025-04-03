# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import ServicePreparer
from testpreparer_async import ServiceClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestServiceBarOperationsAsync(ServiceClientTestBaseAsync):
    @ServicePreparer()
    @recorded_by_proxy_async
    async def test_bar_five(self, service_endpoint):
        client = self.create_async_client(endpoint=service_endpoint)
        response = await client.bar.five()

        # please add some check logic here by yourself
        # ...

    @ServicePreparer()
    @recorded_by_proxy_async
    async def test_bar_six(self, service_endpoint):
        client = self.create_async_client(endpoint=service_endpoint)
        response = await client.bar.six()

        # please add some check logic here by yourself
        # ...
