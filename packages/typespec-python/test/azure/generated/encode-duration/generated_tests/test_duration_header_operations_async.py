# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import DurationPreparer
from testpreparer_async import DurationClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDurationHeaderOperationsAsync(DurationClientTestBaseAsync):
    @DurationPreparer()
    @recorded_by_proxy_async
    async def test_header_default(self, duration_endpoint):
        client = self.create_async_client(endpoint=duration_endpoint)
        response = await client.header.default(
            duration="1 day, 0:00:00",
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy_async
    async def test_header_iso8601(self, duration_endpoint):
        client = self.create_async_client(endpoint=duration_endpoint)
        response = await client.header.iso8601(
            duration="1 day, 0:00:00",
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy_async
    async def test_header_iso8601_array(self, duration_endpoint):
        client = self.create_async_client(endpoint=duration_endpoint)
        response = await client.header.iso8601_array(
            duration=["1 day, 0:00:00"],
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy_async
    async def test_header_int32_seconds(self, duration_endpoint):
        client = self.create_async_client(endpoint=duration_endpoint)
        response = await client.header.int32_seconds(
            duration=0,
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy_async
    async def test_header_float_seconds(self, duration_endpoint):
        client = self.create_async_client(endpoint=duration_endpoint)
        response = await client.header.float_seconds(
            duration=0.0,
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy_async
    async def test_header_float64_seconds(self, duration_endpoint):
        client = self.create_async_client(endpoint=duration_endpoint)
        response = await client.header.float64_seconds(
            duration=0.0,
        )

        # please add some check logic here by yourself
        # ...
