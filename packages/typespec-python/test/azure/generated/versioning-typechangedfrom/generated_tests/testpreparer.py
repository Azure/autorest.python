# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from versioning.typechangedfrom import TypeChangedFromClient


class TypeChangedFromClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(TypeChangedFromClient)
        return self.create_client_from_credential(
            TypeChangedFromClient,
            credential=credential,
            endpoint=endpoint,
        )


TypeChangedFromPreparer = functools.partial(
    PowerShellPreparer, "typechangedfrom", typechangedfrom_endpoint="https://fake_typechangedfrom_endpoint.com"
)
