# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import RenamedFromClientTestBase, RenamedFromPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRenamedFrom(RenamedFromClientTestBase):
    @RenamedFromPreparer()
    @recorded_by_proxy
    def test_new_op(self, renamedfrom_endpoint):
        client = self.create_client(endpoint=renamedfrom_endpoint)
        response = client.new_op(
            body={"enumProp": "str", "newProp": "str", "unionProp": "str"},
            new_query="str",
        )

        # please add some check logic here by yourself
        # ...
