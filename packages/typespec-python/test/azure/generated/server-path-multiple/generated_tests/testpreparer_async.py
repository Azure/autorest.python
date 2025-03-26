# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from server.path.multiple.aio import MultipleClient


class MultipleClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(MultipleClient, is_async=True)
        return self.create_client_from_credential(
            MultipleClient,
            credential=credential,
            endpoint=endpoint,
        )
