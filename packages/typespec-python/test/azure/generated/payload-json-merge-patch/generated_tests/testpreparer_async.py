# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from payload.jsonmergepatch.aio import JsonMergePatchClient


class JsonMergePatchClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(JsonMergePatchClient, is_async=True)
        return self.create_client_from_credential(
            JsonMergePatchClient,
            credential=credential,
            endpoint=endpoint,
        )
