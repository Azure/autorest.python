# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import NullableClientTestBase, NullablePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNullableCollectionsByteOperations(NullableClientTestBase):
    @NullablePreparer()
    @recorded_by_proxy
    def test_collections_byte_get_non_null(self, nullable_endpoint):
        client = self.create_client(endpoint=nullable_endpoint)
        response = client.collections_byte.get_non_null()

        # please add some check logic here by yourself
        # ...

    @NullablePreparer()
    @recorded_by_proxy
    def test_collections_byte_get_null(self, nullable_endpoint):
        client = self.create_client(endpoint=nullable_endpoint)
        response = client.collections_byte.get_null()

        # please add some check logic here by yourself
        # ...

    @NullablePreparer()
    @recorded_by_proxy
    def test_collections_byte_patch_non_null(self, nullable_endpoint):
        client = self.create_client(endpoint=nullable_endpoint)
        response = client.collections_byte.patch_non_null(
            body={"nullableProperty": [bytes("bytes", encoding="utf-8")], "requiredProperty": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @NullablePreparer()
    @recorded_by_proxy
    def test_collections_byte_patch_null(self, nullable_endpoint):
        client = self.create_client(endpoint=nullable_endpoint)
        response = client.collections_byte.patch_null(
            body={"nullableProperty": [bytes("bytes", encoding="utf-8")], "requiredProperty": "str"},
        )

        # please add some check logic here by yourself
        # ...
