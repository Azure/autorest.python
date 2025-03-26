# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from server.endpoint.notdefined.aio import NotDefinedClient


class NotDefinedClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(NotDefinedClient, is_async=True)
        return self.create_client_from_credential(
            NotDefinedClient,
            credential=credential,
            endpoint=endpoint,
        )
