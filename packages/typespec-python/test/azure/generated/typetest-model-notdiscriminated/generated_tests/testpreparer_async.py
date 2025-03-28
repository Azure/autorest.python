# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from typetest.model.notdiscriminated.aio import NotDiscriminatedClient


class NotDiscriminatedClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(NotDiscriminatedClient, is_async=True)
        return self.create_client_from_credential(
            NotDiscriminatedClient,
            credential=credential,
            endpoint=endpoint,
        )
