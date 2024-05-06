# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import TraitsClientTestBase, TraitsPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestTraits(TraitsClientTestBase):
    @TraitsPreparer()
    @recorded_by_proxy
    def test_smoke_test(self, traits_endpoint):
        client = self.create_client(endpoint=traits_endpoint)
        response = client.smoke_test(
            id=0,
            foo="str",
        )

        # please add some check logic here by yourself
        # ...

    @TraitsPreparer()
    @recorded_by_proxy
    def test_repeatable_action(self, traits_endpoint):
        client = self.create_client(endpoint=traits_endpoint)
        response = client.repeatable_action(
            id=0,
            body={"userActionValue": "str"},
        )

        # please add some check logic here by yourself
        # ...
