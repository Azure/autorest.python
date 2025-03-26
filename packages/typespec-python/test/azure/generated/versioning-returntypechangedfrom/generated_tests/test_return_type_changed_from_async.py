# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import ReturnTypeChangedFromPreparer
from testpreparer_async import ReturnTypeChangedFromClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestReturnTypeChangedFromAsync(ReturnTypeChangedFromClientTestBaseAsync):
    @ReturnTypeChangedFromPreparer()
    @recorded_by_proxy_async
    async def test_test(self, returntypechangedfrom_endpoint):
        client = self.create_async_client(endpoint=returntypechangedfrom_endpoint)
        response = await client.test(
            body="str",
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...
