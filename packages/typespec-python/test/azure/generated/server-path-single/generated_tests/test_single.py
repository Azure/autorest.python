# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import SingleClientTestBase, SinglePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSingle(SingleClientTestBase):
    @SinglePreparer()
    @recorded_by_proxy
    def test_my_op(self, single_endpoint):
        client = self.create_client(endpoint=single_endpoint)
        response = client.my_op()

        # please add some check logic here by yourself
        # ...
