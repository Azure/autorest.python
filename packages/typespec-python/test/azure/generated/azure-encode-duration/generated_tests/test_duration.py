# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import DurationClientTestBase, DurationPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDuration(DurationClientTestBase):
    @DurationPreparer()
    @recorded_by_proxy
    def test_duration_constant(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.duration_constant(
            body={"input": "1 day, 0:00:00"},
        )

        # please add some check logic here by yourself
        # ...
