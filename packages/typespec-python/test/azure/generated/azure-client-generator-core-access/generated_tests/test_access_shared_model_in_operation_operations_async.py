# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import AccessPreparer
from testpreparer_async import AccessClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAccessSharedModelInOperationOperationsAsync(AccessClientTestBaseAsync):
    @AccessPreparer()
    @recorded_by_proxy_async
    async def test_shared_model_in_operation_public(self, access_endpoint):
        client = self.create_async_client(endpoint=access_endpoint)
        response = await client.shared_model_in_operation.public(
            name="str",
        )

        # please add some check logic here by yourself
        # ...
