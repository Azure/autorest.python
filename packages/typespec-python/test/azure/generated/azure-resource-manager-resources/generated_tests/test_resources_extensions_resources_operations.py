# coding=utf-8
import pytest
from azure.resourcemanager.resources import ResourcesClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestResourcesExtensionsResourcesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ResourcesClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_extensions_resources_get(self, resource_group):
        response = self.client.extensions_resources.get(
            resource_uri="str",
            extensions_resource_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_extensions_resources_begin_create_or_update(self, resource_group):
        response = self.client.extensions_resources.begin_create_or_update(
            resource_uri="str",
            extensions_resource_name="str",
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
    def test_extensions_resources_update(self, resource_group):
        response = self.client.extensions_resources.update(
            resource_uri="str",
            extensions_resource_name="str",
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
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_extensions_resources_delete(self, resource_group):
        response = self.client.extensions_resources.delete(
            resource_uri="str",
            extensions_resource_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_extensions_resources_list_by_scope(self, resource_group):
        response = self.client.extensions_resources.list_by_scope(
            resource_uri="str",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
