# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ValueTypesClientTestBase, ValueTypesPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestValueTypesExtensibleEnumOperations(ValueTypesClientTestBase):
    @ValueTypesPreparer()
    @recorded_by_proxy
    def test_extensible_enum_get(self, valuetypes_endpoint):
        client = self.create_client(endpoint=valuetypes_endpoint)
        response = client.extensible_enum.get()

        # please add some check logic here by yourself
        # ...

    @ValueTypesPreparer()
    @recorded_by_proxy
    def test_extensible_enum_put(self, valuetypes_endpoint):
        client = self.create_client(endpoint=valuetypes_endpoint)
        response = client.extensible_enum.put(
            body={"property": "str"},
        )

        # please add some check logic here by yourself
        # ...
