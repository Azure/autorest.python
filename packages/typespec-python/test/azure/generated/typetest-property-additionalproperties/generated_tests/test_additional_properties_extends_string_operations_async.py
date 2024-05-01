# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import AdditionalPropertiesPreparer
from testpreparer_async import AdditionalPropertiesClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAdditionalPropertiesExtendsStringOperationsAsync(AdditionalPropertiesClientTestBaseAsync):
    @AdditionalPropertiesPreparer()
    @recorded_by_proxy_async
    async def test_get(self, additionalproperties_endpoint):
        client = self.create_async_client(endpoint=additionalproperties_endpoint)
        response = await client.extends_string.get()

        # please add some check logic here by yourself
        # ...

    @AdditionalPropertiesPreparer()
    @recorded_by_proxy_async
    async def test_put(self, additionalproperties_endpoint):
        client = self.create_async_client(endpoint=additionalproperties_endpoint)
        response = await client.extends_string.put(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...
