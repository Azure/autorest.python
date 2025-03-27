# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from specs.azure.core.lro.rpc import RpcClient


class RpcClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(RpcClient)
        return self.create_client_from_credential(
            RpcClient,
            credential=credential,
            endpoint=endpoint,
        )


RpcPreparer = functools.partial(PowerShellPreparer, "rpc", rpc_endpoint="https://fake_rpc_endpoint.com")
