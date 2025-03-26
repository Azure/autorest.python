# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import JsonlPreparer
from testpreparer_async import JsonlClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestJsonlBasicOperationsAsync(JsonlClientTestBaseAsync):
    @JsonlPreparer()
    @recorded_by_proxy_async
    async def test_basic_send(self, jsonl_endpoint):
        client = self.create_async_client(endpoint=jsonl_endpoint)
        response = await client.basic.send(
            body=bytes("bytes", encoding="utf-8"),
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...

    @JsonlPreparer()
    @recorded_by_proxy_async
    async def test_basic_receive(self, jsonl_endpoint):
        client = self.create_async_client(endpoint=jsonl_endpoint)
        response = await client.basic.receive()

        # please add some check logic here by yourself
        # ...
