# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import AdditionalPropertiesClientTestBase, AdditionalPropertiesPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAdditionalPropertiesSpreadFloatOperations(AdditionalPropertiesClientTestBase):
    @AdditionalPropertiesPreparer()
    @recorded_by_proxy
    def test_spread_float_get(self, additionalproperties_endpoint):
        client = self.create_client(endpoint=additionalproperties_endpoint)
        response = client.spread_float.get()

        # please add some check logic here by yourself
        # ...

    @AdditionalPropertiesPreparer()
    @recorded_by_proxy
    def test_spread_float_put(self, additionalproperties_endpoint):
        client = self.create_client(endpoint=additionalproperties_endpoint)
        response = client.spread_float.put(
            body={"id": 0.0},
        )

        # please add some check logic here by yourself
        # ...
