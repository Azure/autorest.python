# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import ScalarPreparer
from testpreparer_async import ScalarClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestScalarDecimalTypeOperationsAsync(ScalarClientTestBaseAsync):
    @ScalarPreparer()
    @recorded_by_proxy_async
    async def test_decimal_type_response_body(self, scalar_endpoint):
        client = self.create_async_client(endpoint=scalar_endpoint)
        response = await client.decimal_type.response_body()

        # please add some check logic here by yourself
        # ...

    @ScalarPreparer()
    @recorded_by_proxy_async
    async def test_decimal_type_request_body(self, scalar_endpoint):
        client = self.create_async_client(endpoint=scalar_endpoint)
        response = await client.decimal_type.request_body(
            body=0.0,
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...

    @ScalarPreparer()
    @recorded_by_proxy_async
    async def test_decimal_type_request_parameter(self, scalar_endpoint):
        client = self.create_async_client(endpoint=scalar_endpoint)
        response = await client.decimal_type.request_parameter(
            value=0.0,
        )

        # please add some check logic here by yourself
        # ...
