# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import FixedPreparer
from testpreparer_async import FixedClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestFixedStringOperationsAsync(FixedClientTestBaseAsync):
    @FixedPreparer()
    @recorded_by_proxy_async
    async def test_string_get_known_value(self, fixed_endpoint):
        client = self.create_async_client(endpoint=fixed_endpoint)
        response = await client.string.get_known_value()

        # please add some check logic here by yourself
        # ...

    @FixedPreparer()
    @recorded_by_proxy_async
    async def test_string_put_known_value(self, fixed_endpoint):
        client = self.create_async_client(endpoint=fixed_endpoint)
        response = await client.string.put_known_value(
            body="str",
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...

    @FixedPreparer()
    @recorded_by_proxy_async
    async def test_string_put_unknown_value(self, fixed_endpoint):
        client = self.create_async_client(endpoint=fixed_endpoint)
        response = await client.string.put_unknown_value(
            body="str",
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...
