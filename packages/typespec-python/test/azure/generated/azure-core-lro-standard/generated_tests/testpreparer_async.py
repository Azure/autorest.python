# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from specs.azure.core.lro.standard.aio import StandardClient


class StandardClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(StandardClient, is_async=True)
        return self.create_client_from_credential(
            StandardClient,
            credential=credential,
            endpoint=endpoint,
        )
