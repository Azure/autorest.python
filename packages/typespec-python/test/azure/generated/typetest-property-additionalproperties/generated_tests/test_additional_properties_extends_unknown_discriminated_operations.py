# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import AdditionalPropertiesClientTestBase, AdditionalPropertiesPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAdditionalPropertiesExtendsUnknownDiscriminatedOperations(AdditionalPropertiesClientTestBase):
    @AdditionalPropertiesPreparer()
    @recorded_by_proxy
    def test_extends_unknown_discriminated_get(self, additionalproperties_endpoint):
        client = self.create_client(endpoint=additionalproperties_endpoint)
        response = client.extends_unknown_discriminated.get()

        # please add some check logic here by yourself
        # ...

    @AdditionalPropertiesPreparer()
    @recorded_by_proxy
    def test_extends_unknown_discriminated_put(self, additionalproperties_endpoint):
        client = self.create_client(endpoint=additionalproperties_endpoint)
        response = client.extends_unknown_discriminated.put(
            body={"index": 0, "kind": "derived", "name": "str", "age": 0.0},
        )

        # please add some check logic here by yourself
        # ...
