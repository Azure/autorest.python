# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import NullableClientTestBase, NullablePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNullableCollectionsStringOperations(NullableClientTestBase):
    @NullablePreparer()
    @recorded_by_proxy
    def test_collections_string_get_non_null(self, nullable_endpoint):
        client = self.create_client(endpoint=nullable_endpoint)
        response = client.collections_string.get_non_null()

        # please add some check logic here by yourself
        # ...

    @NullablePreparer()
    @recorded_by_proxy
    def test_collections_string_get_null(self, nullable_endpoint):
        client = self.create_client(endpoint=nullable_endpoint)
        response = client.collections_string.get_null()

        # please add some check logic here by yourself
        # ...

    @NullablePreparer()
    @recorded_by_proxy
    def test_collections_string_patch_non_null(self, nullable_endpoint):
        client = self.create_client(endpoint=nullable_endpoint)
        response = client.collections_string.patch_non_null(
            body={"nullableProperty": ["str"], "requiredProperty": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @NullablePreparer()
    @recorded_by_proxy
    def test_collections_string_patch_null(self, nullable_endpoint):
        client = self.create_client(endpoint=nullable_endpoint)
        response = client.collections_string.patch_null(
            body={"nullableProperty": ["str"], "requiredProperty": "str"},
        )

        # please add some check logic here by yourself
        # ...
