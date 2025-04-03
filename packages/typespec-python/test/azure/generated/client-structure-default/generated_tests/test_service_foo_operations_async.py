# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import ServicePreparer
from testpreparer_async import ServiceClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestServiceFooOperationsAsync(ServiceClientTestBaseAsync):
    @ServicePreparer()
    @recorded_by_proxy_async
    async def test_foo_three(self, service_endpoint):
        client = self.create_async_client(endpoint=service_endpoint)
        response = await client.foo.three()

        # please add some check logic here by yourself
        # ...

    @ServicePreparer()
    @recorded_by_proxy_async
    async def test_foo_four(self, service_endpoint):
        client = self.create_async_client(endpoint=service_endpoint)
        response = await client.foo.four()

        # please add some check logic here by yourself
        # ...
