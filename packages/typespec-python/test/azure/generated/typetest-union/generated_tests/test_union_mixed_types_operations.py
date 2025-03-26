# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import UnionClientTestBase, UnionPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestUnionMixedTypesOperations(UnionClientTestBase):
    @UnionPreparer()
    @recorded_by_proxy
    def test_mixed_types_get(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.mixed_types.get()

        # please add some check logic here by yourself
        # ...

    @UnionPreparer()
    @recorded_by_proxy
    def test_mixed_types_send(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.mixed_types.send(
            body={
                "prop": {
                    "array": [{"name": "str"}],
                    "boolean": {"name": "str"},
                    "int": {"name": "str"},
                    "literal": {"name": "str"},
                    "model": {"name": "str"},
                }
            },
            prop={
                "array": [{"name": "str"}],
                "boolean": {"name": "str"},
                "int": {"name": "str"},
                "literal": {"name": "str"},
                "model": {"name": "str"},
            },
        )

        # please add some check logic here by yourself
        # ...
