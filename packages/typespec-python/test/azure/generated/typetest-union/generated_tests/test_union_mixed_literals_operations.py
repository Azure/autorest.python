# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import UnionClientTestBase, UnionPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestUnionMixedLiteralsOperations(UnionClientTestBase):
    @UnionPreparer()
    @recorded_by_proxy
    def test_mixed_literals_get(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.mixed_literals.get()

        # please add some check logic here by yourself
        # ...

    @UnionPreparer()
    @recorded_by_proxy
    def test_mixed_literals_send(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.mixed_literals.send(
            body={"prop": {"booleanLiteral": "a", "floatLiteral": "a", "intLiteral": "a", "stringLiteral": "a"}},
            prop={"booleanLiteral": "a", "floatLiteral": "a", "intLiteral": "a", "stringLiteral": "a"},
        )

        # please add some check logic here by yourself
        # ...
