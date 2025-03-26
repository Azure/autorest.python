# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import NotDefinedPreparer
from testpreparer_async import NotDefinedClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNotDefinedAsync(NotDefinedClientTestBaseAsync):
    @NotDefinedPreparer()
    @recorded_by_proxy_async
    async def test_valid(self, notdefined_endpoint):
        client = self.create_async_client(endpoint=notdefined_endpoint)
        response = await client.valid()

        # please add some check logic here by yourself
        # ...
