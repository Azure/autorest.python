# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import BytesPreparer
from testpreparer_async import BytesClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestBytesHeaderOperationsAsync(BytesClientTestBaseAsync):
    @BytesPreparer()
    @recorded_by_proxy_async
    async def test_header_default(self, bytes_endpoint):
        client = self.create_async_client(endpoint=bytes_endpoint)
        response = await client.header.default(
            value=bytes("bytes", encoding="utf-8"),
        )

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy_async
    async def test_header_base64(self, bytes_endpoint):
        client = self.create_async_client(endpoint=bytes_endpoint)
        response = await client.header.base64(
            value=bytes("bytes", encoding="utf-8"),
        )

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy_async
    async def test_header_base64_url(self, bytes_endpoint):
        client = self.create_async_client(endpoint=bytes_endpoint)
        response = await client.header.base64_url(
            value=bytes("bytes", encoding="utf-8"),
        )

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy_async
    async def test_header_base64_url_array(self, bytes_endpoint):
        client = self.create_async_client(endpoint=bytes_endpoint)
        response = await client.header.base64_url_array(
            value=[bytes("bytes", encoding="utf-8")],
        )

        # please add some check logic here by yourself
        # ...
