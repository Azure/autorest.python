# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import NamespaceFirstPreparer
from testpreparer_async import ClientNamespaceFirstClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNamespaceFirstAsync(ClientNamespaceFirstClientTestBaseAsync):
    @NamespaceFirstPreparer()
    @recorded_by_proxy_async
    async def test_get_first(self, namespacefirst_endpoint):
        client = self.create_async_client(endpoint=namespacefirst_endpoint)
        response = await client.get_first()

        # please add some check logic here by yourself
        # ...
