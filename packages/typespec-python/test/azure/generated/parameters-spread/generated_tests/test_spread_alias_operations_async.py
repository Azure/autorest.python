# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft Corporation (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import SpreadPreparer
from testpreparer_async import SpreadClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSpreadAliasOperationsAsync(SpreadClientTestBaseAsync):
    @SpreadPreparer()
    @recorded_by_proxy_async
    async def test_alias_spread_as_request_body(self, spread_endpoint):
        client = self.create_async_client(endpoint=spread_endpoint)
        response = await client.alias.spread_as_request_body(
            body={"name": "str"},
            name="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpreadPreparer()
    @recorded_by_proxy_async
    async def test_alias_spread_parameter_with_inner_model(self, spread_endpoint):
        client = self.create_async_client(endpoint=spread_endpoint)
        response = await client.alias.spread_parameter_with_inner_model(
            id="str",
            body={"name": "str"},
            x_ms_test_header="str",
            name="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpreadPreparer()
    @recorded_by_proxy_async
    async def test_alias_spread_as_request_parameter(self, spread_endpoint):
        client = self.create_async_client(endpoint=spread_endpoint)
        response = await client.alias.spread_as_request_parameter(
            id="str",
            body={"name": "str"},
            x_ms_test_header="str",
            name="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpreadPreparer()
    @recorded_by_proxy_async
    async def test_alias_spread_with_multiple_parameters(self, spread_endpoint):
        client = self.create_async_client(endpoint=spread_endpoint)
        response = await client.alias.spread_with_multiple_parameters(
            id="str",
            body={"requiredIntList": [0], "requiredString": "str", "optionalInt": 0, "optionalStringList": ["str"]},
            x_ms_test_header="str",
            required_string="str",
            required_int_list=[0],
        )

        # please add some check logic here by yourself
        # ...

    @SpreadPreparer()
    @recorded_by_proxy_async
    async def test_alias_spread_parameter_with_inner_alias(self, spread_endpoint):
        client = self.create_async_client(endpoint=spread_endpoint)
        response = await client.alias.spread_parameter_with_inner_alias(
            id="str",
            body={"age": 0, "name": "str"},
            x_ms_test_header="str",
            name="str",
            age=0,
        )

        # please add some check logic here by yourself
        # ...
