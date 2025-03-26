# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from serialization.encodedname.json.aio import JsonClient


class JsonClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(JsonClient, is_async=True)
        return self.create_client_from_credential(
            JsonClient,
            credential=credential,
            endpoint=endpoint,
        )
