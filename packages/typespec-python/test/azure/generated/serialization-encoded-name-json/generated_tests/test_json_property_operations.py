# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import JsonClientTestBase, JsonPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestJsonPropertyOperations(JsonClientTestBase):
    @JsonPreparer()
    @recorded_by_proxy
    def test_property_send(self, json_endpoint):
        client = self.create_client(endpoint=json_endpoint)
        response = client.property.send(
            body={"wireName": bool},
        )

        # please add some check logic here by yourself
        # ...

    @JsonPreparer()
    @recorded_by_proxy
    def test_property_get(self, json_endpoint):
        client = self.create_client(endpoint=json_endpoint)
        response = client.property.get()

        # please add some check logic here by yourself
        # ...
