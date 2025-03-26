# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from typetest.model.empty.aio import EmptyClient


class EmptyClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(EmptyClient, is_async=True)
        return self.create_client_from_credential(
            EmptyClient,
            credential=credential,
            endpoint=endpoint,
        )
