# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from versioning.added import AddedClient


class AddedClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(AddedClient)
        return self.create_client_from_credential(
            AddedClient,
            credential=credential,
            endpoint=endpoint,
        )


AddedPreparer = functools.partial(PowerShellPreparer, "added", added_endpoint="https://fake_added_endpoint.com")
