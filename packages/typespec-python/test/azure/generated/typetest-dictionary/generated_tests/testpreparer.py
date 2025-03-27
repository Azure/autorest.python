# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from typetest.dictionary import DictionaryClient


class DictionaryClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(DictionaryClient)
        return self.create_client_from_credential(
            DictionaryClient,
            credential=credential,
            endpoint=endpoint,
        )


DictionaryPreparer = functools.partial(
    PowerShellPreparer, "dictionary", dictionary_endpoint="https://fake_dictionary_endpoint.com"
)
