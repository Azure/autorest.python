# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import TwoOperationGroupClientTestBase, TwoOperationGroupPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestTwoOperationGroupGroup2Operations(TwoOperationGroupClientTestBase):
    @TwoOperationGroupPreparer()
    @recorded_by_proxy
    def test_group2_two(self, twooperationgroup_endpoint):
        client = self.create_client(endpoint=twooperationgroup_endpoint)
        response = client.group2.two()

        # please add some check logic here by yourself
        # ...

    @TwoOperationGroupPreparer()
    @recorded_by_proxy
    def test_group2_five(self, twooperationgroup_endpoint):
        client = self.create_client(endpoint=twooperationgroup_endpoint)
        response = client.group2.five()

        # please add some check logic here by yourself
        # ...

    @TwoOperationGroupPreparer()
    @recorded_by_proxy
    def test_group2_six(self, twooperationgroup_endpoint):
        client = self.create_client(endpoint=twooperationgroup_endpoint)
        response = client.group2.six()

        # please add some check logic here by yourself
        # ...
