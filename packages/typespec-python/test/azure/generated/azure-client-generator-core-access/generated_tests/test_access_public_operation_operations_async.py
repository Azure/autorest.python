# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import AccessPreparer
from testpreparer_async import AccessClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAccessPublicOperationOperationsAsync(AccessClientTestBaseAsync):
    @AccessPreparer()
    @recorded_by_proxy_async
    async def test_public_operation_no_decorator_in_public(self, access_endpoint):
        client = self.create_async_client(endpoint=access_endpoint)
        response = await client.public_operation.no_decorator_in_public(
            name="str",
        )

        # please add some check logic here by yourself
        # ...

    @AccessPreparer()
    @recorded_by_proxy_async
    async def test_public_operation_public_decorator_in_public(self, access_endpoint):
        client = self.create_async_client(endpoint=access_endpoint)
        response = await client.public_operation.public_decorator_in_public(
            name="str",
        )

        # please add some check logic here by yourself
        # ...
