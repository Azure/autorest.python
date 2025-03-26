# coding=utf-8
None
import pytest
from azure.resourcemanager.operationtemplates.aio import OperationTemplatesClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestOperationTemplatesLroOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(OperationTemplatesClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_lro_begin_create_or_replace(self, resource_group):
        response = await (
            await self.client.lro.begin_create_or_replace(
                resource_group_name=resource_group.name,
                order_name="str",
                resource={
                    "location": "str",
                    "id": "str",
                    "name": "str",
                    "properties": {"amount": 0, "productId": "str", "provisioningState": "str"},
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
    async def test_lro_begin_export(self, resource_group):
        response = await (
            await self.client.lro.begin_export(
                resource_group_name=resource_group.name,
                order_name="str",
                body={"format": "str"},
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_lro_begin_delete(self, resource_group):
        response = await (
            await self.client.lro.begin_delete(
                resource_group_name=resource_group.name,
                order_name="str",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
