# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import MadeOptionalPreparer
from testpreparer_async import MadeOptionalClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestMadeOptionalAsync(MadeOptionalClientTestBaseAsync):
    @MadeOptionalPreparer()
    @recorded_by_proxy_async
    async def test_test(self, madeoptional_endpoint):
        client = self.create_async_client(endpoint=madeoptional_endpoint)
        response = await client.test(
            body={"prop": "str", "changedProp": "str"},
        )

        # please add some check logic here by yourself
        # ...
