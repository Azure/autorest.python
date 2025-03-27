# coding=utf-8
from authentication.union.aio import UnionClient
from devtools_testutils import AzureRecordedTestCase


class UnionClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(UnionClient, is_async=True)
        return self.create_client_from_credential(
            UnionClient,
            credential=credential,
            endpoint=endpoint,
        )
