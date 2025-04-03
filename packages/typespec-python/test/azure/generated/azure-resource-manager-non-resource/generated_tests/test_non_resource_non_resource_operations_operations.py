# coding=utf-8
import pytest
from azure.resourcemanager.nonresource import NonResourceClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNonResourceNonResourceOperationsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NonResourceClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_non_resource_operations_get(self, resource_group):
        response = self.client.non_resource_operations.get(
            location="str",
            parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_non_resource_operations_create(self, resource_group):
        response = self.client.non_resource_operations.create(
            location="str",
            parameter="str",
            body={"id": "str", "name": "str", "type": "str"},
        )

        # please add some check logic here by yourself
        # ...
