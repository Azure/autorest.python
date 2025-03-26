# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import RepeatabilityPreparer
from testpreparer_async import RepeatabilityClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRepeatabilityAsync(RepeatabilityClientTestBaseAsync):
    @RepeatabilityPreparer()
    @recorded_by_proxy_async
    async def test_immediate_success(self, repeatability_endpoint):
        client = self.create_async_client(endpoint=repeatability_endpoint)
        response = await client.immediate_success()

        # please add some check logic here by yourself
        # ...
