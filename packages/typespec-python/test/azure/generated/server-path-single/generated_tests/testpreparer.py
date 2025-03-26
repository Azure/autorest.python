# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from server.path.single import SingleClient


class SingleClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(SingleClient)
        return self.create_client_from_credential(
            SingleClient,
            credential=credential,
            endpoint=endpoint,
        )


SinglePreparer = functools.partial(PowerShellPreparer, "single", single_endpoint="https://fake_single_endpoint.com")
