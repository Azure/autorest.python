# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.resourcemanager.models.resources import ResourcesClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestResourcesTopLevelTrackedResourcesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ResourcesClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_top_level_tracked_resources_get(self, resource_group):
        response = self.client.top_level_tracked_resources.get(
            resource_group_name=resource_group.name,
            top_level_tracked_resource_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_top_level_tracked_resources_begin_create_or_replace(self, resource_group):
        response = self.client.top_level_tracked_resources.begin_create_or_replace(
            resource_group_name=resource_group.name,
            top_level_tracked_resource_name="str",
            resource={
                "location": "str",
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
                "tags": {"str": "str"},
                "type": "str",
            },
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_top_level_tracked_resources_begin_update(self, resource_group):
        response = self.client.top_level_tracked_resources.begin_update(
            resource_group_name=resource_group.name,
            top_level_tracked_resource_name="str",
            properties={
                "location": "str",
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
                "tags": {"str": "str"},
                "type": "str",
            },
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_top_level_tracked_resources_begin_delete(self, resource_group):
        response = self.client.top_level_tracked_resources.begin_delete(
            resource_group_name=resource_group.name,
            top_level_tracked_resource_name="str",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_top_level_tracked_resources_list_by_resource_group(self, resource_group):
        response = self.client.top_level_tracked_resources.list_by_resource_group(
            resource_group_name=resource_group.name,
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_top_level_tracked_resources_list_by_subscription(self, resource_group):
        response = self.client.top_level_tracked_resources.list_by_subscription()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_top_level_tracked_resources_action_sync(self, resource_group):
        response = self.client.top_level_tracked_resources.action_sync(
            resource_group_name=resource_group.name,
            top_level_tracked_resource_name="str",
            body={"message": "str", "urgent": bool},
        )

        # please add some check logic here by yourself
        # ...
