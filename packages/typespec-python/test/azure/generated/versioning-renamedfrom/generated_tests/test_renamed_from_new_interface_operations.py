# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import RenamedFromClientTestBase, RenamedFromPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRenamedFromNewInterfaceOperations(RenamedFromClientTestBase):
    @RenamedFromPreparer()
    @recorded_by_proxy
    def test_new_interface_new_op_in_new_interface(self, renamedfrom_endpoint):
        client = self.create_client(endpoint=renamedfrom_endpoint)
        response = client.new_interface.new_op_in_new_interface(
            body={"enumProp": "str", "newProp": "str", "unionProp": "str"},
        )

        # please add some check logic here by yourself
        # ...
