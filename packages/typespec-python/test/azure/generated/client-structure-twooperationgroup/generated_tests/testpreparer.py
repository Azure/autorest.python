# coding=utf-8
None
from client.structure.twooperationgroup import TwoOperationGroupClient
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools


class TwoOperationGroupClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(TwoOperationGroupClient)
        return self.create_client_from_credential(
            TwoOperationGroupClient,
            credential=credential,
            endpoint=endpoint,
        )


TwoOperationGroupPreparer = functools.partial(
    PowerShellPreparer, "twooperationgroup", twooperationgroup_endpoint="https://fake_twooperationgroup_endpoint.com"
)
