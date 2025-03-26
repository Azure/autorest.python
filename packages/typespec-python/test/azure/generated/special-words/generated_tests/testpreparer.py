# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from specialwords import SpecialWordsClient


class SpecialWordsClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(SpecialWordsClient)
        return self.create_client_from_credential(
            SpecialWordsClient,
            credential=credential,
            endpoint=endpoint,
        )


SpecialWordsPreparer = functools.partial(
    PowerShellPreparer, "specialwords", specialwords_endpoint="https://fake_specialwords_endpoint.com"
)
