# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import AdditionalPropertiesPreparer
from testpreparer_async import AdditionalPropertiesClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAdditionalPropertiesIsModelOperationsAsync(AdditionalPropertiesClientTestBaseAsync):
    @AdditionalPropertiesPreparer()
    @recorded_by_proxy_async
    async def test_is_model_get(self, additionalproperties_endpoint):
        client = self.create_async_client(endpoint=additionalproperties_endpoint)
        response = await client.is_model.get()

        # please add some check logic here by yourself
        # ...

    @AdditionalPropertiesPreparer()
    @recorded_by_proxy_async
    async def test_is_model_put(self, additionalproperties_endpoint):
        client = self.create_async_client(endpoint=additionalproperties_endpoint)
        response = await client.is_model.put(
            body={"knownProp": {"state": "str"}},
        )

        # please add some check logic here by yourself
        # ...
