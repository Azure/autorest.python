# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from specs.azure.example.basic.aio import AzureExampleClient


class AzureExampleClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(AzureExampleClient, is_async=True)
        return self.create_client_from_credential(
            AzureExampleClient,
            credential=credential,
            endpoint=endpoint,
        )
