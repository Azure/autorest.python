# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import RemovedClientTestBase, RemovedPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRemoved(RemovedClientTestBase):
    @RemovedPreparer()
    @recorded_by_proxy
    def test_v2(self, removed_endpoint):
        client = self.create_client(endpoint=removed_endpoint)
        response = client.v2(
            body={"enumProp": "str", "prop": "str", "unionProp": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @RemovedPreparer()
    @recorded_by_proxy
    def test_model_v3(self, removed_endpoint):
        client = self.create_client(endpoint=removed_endpoint)
        response = client.model_v3(
            body={"enumProp": "str", "id": "str"},
        )

        # please add some check logic here by yourself
        # ...
