# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ArrayClientTestBase, ArrayPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestArrayNullableFloatValueOperations(ArrayClientTestBase):
    @ArrayPreparer()
    @recorded_by_proxy
    def test_nullable_float_value_get(self, array_endpoint):
        client = self.create_client(endpoint=array_endpoint)
        response = client.nullable_float_value.get()

        # please add some check logic here by yourself
        # ...

    @ArrayPreparer()
    @recorded_by_proxy
    def test_nullable_float_value_put(self, array_endpoint):
        client = self.create_client(endpoint=array_endpoint)
        response = client.nullable_float_value.put(
            body=[0.0],
        )

        # please add some check logic here by yourself
        # ...
