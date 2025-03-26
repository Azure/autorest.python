# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ArrayClientTestBase, ArrayPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestArrayUnknownValueOperations(ArrayClientTestBase):
    @ArrayPreparer()
    @recorded_by_proxy
    def test_unknown_value_get(self, array_endpoint):
        client = self.create_client(endpoint=array_endpoint)
        response = client.unknown_value.get()

        # please add some check logic here by yourself
        # ...

    @ArrayPreparer()
    @recorded_by_proxy
    def test_unknown_value_put(self, array_endpoint):
        client = self.create_client(endpoint=array_endpoint)
        response = client.unknown_value.put(
            body=[{}],
        )

        # please add some check logic here by yourself
        # ...
