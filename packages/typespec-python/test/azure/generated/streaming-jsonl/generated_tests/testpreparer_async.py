# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from streaming.jsonl.aio import JsonlClient


class JsonlClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(JsonlClient, is_async=True)
        return self.create_client_from_credential(
            JsonlClient,
            credential=credential,
            endpoint=endpoint,
        )
