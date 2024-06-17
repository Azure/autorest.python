# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.spheredpg.aio import AzureSphereClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAzureSphereDevicesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(AzureSphereClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.devices.get(
            resource_group_name=resource_group.name,
            catalog_name="str",
            product_name="str",
            device_group_name="str",
            device_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.devices.begin_create_or_update(
                resource_group_name=resource_group.name,
                catalog_name="str",
                product_name="str",
                device_group_name="str",
                device_name="str",
                resource={
                    "id": "str",
                    "name": "str",
                    "properties": {
                        "chipSku": "str",
                        "deviceId": "str",
                        "lastAvailableOsVersion": "str",
                        "lastInstalledOsVersion": "str",
                        "lastOsUpdateUtc": "2020-02-20 00:00:00",
                        "lastUpdateRequestUtc": "2020-02-20 00:00:00",
                        "provisioningState": "str",
                    },
                    "systemData": {
                        "createdAt": "2020-02-20",
                        "createdBy": "str",
                        "createdByType": "str",
                        "lastModifiedAt": "2020-02-20",
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
    async def test_update(self, resource_group):
        response = await self.client.devices.update(
            resource_group_name=resource_group.name,
            catalog_name="str",
            product_name="str",
            device_group_name="str",
            device_name="str",
            properties={"properties": {"deviceGroupId": "str"}},
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.devices.begin_delete(
                resource_group_name=resource_group.name,
                catalog_name="str",
                product_name="str",
                device_group_name="str",
                device_name="str",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_device_group(self, resource_group):
        response = self.client.devices.list_by_device_group(
            resource_group_name=resource_group.name,
            catalog_name="str",
            product_name="str",
            device_group_name="str",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_generate_capability_image(self, resource_group):
        response = await (
            await self.client.devices.begin_generate_capability_image(
                resource_group_name=resource_group.name,
                catalog_name="str",
                product_name="str",
                device_group_name="str",
                device_name="str",
                body={"capabilities": ["str"]},
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
