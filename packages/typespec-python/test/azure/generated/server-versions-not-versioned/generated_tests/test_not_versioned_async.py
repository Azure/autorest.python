# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import NotVersionedPreparer
from testpreparer_async import NotVersionedClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNotVersionedAsync(NotVersionedClientTestBaseAsync):
    @NotVersionedPreparer()
    @recorded_by_proxy_async
    async def test_without_api_version(self, notversioned_endpoint):
        client = self.create_async_client(endpoint=notversioned_endpoint)
        response = await client.without_api_version()

        # please add some check logic here by yourself
        # ...

    @NotVersionedPreparer()
    @recorded_by_proxy_async
    async def test_with_query_api_version(self, notversioned_endpoint):
        client = self.create_async_client(endpoint=notversioned_endpoint)
        response = await client.with_query_api_version(
            api_version="str",
        )

        # please add some check logic here by yourself
        # ...

    @NotVersionedPreparer()
    @recorded_by_proxy_async
    async def test_with_path_api_version(self, notversioned_endpoint):
        client = self.create_async_client(endpoint=notversioned_endpoint)
        response = await client.with_path_api_version(
            api_version="str",
        )

        # please add some check logic here by yourself
        # ...
