# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ValueTypesClientTestBase, ValueTypesPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestValueTypesUnknownArrayOperations(ValueTypesClientTestBase):
    @ValueTypesPreparer()
    @recorded_by_proxy
    def test_unknown_array_get(self, valuetypes_endpoint):
        client = self.create_client(endpoint=valuetypes_endpoint)
        response = client.unknown_array.get()

        # please add some check logic here by yourself
        # ...

    @ValueTypesPreparer()
    @recorded_by_proxy
    def test_unknown_array_put(self, valuetypes_endpoint):
        client = self.create_client(endpoint=valuetypes_endpoint)
        response = client.unknown_array.put(
            body={"property": {}},
        )

        # please add some check logic here by yourself
        # ...
