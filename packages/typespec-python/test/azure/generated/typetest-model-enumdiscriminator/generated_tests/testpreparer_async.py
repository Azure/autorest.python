# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from typetest.model.enumdiscriminator.aio import EnumDiscriminatorClient


class EnumDiscriminatorClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(EnumDiscriminatorClient, is_async=True)
        return self.create_client_from_credential(
            EnumDiscriminatorClient,
            credential=credential,
            endpoint=endpoint,
        )
