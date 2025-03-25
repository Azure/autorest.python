# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import ServicePreparer
from testpreparer_async import ServiceClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestServiceQuxOperationsAsync(ServiceClientTestBaseAsync):
    @ServicePreparer()
    @recorded_by_proxy_async
    async def test_qux_eight(self, service_endpoint):
        client = self.create_async_client(endpoint=service_endpoint)
        response = await client.qux.eight()

        # please add some check logic here by yourself
        # ...

    @ServicePreparer()
    @recorded_by_proxy_async
    async def test_qux_bar_nine(self, service_endpoint):
        client = self.create_async_client(endpoint=service_endpoint)
        response = await client.qux.bar.nine()

        # please add some check logic here by yourself
        # ...
