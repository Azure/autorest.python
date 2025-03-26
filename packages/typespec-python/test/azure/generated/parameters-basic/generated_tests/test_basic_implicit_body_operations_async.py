# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import BasicPreparer
from testpreparer_async import BasicClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestBasicImplicitBodyOperationsAsync(BasicClientTestBaseAsync):
    @BasicPreparer()
    @recorded_by_proxy_async
    async def test_implicit_body_simple(self, basic_endpoint):
        client = self.create_async_client(endpoint=basic_endpoint)
        response = await client.implicit_body.simple(
            body={"name": "str"},
            name="str",
        )

        # please add some check logic here by yourself
        # ...
