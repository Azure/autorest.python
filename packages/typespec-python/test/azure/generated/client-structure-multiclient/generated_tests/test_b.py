# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import BPreparer, ClientBClientTestBase


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestB(ClientBClientTestBase):
    @BPreparer()
    @recorded_by_proxy
    def test_renamed_two(self, b_endpoint):
        client = self.create_client(endpoint=b_endpoint)
        response = client.renamed_two()

        # please add some check logic here by yourself
        # ...

    @BPreparer()
    @recorded_by_proxy
    def test_renamed_four(self, b_endpoint):
        client = self.create_client(endpoint=b_endpoint)
        response = client.renamed_four()

        # please add some check logic here by yourself
        # ...

    @BPreparer()
    @recorded_by_proxy
    def test_renamed_six(self, b_endpoint):
        client = self.create_client(endpoint=b_endpoint)
        response = client.renamed_six()

        # please add some check logic here by yourself
        # ...
