# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.spheredpg import AzureSphereClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAzureSphereDeviceGroupsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(AzureSphereClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.device_groups.get(
            resource_group_name=resource_group.name,
            catalog_name="str",
            product_name="str",
            device_group_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.device_groups.begin_create_or_update(
            resource_group_name=resource_group.name,
            catalog_name="str",
            product_name="str",
            device_group_name="str",
            resource={
                "id": "str",
                "name": "str",
                "properties": {
                    "allowCrashDumpsCollection": "str",
                    "description": "str",
                    "hasDeployment": bool,
                    "osFeedType": "str",
                    "provisioningState": "str",
                    "regionalDataBoundary": "str",
                    "updatePolicy": "str",
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
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_update(self, resource_group):
        response = self.client.device_groups.begin_update(
            resource_group_name=resource_group.name,
            catalog_name="str",
            product_name="str",
            device_group_name="str",
            properties={
                "properties": {
                    "allowCrashDumpsCollection": "str",
                    "description": "str",
                    "osFeedType": "str",
                    "regionalDataBoundary": "str",
                    "updatePolicy": "str",
                }
            },
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.device_groups.begin_delete(
            resource_group_name=resource_group.name,
            catalog_name="str",
            product_name="str",
            device_group_name="str",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_product(self, resource_group):
        response = self.client.device_groups.list_by_product(
            resource_group_name=resource_group.name,
            catalog_name="str",
            product_name="str",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_claim_devices(self, resource_group):
        response = self.client.device_groups.begin_claim_devices(
            resource_group_name=resource_group.name,
            catalog_name="str",
            product_name="str",
            device_group_name="str",
            body={"deviceIdentifiers": ["str"]},
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_count_devices(self, resource_group):
        response = self.client.device_groups.count_devices(
            resource_group_name=resource_group.name,
            catalog_name="str",
            product_name="str",
            device_group_name="str",
        )

        # please add some check logic here by yourself
        # ...
