# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft Corporation (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import AddedPreparer
from testpreparer_async import AddedClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAddedInterfaceV2OperationsAsync(AddedClientTestBaseAsync):
    @AddedPreparer()
    @recorded_by_proxy_async
    async def test_interface_v2_v2_in_interface(self, added_endpoint):
        client = self.create_async_client(endpoint=added_endpoint)
        response = await client.interface_v2.v2_in_interface(
            body={"enumProp": "str", "prop": "str", "unionProp": "str"},
        )

        # please add some check logic here by yourself
        # ...
