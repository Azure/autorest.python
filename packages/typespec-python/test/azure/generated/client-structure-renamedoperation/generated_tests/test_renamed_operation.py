# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import RenamedOperationClientTestBase, RenamedOperationPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRenamedOperation(RenamedOperationClientTestBase):
    @RenamedOperationPreparer()
    @recorded_by_proxy
    def test_renamed_one(self, renamedoperation_endpoint):
        client = self.create_client(endpoint=renamedoperation_endpoint)
        response = client.renamed_one()

        # please add some check logic here by yourself
        # ...

    @RenamedOperationPreparer()
    @recorded_by_proxy
    def test_renamed_three(self, renamedoperation_endpoint):
        client = self.create_client(endpoint=renamedoperation_endpoint)
        response = client.renamed_three()

        # please add some check logic here by yourself
        # ...

    @RenamedOperationPreparer()
    @recorded_by_proxy
    def test_renamed_five(self, renamedoperation_endpoint):
        client = self.create_client(endpoint=renamedoperation_endpoint)
        response = client.renamed_five()

        # please add some check logic here by yourself
        # ...
