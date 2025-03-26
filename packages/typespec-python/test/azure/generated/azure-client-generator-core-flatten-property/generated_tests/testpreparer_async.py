# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from specs.azure.clientgenerator.core.flattenproperty.aio import FlattenPropertyClient


class FlattenPropertyClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(FlattenPropertyClient, is_async=True)
        return self.create_client_from_credential(
            FlattenPropertyClient,
            credential=credential,
            endpoint=endpoint,
        )
