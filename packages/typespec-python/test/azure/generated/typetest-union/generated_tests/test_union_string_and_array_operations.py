# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import UnionClientTestBase, UnionPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestUnionStringAndArrayOperations(UnionClientTestBase):
    @UnionPreparer()
    @recorded_by_proxy
    def test_string_and_array_get(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.string_and_array.get()

        # please add some check logic here by yourself
        # ...

    @UnionPreparer()
    @recorded_by_proxy
    def test_string_and_array_send(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.string_and_array.send(
            body={"prop": {"array": "str", "string": "str"}},
            prop={"array": "str", "string": "str"},
        )

        # please add some check logic here by yourself
        # ...
