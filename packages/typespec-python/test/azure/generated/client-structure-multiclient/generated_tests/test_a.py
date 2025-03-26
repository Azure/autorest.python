# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import APreparer, ClientAClientTestBase


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestA(ClientAClientTestBase):
    @APreparer()
    @recorded_by_proxy
    def test_renamed_one(self, a_endpoint):
        client = self.create_client(endpoint=a_endpoint)
        response = client.renamed_one()

        # please add some check logic here by yourself
        # ...

    @APreparer()
    @recorded_by_proxy
    def test_renamed_three(self, a_endpoint):
        client = self.create_client(endpoint=a_endpoint)
        response = client.renamed_three()

        # please add some check logic here by yourself
        # ...

    @APreparer()
    @recorded_by_proxy
    def test_renamed_five(self, a_endpoint):
        client = self.create_client(endpoint=a_endpoint)
        response = client.renamed_five()

        # please add some check logic here by yourself
        # ...
