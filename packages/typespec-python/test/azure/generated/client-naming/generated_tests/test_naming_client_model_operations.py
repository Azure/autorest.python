# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft Corporation (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import NamingClientTestBase, NamingPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNamingClientModelOperations(NamingClientTestBase):
    @NamingPreparer()
    @recorded_by_proxy
    def test_client_model_client(self, naming_endpoint):
        client = self.create_client(endpoint=naming_endpoint)
        response = client.client_model.client(
            body={"defaultName": bool},
        )

        # please add some check logic here by yourself
        # ...

    @NamingPreparer()
    @recorded_by_proxy
    def test_client_model_language(self, naming_endpoint):
        client = self.create_client(endpoint=naming_endpoint)
        response = client.client_model.language(
            body={"defaultName": bool},
        )

        # please add some check logic here by yourself
        # ...
