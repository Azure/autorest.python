# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import RenamedOperationPreparer
from testpreparer_async import RenamedOperationClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRenamedOperationGroupOperationsAsync(RenamedOperationClientTestBaseAsync):
    @RenamedOperationPreparer()
    @recorded_by_proxy_async
    async def test_group_renamed_two(self, renamedoperation_endpoint):
        client = self.create_async_client(endpoint=renamedoperation_endpoint)
        response = await client.group.renamed_two()

        # please add some check logic here by yourself
        # ...

    @RenamedOperationPreparer()
    @recorded_by_proxy_async
    async def test_group_renamed_four(self, renamedoperation_endpoint):
        client = self.create_async_client(endpoint=renamedoperation_endpoint)
        response = await client.group.renamed_four()

        # please add some check logic here by yourself
        # ...

    @RenamedOperationPreparer()
    @recorded_by_proxy_async
    async def test_group_renamed_six(self, renamedoperation_endpoint):
        client = self.create_async_client(endpoint=renamedoperation_endpoint)
        response = await client.group.renamed_six()

        # please add some check logic here by yourself
        # ...
