# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import DeserializeEmptyStringAsNullClientTestBase, DeserializeEmptyStringAsNullPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDeserializeEmptyStringAsNull(DeserializeEmptyStringAsNullClientTestBase):
    @DeserializeEmptyStringAsNullPreparer()
    @recorded_by_proxy
    def test_get(self, deserializeemptystringasnull_endpoint):
        client = self.create_client(endpoint=deserializeemptystringasnull_endpoint)
        response = client.get()

        # please add some check logic here by yourself
        # ...
