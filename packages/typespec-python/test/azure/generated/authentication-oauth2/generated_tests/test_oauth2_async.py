# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import OAuth2Preparer
from testpreparer_async import OAuth2ClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestOAuth2Async(OAuth2ClientTestBaseAsync):
    @OAuth2Preparer()
    @recorded_by_proxy_async
    async def test_valid(self, oauth2_endpoint):
        client = self.create_async_client(endpoint=oauth2_endpoint)
        response = await client.valid()

        # please add some check logic here by yourself
        # ...

    @OAuth2Preparer()
    @recorded_by_proxy_async
    async def test_invalid(self, oauth2_endpoint):
        client = self.create_async_client(endpoint=oauth2_endpoint)
        response = await client.invalid()

        # please add some check logic here by yourself
        # ...
