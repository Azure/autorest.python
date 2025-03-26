# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from typetest.model.nesteddiscriminator.aio import NestedDiscriminatorClient


class NestedDiscriminatorClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(NestedDiscriminatorClient, is_async=True)
        return self.create_client_from_credential(
            NestedDiscriminatorClient,
            credential=credential,
            endpoint=endpoint,
        )
