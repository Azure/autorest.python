# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import JsonMergePatchClientTestBase, JsonMergePatchPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestJsonMergePatch(JsonMergePatchClientTestBase):
    @JsonMergePatchPreparer()
    @recorded_by_proxy
    def test_create_resource(self, jsonmergepatch_endpoint):
        client = self.create_client(endpoint=jsonmergepatch_endpoint)
        response = client.create_resource(
            body={
                "name": "str",
                "array": [{"description": "str", "name": "str"}],
                "description": "str",
                "floatValue": 0.0,
                "innerModel": {"description": "str", "name": "str"},
                "intArray": [0],
                "intValue": 0,
                "map": {"str": {"description": "str", "name": "str"}},
            },
        )

        # please add some check logic here by yourself
        # ...

    @JsonMergePatchPreparer()
    @recorded_by_proxy
    def test_update_resource(self, jsonmergepatch_endpoint):
        client = self.create_client(endpoint=jsonmergepatch_endpoint)
        response = client.update_resource(
            body={
                "array": [{"description": "str", "name": "str"}],
                "description": "str",
                "floatValue": 0.0,
                "innerModel": {"description": "str", "name": "str"},
                "intArray": [0],
                "intValue": 0,
                "map": {"str": {"description": "str", "name": "str"}},
            },
        )

        # please add some check logic here by yourself
        # ...

    @JsonMergePatchPreparer()
    @recorded_by_proxy
    def test_update_optional_resource(self, jsonmergepatch_endpoint):
        client = self.create_client(endpoint=jsonmergepatch_endpoint)
        response = client.update_optional_resource()

        # please add some check logic here by yourself
        # ...
