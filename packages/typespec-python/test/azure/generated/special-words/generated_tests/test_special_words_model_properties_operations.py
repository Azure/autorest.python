# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import SpecialWordsClientTestBase, SpecialWordsPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSpecialWordsModelPropertiesOperations(SpecialWordsClientTestBase):
    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_same_as_model(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.model_properties.same_as_model(
            body={"SameAsModel": "str"},
        )

        # please add some check logic here by yourself
        # ...
