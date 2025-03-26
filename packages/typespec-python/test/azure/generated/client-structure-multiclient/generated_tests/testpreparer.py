# coding=utf-8
None
from client.structure.multiclient import ClientAClient, ClientBClient
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools


class ClientAClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(ClientAClient)
        return self.create_client_from_credential(
            ClientAClient,
            credential=credential,
            endpoint=endpoint,
        )


APreparer = functools.partial(PowerShellPreparer, "a", a_endpoint="https://fake_a_endpoint.com")


class ClientBClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(ClientBClient)
        return self.create_client_from_credential(
            ClientBClient,
            credential=credential,
            endpoint=endpoint,
        )


BPreparer = functools.partial(PowerShellPreparer, "b", b_endpoint="https://fake_b_endpoint.com")
