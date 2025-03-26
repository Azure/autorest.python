# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from specs.azure.encode.duration import DurationClient


class DurationClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(DurationClient)
        return self.create_client_from_credential(
            DurationClient,
            credential=credential,
            endpoint=endpoint,
        )


DurationPreparer = functools.partial(
    PowerShellPreparer, "duration", duration_endpoint="https://fake_duration_endpoint.com"
)
