# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import RenamedOperationPreparer
from testpreparer_async import RenamedOperationClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRenamedOperationAsync(RenamedOperationClientTestBaseAsync):
    @RenamedOperationPreparer()
    @recorded_by_proxy_async
    async def test_renamed_one(self, renamedoperation_endpoint):
        client = self.create_async_client(endpoint=renamedoperation_endpoint)
        response = await client.renamed_one()

        # please add some check logic here by yourself
        # ...

    @RenamedOperationPreparer()
    @recorded_by_proxy_async
    async def test_renamed_three(self, renamedoperation_endpoint):
        client = self.create_async_client(endpoint=renamedoperation_endpoint)
        response = await client.renamed_three()

        # please add some check logic here by yourself
        # ...

    @RenamedOperationPreparer()
    @recorded_by_proxy_async
    async def test_renamed_five(self, renamedoperation_endpoint):
        client = self.create_async_client(endpoint=renamedoperation_endpoint)
        response = await client.renamed_five()

        # please add some check logic here by yourself
        # ...
