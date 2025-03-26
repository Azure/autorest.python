# coding=utf-8
None
from client.naming import NamingClient
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools


class NamingClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(NamingClient)
        return self.create_client_from_credential(
            NamingClient,
            credential=credential,
            endpoint=endpoint,
        )


NamingPreparer = functools.partial(PowerShellPreparer, "naming", naming_endpoint="https://fake_naming_endpoint.com")
