# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from specs.azure.clientgenerator.core.access import AccessClient


class AccessClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(AccessClient)
        return self.create_client_from_credential(
            AccessClient,
            credential=credential,
            endpoint=endpoint,
        )


AccessPreparer = functools.partial(PowerShellPreparer, "access", access_endpoint="https://fake_access_endpoint.com")
