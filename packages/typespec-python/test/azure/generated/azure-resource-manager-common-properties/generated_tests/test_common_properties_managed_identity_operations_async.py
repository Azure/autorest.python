# coding=utf-8
import pytest
from azure.resourcemanager.commonproperties.aio import CommonPropertiesClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestCommonPropertiesManagedIdentityOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(CommonPropertiesClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_managed_identity_get(self, resource_group):
        response = await self.client.managed_identity.get(
            resource_group_name=resource_group.name,
            managed_identity_tracked_resource_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_managed_identity_create_with_system_assigned(self, resource_group):
        response = await self.client.managed_identity.create_with_system_assigned(
            resource_group_name=resource_group.name,
            managed_identity_tracked_resource_name="str",
            resource={
                "location": "str",
                "id": "str",
                "identity": {
                    "type": "str",
                    "principalId": "str",
                    "tenantId": "str",
                    "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                },
                "name": "str",
                "properties": {"provisioningState": "str"},
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
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_managed_identity_update_with_user_assigned_and_system_assigned(self, resource_group):
        response = await self.client.managed_identity.update_with_user_assigned_and_system_assigned(
            resource_group_name=resource_group.name,
            managed_identity_tracked_resource_name="str",
            properties={
                "location": "str",
                "id": "str",
                "identity": {
                    "type": "str",
                    "principalId": "str",
                    "tenantId": "str",
                    "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                },
                "name": "str",
                "properties": {"provisioningState": "str"},
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
        )

        # please add some check logic here by yourself
        # ...
