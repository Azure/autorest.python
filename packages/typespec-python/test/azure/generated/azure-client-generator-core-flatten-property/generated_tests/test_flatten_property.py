# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import FlattenPropertyClientTestBase, FlattenPropertyPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestFlattenProperty(FlattenPropertyClientTestBase):
    @FlattenPropertyPreparer()
    @recorded_by_proxy
    def test_put_flatten_model(self, flattenproperty_endpoint):
        client = self.create_client(endpoint=flattenproperty_endpoint)
        response = client.put_flatten_model(
            input={"name": "str", "properties": {"age": 0, "description": "str"}},
        )

        # please add some check logic here by yourself
        # ...

    @FlattenPropertyPreparer()
    @recorded_by_proxy
    def test_put_nested_flatten_model(self, flattenproperty_endpoint):
        client = self.create_client(endpoint=flattenproperty_endpoint)
        response = client.put_nested_flatten_model(
            input={"name": "str", "properties": {"properties": {"age": 0, "description": "str"}, "summary": "str"}},
        )

        # please add some check logic here by yourself
        # ...
