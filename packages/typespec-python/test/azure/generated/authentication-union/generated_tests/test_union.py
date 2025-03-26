# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import UnionClientTestBase, UnionPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestUnion(UnionClientTestBase):
    @UnionPreparer()
    @recorded_by_proxy
    def test_valid_key(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.valid_key()

        # please add some check logic here by yourself
        # ...

    @UnionPreparer()
    @recorded_by_proxy
    def test_valid_token(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.valid_token()

        # please add some check logic here by yourself
        # ...
