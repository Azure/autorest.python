# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import DurationPreparer
from testpreparer_async import DurationClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDurationAsync(DurationClientTestBaseAsync):
    @DurationPreparer()
    @recorded_by_proxy_async
    async def test_duration_constant(self, duration_endpoint):
        client = self.create_async_client(endpoint=duration_endpoint)
        response = await client.duration_constant(
            body={"input": "1 day, 0:00:00"},
        )

        # please add some check logic here by yourself
        # ...
