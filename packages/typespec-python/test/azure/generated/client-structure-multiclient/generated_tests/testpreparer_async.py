# coding=utf-8
from client.structure.multiclient.aio import ClientAClient, ClientBClient
from devtools_testutils import AzureRecordedTestCase


class ClientAClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(ClientAClient, is_async=True)
        return self.create_client_from_credential(
            ClientAClient,
            credential=credential,
            endpoint=endpoint,
        )


class ClientBClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(ClientBClient, is_async=True)
        return self.create_client_from_credential(
            ClientBClient,
            credential=credential,
            endpoint=endpoint,
        )
