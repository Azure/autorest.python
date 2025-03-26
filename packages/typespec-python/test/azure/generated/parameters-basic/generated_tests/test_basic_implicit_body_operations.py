# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import BasicClientTestBase, BasicPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestBasicImplicitBodyOperations(BasicClientTestBase):
    @BasicPreparer()
    @recorded_by_proxy
    def test_implicit_body_simple(self, basic_endpoint):
        client = self.create_client(endpoint=basic_endpoint)
        response = client.implicit_body.simple(
            body={"name": "str"},
            name="str",
        )

        # please add some check logic here by yourself
        # ...
