# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from specs.azure.core.lro.rpc.aio import RpcClient


class RpcClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(RpcClient, is_async=True)
        return self.create_client_from_credential(
            RpcClient,
            credential=credential,
            endpoint=endpoint,
        )
