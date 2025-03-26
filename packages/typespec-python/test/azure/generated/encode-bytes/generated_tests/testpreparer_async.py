# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from encode.bytes.aio import BytesClient


class BytesClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(BytesClient, is_async=True)
        return self.create_client_from_credential(
            BytesClient,
            credential=credential,
            endpoint=endpoint,
        )
