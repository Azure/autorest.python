# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import AdditionalPropertiesPreparer
from testpreparer_async import AdditionalPropertiesClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAdditionalPropertiesIsUnknownOperationsAsync(AdditionalPropertiesClientTestBaseAsync):
    @AdditionalPropertiesPreparer()
    @recorded_by_proxy_async
    async def test_is_unknown_get(self, additionalproperties_endpoint):
        client = self.create_async_client(endpoint=additionalproperties_endpoint)
        response = await client.is_unknown.get()

        # please add some check logic here by yourself
        # ...

    @AdditionalPropertiesPreparer()
    @recorded_by_proxy_async
    async def test_is_unknown_put(self, additionalproperties_endpoint):
        client = self.create_async_client(endpoint=additionalproperties_endpoint)
        response = await client.is_unknown.put(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...
