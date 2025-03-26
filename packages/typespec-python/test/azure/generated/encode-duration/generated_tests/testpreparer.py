# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
from encode.duration import DurationClient
import functools


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
