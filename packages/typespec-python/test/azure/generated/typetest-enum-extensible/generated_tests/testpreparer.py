# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from typetest.enum.extensible import ExtensibleClient


class ExtensibleClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(ExtensibleClient)
        return self.create_client_from_credential(
            ExtensibleClient,
            credential=credential,
            endpoint=endpoint,
        )


ExtensiblePreparer = functools.partial(
    PowerShellPreparer, "extensible", extensible_endpoint="https://fake_extensible_endpoint.com"
)
