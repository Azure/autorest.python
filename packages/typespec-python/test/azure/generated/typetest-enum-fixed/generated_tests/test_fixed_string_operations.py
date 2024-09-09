# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import FixedClientTestBase, FixedPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestFixedStringOperations(FixedClientTestBase):
    @FixedPreparer()
    @recorded_by_proxy
    def test_string_get_known_value(self, fixed_endpoint):
        client = self.create_client(endpoint=fixed_endpoint)
        response = client.string.get_known_value()

        # please add some check logic here by yourself
        # ...

    @FixedPreparer()
    @recorded_by_proxy
    def test_string_put_known_value(self, fixed_endpoint):
        client = self.create_client(endpoint=fixed_endpoint)
        response = client.string.put_known_value(
            body="str",
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...

    @FixedPreparer()
    @recorded_by_proxy
    def test_string_put_unknown_value(self, fixed_endpoint):
        client = self.create_client(endpoint=fixed_endpoint)
        response = client.string.put_unknown_value(
            body="str",
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...
