# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import AdditionalPropertiesClientTestBase, AdditionalPropertiesPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAdditionalPropertiesIsUnknownOperations(AdditionalPropertiesClientTestBase):
    @AdditionalPropertiesPreparer()
    @recorded_by_proxy
    def test_is_unknown_get(self, additionalproperties_endpoint):
        client = self.create_client(endpoint=additionalproperties_endpoint)
        response = client.is_unknown.get()

        # please add some check logic here by yourself
        # ...

    @AdditionalPropertiesPreparer()
    @recorded_by_proxy
    def test_is_unknown_put(self, additionalproperties_endpoint):
        client = self.create_client(endpoint=additionalproperties_endpoint)
        response = client.is_unknown.put(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...
