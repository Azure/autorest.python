# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from specs.azure.core.page.aio import PageClient


class PageClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(PageClient, is_async=True)
        return self.create_client_from_credential(
            PageClient,
            credential=credential,
            endpoint=endpoint,
        )
