# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ArrayClientTestBase, ArrayPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestArrayBooleanValueOperations(ArrayClientTestBase):
    @ArrayPreparer()
    @recorded_by_proxy
    def test_boolean_value_get(self, array_endpoint):
        client = self.create_client(endpoint=array_endpoint)
        response = client.boolean_value.get()

        # please add some check logic here by yourself
        # ...

    @ArrayPreparer()
    @recorded_by_proxy
    def test_boolean_value_put(self, array_endpoint):
        client = self.create_client(endpoint=array_endpoint)
        response = client.boolean_value.put(
            body=[bool],
        )

        # please add some check logic here by yourself
        # ...
