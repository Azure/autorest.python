# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import CollectionFormatClientTestBase, CollectionFormatPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestCollectionFormatHeaderOperations(CollectionFormatClientTestBase):
    @CollectionFormatPreparer()
    @recorded_by_proxy
    def test_csv(self, collectionformat_endpoint):
        client = self.create_client(endpoint=collectionformat_endpoint)
        response = client.header.csv(
            colors=["str"],
        )

        # please add some check logic here by yourself
        # ...