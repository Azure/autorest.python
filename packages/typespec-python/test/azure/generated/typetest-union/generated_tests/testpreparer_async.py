# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from typetest.union.aio import UnionClient


class UnionClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(UnionClient, is_async=True)
        return self.create_client_from_credential(
            UnionClient,
            credential=credential,
            endpoint=endpoint,
        )
