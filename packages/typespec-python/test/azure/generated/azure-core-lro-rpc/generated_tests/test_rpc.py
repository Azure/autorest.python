# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import RpcClientTestBase, RpcPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRpc(RpcClientTestBase):
    @RpcPreparer()
    @recorded_by_proxy
    def test_begin_long_running_rpc(self, rpc_endpoint):
        client = self.create_client(endpoint=rpc_endpoint)
        response = client.begin_long_running_rpc(
            body={"prompt": "str"},
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
