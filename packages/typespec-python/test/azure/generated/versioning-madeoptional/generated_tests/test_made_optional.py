# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import MadeOptionalClientTestBase, MadeOptionalPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestMadeOptional(MadeOptionalClientTestBase):
    @MadeOptionalPreparer()
    @recorded_by_proxy
    def test_test(self, madeoptional_endpoint):
        client = self.create_client(endpoint=madeoptional_endpoint)
        response = client.test(
            body={"prop": "str", "changedProp": "str"},
        )

        # please add some check logic here by yourself
        # ...
