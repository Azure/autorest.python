# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from typetest.dictionary.aio import DictionaryClient


class DictionaryClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(DictionaryClient, is_async=True)
        return self.create_client_from_credential(
            DictionaryClient,
            credential=credential,
            endpoint=endpoint,
        )
