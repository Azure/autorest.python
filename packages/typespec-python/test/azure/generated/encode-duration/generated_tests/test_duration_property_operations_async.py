# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import DurationPreparer
from testpreparer_async import DurationClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDurationPropertyOperationsAsync(DurationClientTestBaseAsync):
    @DurationPreparer()
    @recorded_by_proxy_async
    async def test_property_default(self, duration_endpoint):
        client = self.create_async_client(endpoint=duration_endpoint)
        response = await client.property.default(
            body={"value": "1 day, 0:00:00"},
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy_async
    async def test_property_iso8601(self, duration_endpoint):
        client = self.create_async_client(endpoint=duration_endpoint)
        response = await client.property.iso8601(
            body={"value": "1 day, 0:00:00"},
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy_async
    async def test_property_int32_seconds(self, duration_endpoint):
        client = self.create_async_client(endpoint=duration_endpoint)
        response = await client.property.int32_seconds(
            body={"value": 0},
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy_async
    async def test_property_float_seconds(self, duration_endpoint):
        client = self.create_async_client(endpoint=duration_endpoint)
        response = await client.property.float_seconds(
            body={"value": 0.0},
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy_async
    async def test_property_float64_seconds(self, duration_endpoint):
        client = self.create_async_client(endpoint=duration_endpoint)
        response = await client.property.float64_seconds(
            body={"value": 0.0},
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy_async
    async def test_property_float_seconds_array(self, duration_endpoint):
        client = self.create_async_client(endpoint=duration_endpoint)
        response = await client.property.float_seconds_array(
            body={"value": [0.0]},
        )

        # please add some check logic here by yourself
        # ...
