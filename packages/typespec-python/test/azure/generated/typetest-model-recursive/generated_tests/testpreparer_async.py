# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from typetest.model.recursive.aio import RecursiveClient


class RecursiveClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(RecursiveClient, is_async=True)
        return self.create_client_from_credential(
            RecursiveClient,
            credential=credential,
            endpoint=endpoint,
        )
