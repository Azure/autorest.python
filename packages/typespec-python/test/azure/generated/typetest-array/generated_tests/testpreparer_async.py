# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from typetest.array.aio import ArrayClient


class ArrayClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(ArrayClient, is_async=True)
        return self.create_client_from_credential(
            ArrayClient,
            credential=credential,
            endpoint=endpoint,
        )
