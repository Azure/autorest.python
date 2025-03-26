# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import AdditionalPropertiesClientTestBase, AdditionalPropertiesPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAdditionalPropertiesSpreadRecordUnionOperations(AdditionalPropertiesClientTestBase):
    @AdditionalPropertiesPreparer()
    @recorded_by_proxy
    def test_spread_record_union_get(self, additionalproperties_endpoint):
        client = self.create_client(endpoint=additionalproperties_endpoint)
        response = client.spread_record_union.get()

        # please add some check logic here by yourself
        # ...

    @AdditionalPropertiesPreparer()
    @recorded_by_proxy
    def test_spread_record_union_put(self, additionalproperties_endpoint):
        client = self.create_client(endpoint=additionalproperties_endpoint)
        response = client.spread_record_union.put(
            body={"flag": bool},
        )

        # please add some check logic here by yourself
        # ...
