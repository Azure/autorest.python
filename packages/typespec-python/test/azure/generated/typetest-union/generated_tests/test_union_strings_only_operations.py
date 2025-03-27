# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import UnionClientTestBase, UnionPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestUnionStringsOnlyOperations(UnionClientTestBase):
    @UnionPreparer()
    @recorded_by_proxy
    def test_strings_only_get(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.strings_only.get()

        # please add some check logic here by yourself
        # ...

    @UnionPreparer()
    @recorded_by_proxy
    def test_strings_only_send(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.strings_only.send(
            body={"prop": "a"},
            prop="a",
        )

        # please add some check logic here by yourself
        # ...
