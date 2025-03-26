# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from specialwords.aio import SpecialWordsClient


class SpecialWordsClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(SpecialWordsClient, is_async=True)
        return self.create_client_from_credential(
            SpecialWordsClient,
            credential=credential,
            endpoint=endpoint,
        )
