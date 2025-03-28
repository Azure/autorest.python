# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import NamingPreparer
from testpreparer_async import NamingClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNamingAsync(NamingClientTestBaseAsync):
    @NamingPreparer()
    @recorded_by_proxy_async
    async def test_client_name(self, naming_endpoint):
        client = self.create_async_client(endpoint=naming_endpoint)
        response = await client.client_name()

        # please add some check logic here by yourself
        # ...

    @NamingPreparer()
    @recorded_by_proxy_async
    async def test_parameter(self, naming_endpoint):
        client = self.create_async_client(endpoint=naming_endpoint)
        response = await client.parameter(
            client_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @NamingPreparer()
    @recorded_by_proxy_async
    async def test_client(self, naming_endpoint):
        client = self.create_async_client(endpoint=naming_endpoint)
        response = await client.client(
            body={"defaultName": bool},
        )

        # please add some check logic here by yourself
        # ...

    @NamingPreparer()
    @recorded_by_proxy_async
    async def test_language(self, naming_endpoint):
        client = self.create_async_client(endpoint=naming_endpoint)
        response = await client.language(
            body={"defaultName": bool},
        )

        # please add some check logic here by yourself
        # ...

    @NamingPreparer()
    @recorded_by_proxy_async
    async def test_compatible_with_encoded_name(self, naming_endpoint):
        client = self.create_async_client(endpoint=naming_endpoint)
        response = await client.compatible_with_encoded_name(
            body={"wireName": bool},
        )

        # please add some check logic here by yourself
        # ...

    @NamingPreparer()
    @recorded_by_proxy_async
    async def test_request(self, naming_endpoint):
        client = self.create_async_client(endpoint=naming_endpoint)
        response = await client.request(
            client_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @NamingPreparer()
    @recorded_by_proxy_async
    async def test_response(self, naming_endpoint):
        client = self.create_async_client(endpoint=naming_endpoint)
        response = await client.response()

        # please add some check logic here by yourself
        # ...
