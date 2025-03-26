# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ArrayClientTestBase, ArrayPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestArrayModelValueOperations(ArrayClientTestBase):
    @ArrayPreparer()
    @recorded_by_proxy
    def test_model_value_get(self, array_endpoint):
        client = self.create_client(endpoint=array_endpoint)
        response = client.model_value.get()

        # please add some check logic here by yourself
        # ...

    @ArrayPreparer()
    @recorded_by_proxy
    def test_model_value_put(self, array_endpoint):
        client = self.create_client(endpoint=array_endpoint)
        response = client.model_value.put(
            body=[{"property": "str", "children": [...]}],
        )

        # please add some check logic here by yourself
        # ...
