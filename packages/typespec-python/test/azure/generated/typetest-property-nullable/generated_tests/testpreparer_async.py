# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from typetest.property.nullable.aio import NullableClient


class NullableClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(NullableClient, is_async=True)
        return self.create_client_from_credential(
            NullableClient,
            credential=credential,
            endpoint=endpoint,
        )
