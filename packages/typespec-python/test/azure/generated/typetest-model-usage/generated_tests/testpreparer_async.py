# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from typetest.model.usage.aio import UsageClient


class UsageClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(UsageClient, is_async=True)
        return self.create_client_from_credential(
            UsageClient,
            credential=credential,
            endpoint=endpoint,
        )
