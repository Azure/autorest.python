# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from versioning.renamedfrom import RenamedFromClient


class RenamedFromClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(RenamedFromClient)
        return self.create_client_from_credential(
            RenamedFromClient,
            credential=credential,
            endpoint=endpoint,
        )


RenamedFromPreparer = functools.partial(
    PowerShellPreparer, "renamedfrom", renamedfrom_endpoint="https://fake_renamedfrom_endpoint.com"
)
