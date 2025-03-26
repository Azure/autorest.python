# coding=utf-8
from client.naming.aio import NamingClient
from devtools_testutils import AzureRecordedTestCase


class NamingClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(NamingClient, is_async=True)
        return self.create_client_from_credential(
            NamingClient,
            credential=credential,
            endpoint=endpoint,
        )
