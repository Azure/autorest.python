# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import APreparer
from testpreparer_async import ClientAClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAAsync(ClientAClientTestBaseAsync):
    @APreparer()
    @recorded_by_proxy_async
    async def test_renamed_one(self, a_endpoint):
        client = self.create_async_client(endpoint=a_endpoint)
        response = await client.renamed_one()

        # please add some check logic here by yourself
        # ...

    @APreparer()
    @recorded_by_proxy_async
    async def test_renamed_three(self, a_endpoint):
        client = self.create_async_client(endpoint=a_endpoint)
        response = await client.renamed_three()

        # please add some check logic here by yourself
        # ...

    @APreparer()
    @recorded_by_proxy_async
    async def test_renamed_five(self, a_endpoint):
        client = self.create_async_client(endpoint=a_endpoint)
        response = await client.renamed_five()

        # please add some check logic here by yourself
        # ...
