# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from specs.azure.core.scalar import ScalarClient


class ScalarClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(ScalarClient)
        return self.create_client_from_credential(
            ScalarClient,
            credential=credential,
            endpoint=endpoint,
        )


ScalarPreparer = functools.partial(PowerShellPreparer, "scalar", scalar_endpoint="https://fake_scalar_endpoint.com")
