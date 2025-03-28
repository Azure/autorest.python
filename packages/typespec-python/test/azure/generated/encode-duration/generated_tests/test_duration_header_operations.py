# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import DurationClientTestBase, DurationPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDurationHeaderOperations(DurationClientTestBase):
    @DurationPreparer()
    @recorded_by_proxy
    def test_header_default(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.header.default(
            duration="1 day, 0:00:00",
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy
    def test_header_iso8601(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.header.iso8601(
            duration="1 day, 0:00:00",
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy
    def test_header_iso8601_array(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.header.iso8601_array(
            duration=["1 day, 0:00:00"],
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy
    def test_header_int32_seconds(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.header.int32_seconds(
            duration=0,
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy
    def test_header_float_seconds(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.header.float_seconds(
            duration=0.0,
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy
    def test_header_float64_seconds(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.header.float64_seconds(
            duration=0.0,
        )

        # please add some check logic here by yourself
        # ...
