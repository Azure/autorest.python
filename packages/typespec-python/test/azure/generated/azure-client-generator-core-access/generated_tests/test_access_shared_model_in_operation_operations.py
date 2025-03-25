# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import AccessClientTestBase, AccessPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAccessSharedModelInOperationOperations(AccessClientTestBase):
    @AccessPreparer()
    @recorded_by_proxy
    def test_shared_model_in_operation_public(self, access_endpoint):
        client = self.create_client(endpoint=access_endpoint)
        response = client.shared_model_in_operation.public(
            name="str",
        )

        # please add some check logic here by yourself
        # ...
