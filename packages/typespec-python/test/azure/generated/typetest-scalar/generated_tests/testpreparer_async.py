# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from typetest.scalar.aio import ScalarClient


class ScalarClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(ScalarClient, is_async=True)
        return self.create_client_from_credential(
            ScalarClient,
            credential=credential,
            endpoint=endpoint,
        )
