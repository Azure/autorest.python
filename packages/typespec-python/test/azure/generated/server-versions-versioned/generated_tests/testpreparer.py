# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from server.versions.versioned import VersionedClient


class VersionedClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(VersionedClient)
        return self.create_client_from_credential(
            VersionedClient,
            credential=credential,
            endpoint=endpoint,
        )


VersionedPreparer = functools.partial(
    PowerShellPreparer, "versioned", versioned_endpoint="https://fake_versioned_endpoint.com"
)
