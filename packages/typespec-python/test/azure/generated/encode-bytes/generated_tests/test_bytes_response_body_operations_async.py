# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import BytesPreparer
from testpreparer_async import BytesClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestBytesResponseBodyOperationsAsync(BytesClientTestBaseAsync):
    @BytesPreparer()
    @recorded_by_proxy_async
    async def test_response_body_default(self, bytes_endpoint):
        client = self.create_async_client(endpoint=bytes_endpoint)
        response = await client.response_body.default()

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy_async
    async def test_response_body_octet_stream(self, bytes_endpoint):
        client = self.create_async_client(endpoint=bytes_endpoint)
        response = await client.response_body.octet_stream()

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy_async
    async def test_response_body_custom_content_type(self, bytes_endpoint):
        client = self.create_async_client(endpoint=bytes_endpoint)
        response = await client.response_body.custom_content_type()

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy_async
    async def test_response_body_base64(self, bytes_endpoint):
        client = self.create_async_client(endpoint=bytes_endpoint)
        response = await client.response_body.base64()

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy_async
    async def test_response_body_base64_url(self, bytes_endpoint):
        client = self.create_async_client(endpoint=bytes_endpoint)
        response = await client.response_body.base64_url()

        # please add some check logic here by yourself
        # ...
