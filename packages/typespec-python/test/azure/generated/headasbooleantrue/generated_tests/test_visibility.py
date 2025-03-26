# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import VisibilityClientTestBase, VisibilityPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestVisibility(VisibilityClientTestBase):
    @VisibilityPreparer()
    @recorded_by_proxy
    def test_get_model(self, visibility_endpoint):
        client = self.create_client(endpoint=visibility_endpoint)
        response = client.get_model(
            input={"createProp": ["str"], "deleteProp": bool, "queryProp": 0, "readProp": "str", "updateProp": [0]},
        )

        # please add some check logic here by yourself
        # ...

    @VisibilityPreparer()
    @recorded_by_proxy
    def test_head_model(self, visibility_endpoint):
        client = self.create_client(endpoint=visibility_endpoint)
        response = client.head_model(
            input={"createProp": ["str"], "deleteProp": bool, "queryProp": 0, "readProp": "str", "updateProp": [0]},
        )

        # please add some check logic here by yourself
        # ...

    @VisibilityPreparer()
    @recorded_by_proxy
    def test_put_model(self, visibility_endpoint):
        client = self.create_client(endpoint=visibility_endpoint)
        response = client.put_model(
            input={"createProp": ["str"], "deleteProp": bool, "queryProp": 0, "readProp": "str", "updateProp": [0]},
        )

        # please add some check logic here by yourself
        # ...

    @VisibilityPreparer()
    @recorded_by_proxy
    def test_patch_model(self, visibility_endpoint):
        client = self.create_client(endpoint=visibility_endpoint)
        response = client.patch_model(
            input={"createProp": ["str"], "deleteProp": bool, "queryProp": 0, "readProp": "str", "updateProp": [0]},
        )

        # please add some check logic here by yourself
        # ...

    @VisibilityPreparer()
    @recorded_by_proxy
    def test_post_model(self, visibility_endpoint):
        client = self.create_client(endpoint=visibility_endpoint)
        response = client.post_model(
            input={"createProp": ["str"], "deleteProp": bool, "queryProp": 0, "readProp": "str", "updateProp": [0]},
        )

        # please add some check logic here by yourself
        # ...

    @VisibilityPreparer()
    @recorded_by_proxy
    def test_delete_model(self, visibility_endpoint):
        client = self.create_client(endpoint=visibility_endpoint)
        response = client.delete_model(
            input={"createProp": ["str"], "deleteProp": bool, "queryProp": 0, "readProp": "str", "updateProp": [0]},
        )

        # please add some check logic here by yourself
        # ...

    @VisibilityPreparer()
    @recorded_by_proxy
    def test_put_read_only_model(self, visibility_endpoint):
        client = self.create_client(endpoint=visibility_endpoint)
        response = client.put_read_only_model(
            input={"optionalNullableIntList": [0], "optionalStringRecord": {"str": "str"}},
        )

        # please add some check logic here by yourself
        # ...
