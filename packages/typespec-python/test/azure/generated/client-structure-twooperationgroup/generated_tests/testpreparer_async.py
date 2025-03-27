# coding=utf-8
from client.structure.twooperationgroup.aio import TwoOperationGroupClient
from devtools_testutils import AzureRecordedTestCase


class TwoOperationGroupClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(TwoOperationGroupClient, is_async=True)
        return self.create_client_from_credential(
            TwoOperationGroupClient,
            credential=credential,
            endpoint=endpoint,
        )
