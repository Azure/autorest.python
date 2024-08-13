# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import SubNamespace.SecondPreparer
from testpreparer_async import SubNamespace.SecondClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSubNamespace.SecondGroup5OperationsAsync(SubNamespace.SecondClientTestBaseAsync):
    @SubNamespace.SecondPreparer()
    @recorded_by_proxy_async
    async def test_six(self, subnamespace.second_endpoint):
        client = self.create_async_client(endpoint=subnamespace.second_endpoint)
        response = await client.group5.six(
        )
        
        # please add some check logic here by yourself
        # ...

