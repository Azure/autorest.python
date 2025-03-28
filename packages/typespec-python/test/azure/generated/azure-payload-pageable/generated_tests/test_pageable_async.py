# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import PageablePreparer
from testpreparer_async import PageableClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestPageableAsync(PageableClientTestBaseAsync):
    @PageablePreparer()
    @recorded_by_proxy_async
    async def test_list(self, pageable_endpoint):
        client = self.create_async_client(endpoint=pageable_endpoint)
        response = client.list()
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
