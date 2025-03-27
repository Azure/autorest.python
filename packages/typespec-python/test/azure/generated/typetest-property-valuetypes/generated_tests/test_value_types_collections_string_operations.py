# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ValueTypesClientTestBase, ValueTypesPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestValueTypesCollectionsStringOperations(ValueTypesClientTestBase):
    @ValueTypesPreparer()
    @recorded_by_proxy
    def test_collections_string_get(self, valuetypes_endpoint):
        client = self.create_client(endpoint=valuetypes_endpoint)
        response = client.collections_string.get()

        # please add some check logic here by yourself
        # ...

    @ValueTypesPreparer()
    @recorded_by_proxy
    def test_collections_string_put(self, valuetypes_endpoint):
        client = self.create_client(endpoint=valuetypes_endpoint)
        response = client.collections_string.put(
            body={"property": ["str"]},
        )

        # please add some check logic here by yourself
        # ...
