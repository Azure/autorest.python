# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import NamingPreparer
from testpreparer_async import NamingClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNamingClientModelOperationsAsync(NamingClientTestBaseAsync):
    @NamingPreparer()
    @recorded_by_proxy_async
    async def test_client_model_client(self, naming_endpoint):
        client = self.create_async_client(endpoint=naming_endpoint)
        response = await client.client_model.client(
            body={"defaultName": bool},
        )

        # please add some check logic here by yourself
        # ...

    @NamingPreparer()
    @recorded_by_proxy_async
    async def test_client_model_language(self, naming_endpoint):
        client = self.create_async_client(endpoint=naming_endpoint)
        response = await client.client_model.language(
            body={"defaultName": bool},
        )

        # please add some check logic here by yourself
        # ...
