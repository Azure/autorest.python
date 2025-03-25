# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft Corporation (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import StatusCodeRangeClientTestBase, StatusCodeRangePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestStatusCodeRange(StatusCodeRangeClientTestBase):
    @StatusCodeRangePreparer()
    @recorded_by_proxy
    def test_error_response_status_code_in_range(self, statuscoderange_endpoint):
        client = self.create_client(endpoint=statuscoderange_endpoint)
        response = client.error_response_status_code_in_range()

        # please add some check logic here by yourself
        # ...

    @StatusCodeRangePreparer()
    @recorded_by_proxy
    def test_error_response_status_code404(self, statuscoderange_endpoint):
        client = self.create_client(endpoint=statuscoderange_endpoint)
        response = client.error_response_status_code404()

        # please add some check logic here by yourself
        # ...
