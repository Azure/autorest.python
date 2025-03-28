# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import TwoOperationGroupPreparer
from testpreparer_async import TwoOperationGroupClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestTwoOperationGroupGroup1OperationsAsync(TwoOperationGroupClientTestBaseAsync):
    @TwoOperationGroupPreparer()
    @recorded_by_proxy_async
    async def test_group1_one(self, twooperationgroup_endpoint):
        client = self.create_async_client(endpoint=twooperationgroup_endpoint)
        response = await client.group1.one()

        # please add some check logic here by yourself
        # ...

    @TwoOperationGroupPreparer()
    @recorded_by_proxy_async
    async def test_group1_three(self, twooperationgroup_endpoint):
        client = self.create_async_client(endpoint=twooperationgroup_endpoint)
        response = await client.group1.three()

        # please add some check logic here by yourself
        # ...

    @TwoOperationGroupPreparer()
    @recorded_by_proxy_async
    async def test_group1_four(self, twooperationgroup_endpoint):
        client = self.create_async_client(endpoint=twooperationgroup_endpoint)
        response = await client.group1.four()

        # please add some check logic here by yourself
        # ...
