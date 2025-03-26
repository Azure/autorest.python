# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import NotDiscriminatedPreparer
from testpreparer_async import NotDiscriminatedClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNotDiscriminatedAsync(NotDiscriminatedClientTestBaseAsync):
    @NotDiscriminatedPreparer()
    @recorded_by_proxy_async
    async def test_post_valid(self, notdiscriminated_endpoint):
        client = self.create_async_client(endpoint=notdiscriminated_endpoint)
        response = await client.post_valid(
            input={"age": 0, "name": "str", "smart": bool},
        )

        # please add some check logic here by yourself
        # ...

    @NotDiscriminatedPreparer()
    @recorded_by_proxy_async
    async def test_get_valid(self, notdiscriminated_endpoint):
        client = self.create_async_client(endpoint=notdiscriminated_endpoint)
        response = await client.get_valid()

        # please add some check logic here by yourself
        # ...

    @NotDiscriminatedPreparer()
    @recorded_by_proxy_async
    async def test_put_valid(self, notdiscriminated_endpoint):
        client = self.create_async_client(endpoint=notdiscriminated_endpoint)
        response = await client.put_valid(
            input={"age": 0, "name": "str", "smart": bool},
        )

        # please add some check logic here by yourself
        # ...
