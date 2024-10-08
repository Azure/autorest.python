# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import ArrayPreparer
from testpreparer_async import ArrayClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestArrayNullableModelValueOperationsAsync(ArrayClientTestBaseAsync):
    @ArrayPreparer()
    @recorded_by_proxy_async
    async def test_nullable_model_value_get(self, array_endpoint):
        client = self.create_async_client(endpoint=array_endpoint)
        response = await client.nullable_model_value.get()

        # please add some check logic here by yourself
        # ...

    @ArrayPreparer()
    @recorded_by_proxy_async
    async def test_nullable_model_value_put(self, array_endpoint):
        client = self.create_async_client(endpoint=array_endpoint)
        response = await client.nullable_model_value.put(
            body=[{"property": "str", "children": [...]}],
        )

        # please add some check logic here by yourself
        # ...
