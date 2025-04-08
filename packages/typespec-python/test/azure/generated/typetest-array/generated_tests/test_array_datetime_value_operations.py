# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ArrayClientTestBase, ArrayPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestArrayDatetimeValueOperations(ArrayClientTestBase):
    @ArrayPreparer()
    @recorded_by_proxy
    def test_datetime_value_get(self, array_endpoint):
        client = self.create_client(endpoint=array_endpoint)
        response = client.datetime_value.get()

        # please add some check logic here by yourself
        # ...

    @ArrayPreparer()
    @recorded_by_proxy
    def test_datetime_value_put(self, array_endpoint):
        client = self.create_client(endpoint=array_endpoint)
        response = client.datetime_value.put(
            body=["2020-02-20 00:00:00"],
        )

        # please add some check logic here by yourself
        # ...
