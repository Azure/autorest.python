# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import NamespaceSecondPreparer
from testpreparer_async import ClientNamespaceSecondClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNamespaceSecondAsync(ClientNamespaceSecondClientTestBaseAsync):
    @NamespaceSecondPreparer()
    @recorded_by_proxy_async
    async def test_get_second(self, namespacesecond_endpoint):
        client = self.create_async_client(endpoint=namespacesecond_endpoint)
        response = await client.get_second()

        # please add some check logic here by yourself
        # ...
