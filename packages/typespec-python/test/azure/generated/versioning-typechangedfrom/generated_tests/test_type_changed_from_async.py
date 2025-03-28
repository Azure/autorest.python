# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import TypeChangedFromPreparer
from testpreparer_async import TypeChangedFromClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestTypeChangedFromAsync(TypeChangedFromClientTestBaseAsync):
    @TypeChangedFromPreparer()
    @recorded_by_proxy_async
    async def test_test(self, typechangedfrom_endpoint):
        client = self.create_async_client(endpoint=typechangedfrom_endpoint)
        response = await client.test(
            body={"changedProp": "str", "prop": "str"},
            param="str",
        )

        # please add some check logic here by yourself
        # ...
