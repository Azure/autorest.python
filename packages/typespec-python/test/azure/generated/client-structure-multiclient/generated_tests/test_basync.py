# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import BPreparer
from testpreparer_async import ClientBClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestBAsync(ClientBClientTestBaseAsync):
    @BPreparer()
    @recorded_by_proxy_async
    async def test_renamed_two(self, b_endpoint):
        client = self.create_async_client(endpoint=b_endpoint)
        response = await client.renamed_two()

        # please add some check logic here by yourself
        # ...

    @BPreparer()
    @recorded_by_proxy_async
    async def test_renamed_four(self, b_endpoint):
        client = self.create_async_client(endpoint=b_endpoint)
        response = await client.renamed_four()

        # please add some check logic here by yourself
        # ...

    @BPreparer()
    @recorded_by_proxy_async
    async def test_renamed_six(self, b_endpoint):
        client = self.create_async_client(endpoint=b_endpoint)
        response = await client.renamed_six()

        # please add some check logic here by yourself
        # ...
