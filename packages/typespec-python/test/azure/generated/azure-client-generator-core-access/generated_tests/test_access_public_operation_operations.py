# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import AccessClientTestBase, AccessPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAccessPublicOperationOperations(AccessClientTestBase):
    @AccessPreparer()
    @recorded_by_proxy
    def test_public_operation_no_decorator_in_public(self, access_endpoint):
        client = self.create_client(endpoint=access_endpoint)
        response = client.public_operation.no_decorator_in_public(
            name="str",
        )

        # please add some check logic here by yourself
        # ...

    @AccessPreparer()
    @recorded_by_proxy
    def test_public_operation_public_decorator_in_public(self, access_endpoint):
        client = self.create_client(endpoint=access_endpoint)
        response = client.public_operation.public_decorator_in_public(
            name="str",
        )

        # please add some check logic here by yourself
        # ...
