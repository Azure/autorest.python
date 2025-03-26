# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import CustomPreparer
from testpreparer_async import CustomClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestCustomAsync(CustomClientTestBaseAsync):
    @CustomPreparer()
    @recorded_by_proxy_async
    async def test_valid(self, custom_endpoint):
        client = self.create_async_client(endpoint=custom_endpoint)
        response = await client.valid()

        # please add some check logic here by yourself
        # ...

    @CustomPreparer()
    @recorded_by_proxy_async
    async def test_invalid(self, custom_endpoint):
        client = self.create_async_client(endpoint=custom_endpoint)
        response = await client.invalid()

        # please add some check logic here by yourself
        # ...
