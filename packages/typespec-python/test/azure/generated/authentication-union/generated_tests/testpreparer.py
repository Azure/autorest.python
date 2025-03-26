# coding=utf-8
None
from authentication.union import UnionClient
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools


class UnionClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(UnionClient)
        return self.create_client_from_credential(
            UnionClient,
            credential=credential,
            endpoint=endpoint,
        )


UnionPreparer = functools.partial(PowerShellPreparer, "union", union_endpoint="https://fake_union_endpoint.com")
