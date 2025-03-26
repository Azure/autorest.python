# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import RepeatabilityClientTestBase, RepeatabilityPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRepeatability(RepeatabilityClientTestBase):
    @RepeatabilityPreparer()
    @recorded_by_proxy
    def test_immediate_success(self, repeatability_endpoint):
        client = self.create_client(endpoint=repeatability_endpoint)
        response = client.immediate_success()

        # please add some check logic here by yourself
        # ...
