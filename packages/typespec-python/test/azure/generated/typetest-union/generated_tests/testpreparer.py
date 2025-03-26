# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from typetest.union import UnionClient


class UnionClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(UnionClient)
        return self.create_client_from_credential(
            UnionClient,
            credential=credential,
            endpoint=endpoint,
        )


UnionPreparer = functools.partial(PowerShellPreparer, "union", union_endpoint="https://fake_union_endpoint.com")
