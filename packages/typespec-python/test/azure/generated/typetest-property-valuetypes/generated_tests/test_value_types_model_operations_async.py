# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import ValueTypesPreparer
from testpreparer_async import ValueTypesClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestValueTypesModelOperationsAsync(ValueTypesClientTestBaseAsync):
    @ValueTypesPreparer()
    @recorded_by_proxy_async
    async def test_get(self, valuetypes_endpoint):
        client = self.create_async_client(endpoint=valuetypes_endpoint)
        response = await client.model.get()

        # please add some check logic here by yourself
        # ...

    @ValueTypesPreparer()
    @recorded_by_proxy_async
    async def test_put(self, valuetypes_endpoint):
        client = self.create_async_client(endpoint=valuetypes_endpoint)
        response = await client.model.put(
            body={"property": {"property": "str"}},
        )

        # please add some check logic here by yourself
        # ...
