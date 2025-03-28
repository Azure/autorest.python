# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import DurationClientTestBase, DurationPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDurationPropertyOperations(DurationClientTestBase):
    @DurationPreparer()
    @recorded_by_proxy
    def test_property_default(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.property.default(
            body={"value": "1 day, 0:00:00"},
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy
    def test_property_iso8601(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.property.iso8601(
            body={"value": "1 day, 0:00:00"},
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy
    def test_property_int32_seconds(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.property.int32_seconds(
            body={"value": 0},
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy
    def test_property_float_seconds(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.property.float_seconds(
            body={"value": 0.0},
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy
    def test_property_float64_seconds(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.property.float64_seconds(
            body={"value": 0.0},
        )

        # please add some check logic here by yourself
        # ...

    @DurationPreparer()
    @recorded_by_proxy
    def test_property_float_seconds_array(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.property.float_seconds_array(
            body={"value": [0.0]},
        )

        # please add some check logic here by yourself
        # ...
