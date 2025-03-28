# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import AdditionalPropertiesClientTestBase, AdditionalPropertiesPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAdditionalPropertiesIsUnknownDerivedOperations(AdditionalPropertiesClientTestBase):
    @AdditionalPropertiesPreparer()
    @recorded_by_proxy
    def test_is_unknown_derived_get(self, additionalproperties_endpoint):
        client = self.create_client(endpoint=additionalproperties_endpoint)
        response = client.is_unknown_derived.get()

        # please add some check logic here by yourself
        # ...

    @AdditionalPropertiesPreparer()
    @recorded_by_proxy
    def test_is_unknown_derived_put(self, additionalproperties_endpoint):
        client = self.create_client(endpoint=additionalproperties_endpoint)
        response = client.is_unknown_derived.put(
            body={"index": 0, "name": "str", "age": 0.0},
        )

        # please add some check logic here by yourself
        # ...
