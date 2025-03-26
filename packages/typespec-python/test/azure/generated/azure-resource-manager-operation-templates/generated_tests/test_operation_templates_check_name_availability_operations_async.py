# coding=utf-8
import pytest
from azure.resourcemanager.operationtemplates.aio import OperationTemplatesClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestOperationTemplatesCheckNameAvailabilityOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(OperationTemplatesClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_check_name_availability_check_global(self, resource_group):
        response = await self.client.check_name_availability.check_global(
            body={"name": "str", "type": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_check_name_availability_check_local(self, resource_group):
        response = await self.client.check_name_availability.check_local(
            location="str",
            body={"name": "str", "type": "str"},
        )

        # please add some check logic here by yourself
        # ...
