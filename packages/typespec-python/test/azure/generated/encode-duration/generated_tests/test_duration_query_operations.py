# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import DurationClientTestBase, DurationPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDurationQueryOperations(DurationClientTestBase):
    @DurationPreparer()
    @recorded_by_proxy
    def test_query_default(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.query.default(
            input="1 day, 0:00:00",
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy
    def test_query_iso8601(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.query.iso8601(
            input="1 day, 0:00:00",
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy
    def test_query_int32_seconds(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.query.int32_seconds(
            input=0,
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy
    def test_query_float_seconds(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.query.float_seconds(
            input=0.0,
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy
    def test_query_float64_seconds(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.query.float64_seconds(
            input=0.0,
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy
    def test_query_int32_seconds_array(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.query.int32_seconds_array(
            input=[0],
        )

        # please add some check logic here by yourself
        # ...
