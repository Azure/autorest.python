# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import RenamedFromPreparer
from testpreparer_async import RenamedFromClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRenamedFromNewInterfaceOperationsAsync(RenamedFromClientTestBaseAsync):
    @RenamedFromPreparer()
    @recorded_by_proxy_async
    async def test_new_interface_new_op_in_new_interface(self, renamedfrom_endpoint):
        client = self.create_async_client(endpoint=renamedfrom_endpoint)
        response = await client.new_interface.new_op_in_new_interface(
            body={"enumProp": "str", "newProp": "str", "unionProp": "str"},
        )

        # please add some check logic here by yourself
        # ...
