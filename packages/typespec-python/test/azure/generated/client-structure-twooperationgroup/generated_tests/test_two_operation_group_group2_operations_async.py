# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import TwoOperationGroupPreparer
from testpreparer_async import TwoOperationGroupClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestTwoOperationGroupGroup2OperationsAsync(TwoOperationGroupClientTestBaseAsync):
    @TwoOperationGroupPreparer()
    @recorded_by_proxy_async
    async def test_group2_two(self, twooperationgroup_endpoint):
        client = self.create_async_client(endpoint=twooperationgroup_endpoint)
        response = await client.group2.two()

        # please add some check logic here by yourself
        # ...

    @TwoOperationGroupPreparer()
    @recorded_by_proxy_async
    async def test_group2_five(self, twooperationgroup_endpoint):
        client = self.create_async_client(endpoint=twooperationgroup_endpoint)
        response = await client.group2.five()

        # please add some check logic here by yourself
        # ...

    @TwoOperationGroupPreparer()
    @recorded_by_proxy_async
    async def test_group2_six(self, twooperationgroup_endpoint):
        client = self.create_async_client(endpoint=twooperationgroup_endpoint)
        response = await client.group2.six()

        # please add some check logic here by yourself
        # ...
