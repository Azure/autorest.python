# coding=utf-8
None
from client.clientnamespace.aio import ClientNamespaceFirstClient
from client.clientnamespace.second.aio import ClientNamespaceSecondClient
from devtools_testutils import AzureRecordedTestCase


class ClientNamespaceFirstClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(ClientNamespaceFirstClient, is_async=True)
        return self.create_client_from_credential(
            ClientNamespaceFirstClient,
            credential=credential,
            endpoint=endpoint,
        )


class ClientNamespaceSecondClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(ClientNamespaceSecondClient, is_async=True)
        return self.create_client_from_credential(
            ClientNamespaceSecondClient,
            credential=credential,
            endpoint=endpoint,
        )
