# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import UnionPreparer
from testpreparer_async import UnionClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestUnionEnumsOnlyOperationsAsync(UnionClientTestBaseAsync):
    @UnionPreparer()
    @recorded_by_proxy_async
    async def test_get(self, union_endpoint):
        client = self.create_async_client(endpoint=union_endpoint)
        response = await client.enums_only.get()

        # please add some check logic here by yourself
        # ...

    @UnionPreparer()
    @recorded_by_proxy_async
    async def test_send(self, union_endpoint):
        client = self.create_async_client(endpoint=union_endpoint)
        response = await client.enums_only.send(
            body={"prop": {"lr": "left", "ud": "up"}},
            prop={"lr": "left", "ud": "up"},
        )

        # please add some check logic here by yourself
        # ...
