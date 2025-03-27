# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from typetest.enum.fixed.aio import FixedClient


class FixedClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(FixedClient, is_async=True)
        return self.create_client_from_credential(
            FixedClient,
            credential=credential,
            endpoint=endpoint,
        )
