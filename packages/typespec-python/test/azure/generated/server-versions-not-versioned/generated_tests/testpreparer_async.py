# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from server.versions.notversioned.aio import NotVersionedClient


class NotVersionedClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(NotVersionedClient, is_async=True)
        return self.create_client_from_credential(
            NotVersionedClient,
            credential=credential,
            endpoint=endpoint,
        )
