# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from typetest.enum.extensible.aio import ExtensibleClient


class ExtensibleClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(ExtensibleClient, is_async=True)
        return self.create_client_from_credential(
            ExtensibleClient,
            credential=credential,
            endpoint=endpoint,
        )
