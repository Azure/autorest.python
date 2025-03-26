# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from versioning.added.aio import AddedClient


class AddedClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(AddedClient, is_async=True)
        return self.create_client_from_credential(
            AddedClient,
            credential=credential,
            endpoint=endpoint,
        )
