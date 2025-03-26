# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from server.versions.notversioned import NotVersionedClient


class NotVersionedClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(NotVersionedClient)
        return self.create_client_from_credential(
            NotVersionedClient,
            credential=credential,
            endpoint=endpoint,
        )


NotVersionedPreparer = functools.partial(
    PowerShellPreparer, "notversioned", notversioned_endpoint="https://fake_notversioned_endpoint.com"
)
