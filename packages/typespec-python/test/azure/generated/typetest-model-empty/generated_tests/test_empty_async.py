# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import EmptyPreparer
from testpreparer_async import EmptyClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestEmptyAsync(EmptyClientTestBaseAsync):
    @EmptyPreparer()
    @recorded_by_proxy_async
    async def test_put_empty(self, empty_endpoint):
        client = self.create_async_client(endpoint=empty_endpoint)
        response = await client.put_empty(
            input={},
        )

        # please add some check logic here by yourself
        # ...

    @EmptyPreparer()
    @recorded_by_proxy_async
    async def test_get_empty(self, empty_endpoint):
        client = self.create_async_client(endpoint=empty_endpoint)
        response = await client.get_empty()

        # please add some check logic here by yourself
        # ...

    @EmptyPreparer()
    @recorded_by_proxy_async
    async def test_post_round_trip_empty(self, empty_endpoint):
        client = self.create_async_client(endpoint=empty_endpoint)
        response = await client.post_round_trip_empty(
            body={},
        )

        # please add some check logic here by yourself
        # ...
