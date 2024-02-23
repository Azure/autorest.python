# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import TwoOperationGroupPreparer
from testpreparer_async import TwoOperationGroupClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestTwoOperationGroupGroup2OperationsAsync(TwoOperationGroupClientTestBaseAsync):
    @TwoOperationGroupPreparer()
    @recorded_by_proxy_async
    async def test_two(self, twooperationgroup_endpoint):
        client = self.create_async_client(endpoint=twooperationgroup_endpoint)
        response = client.group2.two()

        # please add some check logic here by yourself

    @TwoOperationGroupPreparer()
    @recorded_by_proxy_async
    async def test_five(self, twooperationgroup_endpoint):
        client = self.create_async_client(endpoint=twooperationgroup_endpoint)
        response = client.group2.five()

        # please add some check logic here by yourself

    @TwoOperationGroupPreparer()
    @recorded_by_proxy_async
    async def test_six(self, twooperationgroup_endpoint):
        client = self.create_async_client(endpoint=twooperationgroup_endpoint)
        response = client.group2.six()

        # please add some check logic here by yourself
