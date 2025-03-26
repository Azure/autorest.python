# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from specs.azure.clientgenerator.core.access.aio import AccessClient


class AccessClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(AccessClient, is_async=True)
        return self.create_client_from_credential(
            AccessClient,
            credential=credential,
            endpoint=endpoint,
        )
