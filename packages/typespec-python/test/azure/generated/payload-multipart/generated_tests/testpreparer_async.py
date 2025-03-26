# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from payload.multipart.aio import MultiPartClient


class MultiPartClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(MultiPartClient, is_async=True)
        return self.create_client_from_credential(
            MultiPartClient,
            credential=credential,
            endpoint=endpoint,
        )
