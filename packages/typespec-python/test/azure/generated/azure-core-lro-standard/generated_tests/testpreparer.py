# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from specs.azure.core.lro.standard import StandardClient


class StandardClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(StandardClient)
        return self.create_client_from_credential(
            StandardClient,
            credential=credential,
            endpoint=endpoint,
        )


StandardPreparer = functools.partial(
    PowerShellPreparer, "standard", standard_endpoint="https://fake_standard_endpoint.com"
)
