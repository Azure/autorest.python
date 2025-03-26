# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import AdditionalPropertiesPreparer
from testpreparer_async import AdditionalPropertiesClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAdditionalPropertiesSpreadRecordNonDiscriminatedUnion3OperationsAsync(
    AdditionalPropertiesClientTestBaseAsync
):
    @AdditionalPropertiesPreparer()
    @recorded_by_proxy_async
    async def test_spread_record_non_discriminated_union3_get(self, additionalproperties_endpoint):
        client = self.create_async_client(endpoint=additionalproperties_endpoint)
        response = await client.spread_record_non_discriminated_union3.get()

        # please add some check logic here by yourself
        # ...

    @AdditionalPropertiesPreparer()
    @recorded_by_proxy_async
    async def test_spread_record_non_discriminated_union3_put(self, additionalproperties_endpoint):
        client = self.create_async_client(endpoint=additionalproperties_endpoint)
        response = await client.spread_record_non_discriminated_union3.put(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...
