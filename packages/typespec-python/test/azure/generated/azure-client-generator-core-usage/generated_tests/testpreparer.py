# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from specs.azure.clientgenerator.core.usage import UsageClient


class UsageClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(UsageClient)
        return self.create_client_from_credential(
            UsageClient,
            credential=credential,
            endpoint=endpoint,
        )


UsagePreparer = functools.partial(PowerShellPreparer, "usage", usage_endpoint="https://fake_usage_endpoint.com")
