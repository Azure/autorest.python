# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import PageClientTestBase, PagePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestPage(PageClientTestBase):
    @PagePreparer()
    @recorded_by_proxy
    def test_list_with_page(self, page_endpoint):
        client = self.create_client(endpoint=page_endpoint)
        response = client.list_with_page()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @PagePreparer()
    @recorded_by_proxy
    def test_list_with_parameters(self, page_endpoint):
        client = self.create_client(endpoint=page_endpoint)
        response = client.list_with_parameters(
            body_input={"inputName": "str"},
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @PagePreparer()
    @recorded_by_proxy
    def test_list_with_custom_page_model(self, page_endpoint):
        client = self.create_client(endpoint=page_endpoint)
        response = client.list_with_custom_page_model()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @PagePreparer()
    @recorded_by_proxy
    def test_with_parameterized_next_link(self, page_endpoint):
        client = self.create_client(endpoint=page_endpoint)
        response = client.with_parameterized_next_link(
            select="str",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
