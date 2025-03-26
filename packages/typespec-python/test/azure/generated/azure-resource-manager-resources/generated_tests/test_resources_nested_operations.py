# coding=utf-8
None
import pytest
from azure.resourcemanager.resources import ResourcesClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestResourcesNestedOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ResourcesClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_nested_get(self, resource_group):
        response = self.client.nested.get(
            resource_group_name=resource_group.name,
            top_level_tracked_resource_name="str",
            nexted_proxy_resource_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_nested_begin_create_or_replace(self, resource_group):
        response = self.client.nested.begin_create_or_replace(
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
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_nested_begin_update(self, resource_group):
        response = self.client.nested.begin_update(
            resource_group_name=resource_group.name,
            top_level_tracked_resource_name="str",
            nexted_proxy_resource_name="str",
            properties={
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
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_nested_begin_delete(self, resource_group):
        response = self.client.nested.begin_delete(
            resource_group_name=resource_group.name,
            top_level_tracked_resource_name="str",
            nexted_proxy_resource_name="str",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_nested_list_by_top_level_tracked_resource(self, resource_group):
        response = self.client.nested.list_by_top_level_tracked_resource(
            resource_group_name=resource_group.name,
            top_level_tracked_resource_name="str",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
