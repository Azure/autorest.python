# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import OptionalPreparer
from testpreparer_async import OptionalClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestOptionalUnionFloatLiteralOperationsAsync(OptionalClientTestBaseAsync):
    @OptionalPreparer()
    @recorded_by_proxy_async
    async def test_get_all(self, optional_endpoint):
        client = self.create_async_client(endpoint=optional_endpoint)
        response = client.union_float_literal.get_all()

        # please add some check logic here by yourself

    @OptionalPreparer()
    @recorded_by_proxy_async
    async def test_get_default(self, optional_endpoint):
        client = self.create_async_client(endpoint=optional_endpoint)
        response = client.union_float_literal.get_default()

        # please add some check logic here by yourself

    @OptionalPreparer()
    @recorded_by_proxy_async
    async def test_put_all(self, optional_endpoint):
        client = self.create_async_client(endpoint=optional_endpoint)
        response = client.union_float_literal.put_all(
            body={"property": 1.2},
        )

        # please add some check logic here by yourself

    @OptionalPreparer()
    @recorded_by_proxy_async
    async def test_put_default(self, optional_endpoint):
        client = self.create_async_client(endpoint=optional_endpoint)
        response = client.union_float_literal.put_default(
            body={"property": 1.2},
        )

        # please add some check logic here by yourself
