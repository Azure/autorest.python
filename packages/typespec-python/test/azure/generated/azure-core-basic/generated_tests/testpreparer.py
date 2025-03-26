# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from specs.azure.core.basic import BasicClient


class BasicClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(BasicClient)
        return self.create_client_from_credential(
            BasicClient,
            credential=credential,
            endpoint=endpoint,
        )


BasicPreparer = functools.partial(PowerShellPreparer, "basic", basic_endpoint="https://fake_basic_endpoint.com")
