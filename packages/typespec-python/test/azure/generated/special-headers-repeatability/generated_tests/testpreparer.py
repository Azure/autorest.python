# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from specialheaders.repeatability import RepeatabilityClient


class RepeatabilityClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(RepeatabilityClient)
        return self.create_client_from_credential(
            RepeatabilityClient,
            credential=credential,
            endpoint=endpoint,
        )


RepeatabilityPreparer = functools.partial(
    PowerShellPreparer, "repeatability", repeatability_endpoint="https://fake_repeatability_endpoint.com"
)
