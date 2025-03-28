# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import BytesPreparer
from testpreparer_async import BytesClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestBytesRequestBodyOperationsAsync(BytesClientTestBaseAsync):
    @BytesPreparer()
    @recorded_by_proxy_async
    async def test_request_body_default(self, bytes_endpoint):
        client = self.create_async_client(endpoint=bytes_endpoint)
        response = await client.request_body.default(
            value=bytes("bytes", encoding="utf-8"),
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy_async
    async def test_request_body_octet_stream(self, bytes_endpoint):
        client = self.create_async_client(endpoint=bytes_endpoint)
        response = await client.request_body.octet_stream(
            value=bytes("bytes", encoding="utf-8"),
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy_async
    async def test_request_body_custom_content_type(self, bytes_endpoint):
        client = self.create_async_client(endpoint=bytes_endpoint)
        response = await client.request_body.custom_content_type(
            value=bytes("bytes", encoding="utf-8"),
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy_async
    async def test_request_body_base64(self, bytes_endpoint):
        client = self.create_async_client(endpoint=bytes_endpoint)
        response = await client.request_body.base64(
            value=bytes("bytes", encoding="utf-8"),
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy_async
    async def test_request_body_base64_url(self, bytes_endpoint):
        client = self.create_async_client(endpoint=bytes_endpoint)
        response = await client.request_body.base64_url(
            value=bytes("bytes", encoding="utf-8"),
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...
