# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import NullableClientTestBase, NullablePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNullableCollectionsModelOperations(NullableClientTestBase):
    @NullablePreparer()
    @recorded_by_proxy
    def test_collections_model_get_non_null(self, nullable_endpoint):
        client = self.create_client(endpoint=nullable_endpoint)
        response = client.collections_model.get_non_null()

        # please add some check logic here by yourself
        # ...

    @NullablePreparer()
    @recorded_by_proxy
    def test_collections_model_get_null(self, nullable_endpoint):
        client = self.create_client(endpoint=nullable_endpoint)
        response = client.collections_model.get_null()

        # please add some check logic here by yourself
        # ...

    @NullablePreparer()
    @recorded_by_proxy
    def test_collections_model_patch_non_null(self, nullable_endpoint):
        client = self.create_client(endpoint=nullable_endpoint)
        response = client.collections_model.patch_non_null(
            body={"nullableProperty": [{"property": "str"}], "requiredProperty": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @NullablePreparer()
    @recorded_by_proxy
    def test_collections_model_patch_null(self, nullable_endpoint):
        client = self.create_client(endpoint=nullable_endpoint)
        response = client.collections_model.patch_null(
            body={"nullableProperty": [{"property": "str"}], "requiredProperty": "str"},
        )

        # please add some check logic here by yourself
        # ...
