# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import RenamedFromPreparer
from testpreparer_async import RenamedFromClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRenamedFromAsync(RenamedFromClientTestBaseAsync):
    @RenamedFromPreparer()
    @recorded_by_proxy_async
    async def test_new_op(self, renamedfrom_endpoint):
        client = self.create_async_client(endpoint=renamedfrom_endpoint)
        response = await client.new_op(
            body={"enumProp": "str", "newProp": "str", "unionProp": "str"},
            new_query="str",
        )

        # please add some check logic here by yourself
        # ...
