# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import MultiplePreparer
from testpreparer_async import MultipleClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestMultipleAsync(MultipleClientTestBaseAsync):
    @MultiplePreparer()
    @recorded_by_proxy_async
    async def test_no_operation_params(self, multiple_endpoint):
        client = self.create_async_client(endpoint=multiple_endpoint)
        response = await client.no_operation_params()

        # please add some check logic here by yourself
        # ...

    @MultiplePreparer()
    @recorded_by_proxy_async
    async def test_with_operation_path_param(self, multiple_endpoint):
        client = self.create_async_client(endpoint=multiple_endpoint)
        response = await client.with_operation_path_param(
            keyword="str",
        )

        # please add some check logic here by yourself
        # ...
