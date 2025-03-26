# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import RpcPreparer
from testpreparer_async import RpcClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRpcAsync(RpcClientTestBaseAsync):
    @RpcPreparer()
    @recorded_by_proxy_async
    async def test_begin_long_running_rpc(self, rpc_endpoint):
        client = self.create_async_client(endpoint=rpc_endpoint)
        response = await (
            await client.begin_long_running_rpc(
                body={"prompt": "str"},
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
