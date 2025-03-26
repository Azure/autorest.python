# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from server.path.multiple import MultipleClient


class MultipleClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(MultipleClient)
        return self.create_client_from_credential(
            MultipleClient,
            credential=credential,
            endpoint=endpoint,
        )


MultiplePreparer = functools.partial(
    PowerShellPreparer, "multiple", multiple_endpoint="https://fake_multiple_endpoint.com"
)
