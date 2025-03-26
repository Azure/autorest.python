# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import SinglePreparer
from testpreparer_async import SingleClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSingleAsync(SingleClientTestBaseAsync):
    @SinglePreparer()
    @recorded_by_proxy_async
    async def test_my_op(self, single_endpoint):
        client = self.create_async_client(endpoint=single_endpoint)
        response = await client.my_op()

        # please add some check logic here by yourself
        # ...
