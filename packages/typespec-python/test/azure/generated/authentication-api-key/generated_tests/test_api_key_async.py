# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import ApiKeyPreparer
from testpreparer_async import ApiKeyClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestApiKeyAsync(ApiKeyClientTestBaseAsync):
    @ApiKeyPreparer()
    @recorded_by_proxy_async
    async def test_valid(self, apikey_endpoint):
        client = self.create_async_client(endpoint=apikey_endpoint)
        response = await client.valid()

        # please add some check logic here by yourself
        # ...

    @ApiKeyPreparer()
    @recorded_by_proxy_async
    async def test_invalid(self, apikey_endpoint):
        client = self.create_async_client(endpoint=apikey_endpoint)
        response = await client.invalid()

        # please add some check logic here by yourself
        # ...
