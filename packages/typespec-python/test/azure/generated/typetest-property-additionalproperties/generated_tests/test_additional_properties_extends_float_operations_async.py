# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import AdditionalPropertiesPreparer
from testpreparer_async import AdditionalPropertiesClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAdditionalPropertiesExtendsFloatOperationsAsync(AdditionalPropertiesClientTestBaseAsync):
    @AdditionalPropertiesPreparer()
    @recorded_by_proxy_async
    async def test_extends_float_get(self, additionalproperties_endpoint):
        client = self.create_async_client(endpoint=additionalproperties_endpoint)
        response = await client.extends_float.get()

        # please add some check logic here by yourself
        # ...

    @AdditionalPropertiesPreparer()
    @recorded_by_proxy_async
    async def test_extends_float_put(self, additionalproperties_endpoint):
        client = self.create_async_client(endpoint=additionalproperties_endpoint)
        response = await client.extends_float.put(
            body={"id": 0.0},
        )

        # please add some check logic here by yourself
        # ...
