# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft Corporation (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import StandardClientTestBase, StandardPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestStandard(StandardClientTestBase):
    @StandardPreparer()
    @recorded_by_proxy
    def test_begin_create_or_replace(self, standard_endpoint):
        client = self.create_client(endpoint=standard_endpoint)
        response = client.begin_create_or_replace(
            name="str",
            resource={"name": "str", "role": "str"},
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @StandardPreparer()
    @recorded_by_proxy
    def test_begin_delete(self, standard_endpoint):
        client = self.create_client(endpoint=standard_endpoint)
        response = client.begin_delete(
            name="str",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @StandardPreparer()
    @recorded_by_proxy
    def test_begin_export(self, standard_endpoint):
        client = self.create_client(endpoint=standard_endpoint)
        response = client.begin_export(
            name="str",
            format="str",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
