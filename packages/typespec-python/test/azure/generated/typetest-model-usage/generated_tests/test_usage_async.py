# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import UsagePreparer
from testpreparer_async import UsageClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestUsageAsync(UsageClientTestBaseAsync):
    @UsagePreparer()
    @recorded_by_proxy_async
    async def test_input(self, usage_endpoint):
        client = self.create_async_client(endpoint=usage_endpoint)
        response = await client.input(
            input={"requiredProp": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @UsagePreparer()
    @recorded_by_proxy_async
    async def test_output(self, usage_endpoint):
        client = self.create_async_client(endpoint=usage_endpoint)
        response = await client.output()

        # please add some check logic here by yourself
        # ...

    @UsagePreparer()
    @recorded_by_proxy_async
    async def test_input_and_output(self, usage_endpoint):
        client = self.create_async_client(endpoint=usage_endpoint)
        response = await client.input_and_output(
            body={"requiredProp": "str"},
        )

        # please add some check logic here by yourself
        # ...
