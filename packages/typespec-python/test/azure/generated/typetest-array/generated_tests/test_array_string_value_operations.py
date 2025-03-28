# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ArrayClientTestBase, ArrayPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestArrayStringValueOperations(ArrayClientTestBase):
    @ArrayPreparer()
    @recorded_by_proxy
    def test_string_value_get(self, array_endpoint):
        client = self.create_client(endpoint=array_endpoint)
        response = client.string_value.get()

        # please add some check logic here by yourself
        # ...

    @ArrayPreparer()
    @recorded_by_proxy
    def test_string_value_put(self, array_endpoint):
        client = self.create_client(endpoint=array_endpoint)
        response = client.string_value.put(
            body=["str"],
        )

        # please add some check logic here by yourself
        # ...
