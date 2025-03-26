# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import OptionalClientTestBase, OptionalPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestOptionalCollectionsModelOperations(OptionalClientTestBase):
    @OptionalPreparer()
    @recorded_by_proxy
    def test_collections_model_get_all(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.collections_model.get_all()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_collections_model_get_default(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.collections_model.get_default()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_collections_model_put_all(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.collections_model.put_all(
            body={"property": [{"property": "str"}]},
        )

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_collections_model_put_default(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.collections_model.put_default(
            body={"property": [{"property": "str"}]},
        )

        # please add some check logic here by yourself
        # ...
