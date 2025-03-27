# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import NumericPreparer
from testpreparer_async import NumericClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNumericPropertyOperationsAsync(NumericClientTestBaseAsync):
    @NumericPreparer()
    @recorded_by_proxy_async
    async def test_property_safeint_as_string(self, numeric_endpoint):
        client = self.create_async_client(endpoint=numeric_endpoint)
        response = await client.property.safeint_as_string(
            value={"value": 0},
        )

        # please add some check logic here by yourself
        # ...

    @NumericPreparer()
    @recorded_by_proxy_async
    async def test_property_uint32_as_string_optional(self, numeric_endpoint):
        client = self.create_async_client(endpoint=numeric_endpoint)
        response = await client.property.uint32_as_string_optional(
            value={"value": 0},
        )

        # please add some check logic here by yourself
        # ...

    @NumericPreparer()
    @recorded_by_proxy_async
    async def test_property_uint8_as_string(self, numeric_endpoint):
        client = self.create_async_client(endpoint=numeric_endpoint)
        response = await client.property.uint8_as_string(
            value={"value": 0},
        )

        # please add some check logic here by yourself
        # ...
