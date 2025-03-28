# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import ResiliencyServiceDrivenPreparer
from testpreparer_async import ResiliencyServiceDrivenClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestResiliencyServiceDrivenAsync(ResiliencyServiceDrivenClientTestBaseAsync):
    @ResiliencyServiceDrivenPreparer()
    @recorded_by_proxy_async
    async def test_from_none(self, resiliencyservicedriven_endpoint):
        client = self.create_async_client(endpoint=resiliencyservicedriven_endpoint)
        response = await client.from_none()

        # please add some check logic here by yourself
        # ...

    @ResiliencyServiceDrivenPreparer()
    @recorded_by_proxy_async
    async def test_from_one_required(self, resiliencyservicedriven_endpoint):
        client = self.create_async_client(endpoint=resiliencyservicedriven_endpoint)
        response = await client.from_one_required(
            parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @ResiliencyServiceDrivenPreparer()
    @recorded_by_proxy_async
    async def test_from_one_optional(self, resiliencyservicedriven_endpoint):
        client = self.create_async_client(endpoint=resiliencyservicedriven_endpoint)
        response = await client.from_one_optional()

        # please add some check logic here by yourself
        # ...
