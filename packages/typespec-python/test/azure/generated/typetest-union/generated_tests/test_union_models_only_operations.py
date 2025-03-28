# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import UnionClientTestBase, UnionPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestUnionModelsOnlyOperations(UnionClientTestBase):
    @UnionPreparer()
    @recorded_by_proxy
    def test_models_only_get(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.models_only.get()

        # please add some check logic here by yourself
        # ...

    @UnionPreparer()
    @recorded_by_proxy
    def test_models_only_send(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.models_only.send(
            body={"prop": {"name": "str"}},
            prop={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...
