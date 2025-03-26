# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from payload.pageable.aio import PageableClient


class PageableClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(PageableClient, is_async=True)
        return self.create_client_from_credential(
            PageableClient,
            credential=credential,
            endpoint=endpoint,
        )
