# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import TwoOperationGroupClientTestBase, TwoOperationGroupPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestTwoOperationGroupGroup1Operations(TwoOperationGroupClientTestBase):
    @TwoOperationGroupPreparer()
    @recorded_by_proxy
    def test_group1_one(self, twooperationgroup_endpoint):
        client = self.create_client(endpoint=twooperationgroup_endpoint)
        response = client.group1.one()

        # please add some check logic here by yourself
        # ...

    @TwoOperationGroupPreparer()
    @recorded_by_proxy
    def test_group1_three(self, twooperationgroup_endpoint):
        client = self.create_client(endpoint=twooperationgroup_endpoint)
        response = client.group1.three()

        # please add some check logic here by yourself
        # ...

    @TwoOperationGroupPreparer()
    @recorded_by_proxy
    def test_group1_four(self, twooperationgroup_endpoint):
        client = self.create_client(endpoint=twooperationgroup_endpoint)
        response = client.group1.four()

        # please add some check logic here by yourself
        # ...
