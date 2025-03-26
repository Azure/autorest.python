# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import RenamedOperationClientTestBase, RenamedOperationPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRenamedOperationGroupOperations(RenamedOperationClientTestBase):
    @RenamedOperationPreparer()
    @recorded_by_proxy
    def test_group_renamed_two(self, renamedoperation_endpoint):
        client = self.create_client(endpoint=renamedoperation_endpoint)
        response = client.group.renamed_two()

        # please add some check logic here by yourself
        # ...

    @RenamedOperationPreparer()
    @recorded_by_proxy
    def test_group_renamed_four(self, renamedoperation_endpoint):
        client = self.create_client(endpoint=renamedoperation_endpoint)
        response = client.group.renamed_four()

        # please add some check logic here by yourself
        # ...

    @RenamedOperationPreparer()
    @recorded_by_proxy
    def test_group_renamed_six(self, renamedoperation_endpoint):
        client = self.create_client(endpoint=renamedoperation_endpoint)
        response = client.group.renamed_six()

        # please add some check logic here by yourself
        # ...
