# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ValueTypesClientTestBase, ValueTypesPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestValueTypesIntLiteralOperations(ValueTypesClientTestBase):
    @ValueTypesPreparer()
    @recorded_by_proxy
    def test_int_literal_get(self, valuetypes_endpoint):
        client = self.create_client(endpoint=valuetypes_endpoint)
        response = client.int_literal.get()

        # please add some check logic here by yourself
        # ...

    @ValueTypesPreparer()
    @recorded_by_proxy
    def test_int_literal_put(self, valuetypes_endpoint):
        client = self.create_client(endpoint=valuetypes_endpoint)
        response = client.int_literal.put(
            body={"property": 42},
        )

        # please add some check logic here by yourself
        # ...
