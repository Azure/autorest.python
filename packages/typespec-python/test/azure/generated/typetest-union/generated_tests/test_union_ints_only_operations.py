# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import UnionClientTestBase, UnionPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestUnionIntsOnlyOperations(UnionClientTestBase):
    @UnionPreparer()
    @recorded_by_proxy
    def test_ints_only_get(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.ints_only.get()

        # please add some check logic here by yourself
        # ...

    @UnionPreparer()
    @recorded_by_proxy
    def test_ints_only_send(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.ints_only.send(
            body={"prop": 1},
            prop=1,
        )

        # please add some check logic here by yourself
        # ...
