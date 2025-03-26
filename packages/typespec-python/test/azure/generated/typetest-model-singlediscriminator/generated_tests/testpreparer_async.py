# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from typetest.model.singlediscriminator.aio import SingleDiscriminatorClient


class SingleDiscriminatorClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(SingleDiscriminatorClient, is_async=True)
        return self.create_client_from_credential(
            SingleDiscriminatorClient,
            credential=credential,
            endpoint=endpoint,
        )
