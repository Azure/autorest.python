# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from payload.contentnegotiation.aio import ContentNegotiationClient


class ContentNegotiationClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(ContentNegotiationClient, is_async=True)
        return self.create_client_from_credential(
            ContentNegotiationClient,
            credential=credential,
            endpoint=endpoint,
        )
