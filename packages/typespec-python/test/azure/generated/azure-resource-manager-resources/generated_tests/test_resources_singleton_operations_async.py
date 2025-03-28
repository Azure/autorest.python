# coding=utf-8
import pytest
from azure.resourcemanager.resources.aio import ResourcesClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestResourcesSingletonOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ResourcesClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_singleton_get_by_resource_group(self, resource_group):
        response = await self.client.singleton.get_by_resource_group(
            resource_group_name=resource_group.name,
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_singleton_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.singleton.begin_create_or_update(
                resource_group_name=resource_group.name,
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
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_singleton_update(self, resource_group):
        response = await self.client.singleton.update(
            resource_group_name=resource_group.name,
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
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_singleton_list_by_resource_group(self, resource_group):
        response = self.client.singleton.list_by_resource_group(
            resource_group_name=resource_group.name,
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
