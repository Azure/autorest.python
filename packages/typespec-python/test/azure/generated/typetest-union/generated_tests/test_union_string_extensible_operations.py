# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import UnionClientTestBase, UnionPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestUnionStringExtensibleOperations(UnionClientTestBase):
    @UnionPreparer()
    @recorded_by_proxy
    def test_string_extensible_get(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.string_extensible.get()

        # please add some check logic here by yourself
        # ...

    @UnionPreparer()
    @recorded_by_proxy
    def test_string_extensible_send(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.string_extensible.send(
            body={"prop": "b"},
            prop="b",
        )

        # please add some check logic here by yourself
        # ...
