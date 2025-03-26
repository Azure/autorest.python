# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from versioning.removed import RemovedClient


class RemovedClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(RemovedClient)
        return self.create_client_from_credential(
            RemovedClient,
            credential=credential,
            endpoint=endpoint,
        )


RemovedPreparer = functools.partial(PowerShellPreparer, "removed", removed_endpoint="https://fake_removed_endpoint.com")
