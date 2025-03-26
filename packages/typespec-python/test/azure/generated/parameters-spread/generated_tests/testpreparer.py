# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from parameters.spread import SpreadClient


class SpreadClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(SpreadClient)
        return self.create_client_from_credential(
            SpreadClient,
            credential=credential,
            endpoint=endpoint,
        )


SpreadPreparer = functools.partial(PowerShellPreparer, "spread", spread_endpoint="https://fake_spread_endpoint.com")
