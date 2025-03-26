# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import ScalarPreparer
from testpreparer_async import ScalarClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestScalarAzureLocationScalarOperationsAsync(ScalarClientTestBaseAsync):
    @ScalarPreparer()
    @recorded_by_proxy_async
    async def test_azure_location_scalar_get(self, scalar_endpoint):
        client = self.create_async_client(endpoint=scalar_endpoint)
        response = await client.azure_location_scalar.get()

        # please add some check logic here by yourself
        # ...

    @ScalarPreparer()
    @recorded_by_proxy_async
    async def test_azure_location_scalar_put(self, scalar_endpoint):
        client = self.create_async_client(endpoint=scalar_endpoint)
        response = await client.azure_location_scalar.put(
            body="str",
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...

    @ScalarPreparer()
    @recorded_by_proxy_async
    async def test_azure_location_scalar_post(self, scalar_endpoint):
        client = self.create_async_client(endpoint=scalar_endpoint)
        response = await client.azure_location_scalar.post(
            body={"location": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @ScalarPreparer()
    @recorded_by_proxy_async
    async def test_azure_location_scalar_header(self, scalar_endpoint):
        client = self.create_async_client(endpoint=scalar_endpoint)
        response = await client.azure_location_scalar.header(
            region="str",
        )

        # please add some check logic here by yourself
        # ...

    @ScalarPreparer()
    @recorded_by_proxy_async
    async def test_azure_location_scalar_query(self, scalar_endpoint):
        client = self.create_async_client(endpoint=scalar_endpoint)
        response = await client.azure_location_scalar.query(
            region="str",
        )

        # please add some check logic here by yourself
        # ...
