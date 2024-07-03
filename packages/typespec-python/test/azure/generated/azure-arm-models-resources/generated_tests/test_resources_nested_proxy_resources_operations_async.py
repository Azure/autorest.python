# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.arm.models.resources.aio import ResourcesClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestResourcesNestedProxyResourcesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ResourcesClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.nested_proxy_resources.get(
            resource_group_name=resource_group.name,
            top_level_tracked_resource_name="str",
            nexted_proxy_resource_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create_or_replace(self, resource_group):
        response = await (
            await self.client.nested_proxy_resources.begin_create_or_replace(
                resource_group_name=resource_group.name,
                top_level_tracked_resource_name="str",
                nexted_proxy_resource_name="str",
                resource={
                    "id": "str",
                    "name": "str",
                    "properties": {"description": "str", "provisioningState": "str"},
                    "systemData": {
                        "createdAt": "2020-02-20 00:00:00",
                        "createdBy": "str",
                        "createdByType": "str",
                        "lastModifiedAt": "2020-02-20 00:00:00",
                        "lastModifiedBy": "str",
                        "lastModifiedByType": "str",
                    },
                    "type": "str",
                },
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_update(self, resource_group):
        response = await (
            await self.client.nested_proxy_resources.begin_update(
                resource_group_name=resource_group.name,
                top_level_tracked_resource_name="str",
                nexted_proxy_resource_name="str",
                properties={"properties": {"description": "str"}},
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.nested_proxy_resources.begin_delete(
                resource_group_name=resource_group.name,
                top_level_tracked_resource_name="str",
                nexted_proxy_resource_name="str",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_top_level_tracked_resource(self, resource_group):
        response = self.client.nested_proxy_resources.list_by_top_level_tracked_resource(
            resource_group_name=resource_group.name,
            top_level_tracked_resource_name="str",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
