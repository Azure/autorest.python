# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from server.versions.versioned.aio import VersionedClient


class VersionedClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(VersionedClient, is_async=True)
        return self.create_client_from_credential(
            VersionedClient,
            credential=credential,
            endpoint=endpoint,
        )
