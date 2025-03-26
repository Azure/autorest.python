# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from specs.azure.example.basic import AzureExampleClient


class AzureExampleClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(AzureExampleClient)
        return self.create_client_from_credential(
            AzureExampleClient,
            credential=credential,
            endpoint=endpoint,
        )


AzureExamplePreparer = functools.partial(
    PowerShellPreparer, "azureexample", azureexample_endpoint="https://fake_azureexample_endpoint.com"
)
