# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import BytesPreparer
from testpreparer_async import BytesClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestBytesPropertyOperationsAsync(BytesClientTestBaseAsync):
    @BytesPreparer()
    @recorded_by_proxy_async
    async def test_property_default(self, bytes_endpoint):
        client = self.create_async_client(endpoint=bytes_endpoint)
        response = await client.property.default(
            body={"value": bytes("bytes", encoding="utf-8")},
        )

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy_async
    async def test_property_base64(self, bytes_endpoint):
        client = self.create_async_client(endpoint=bytes_endpoint)
        response = await client.property.base64(
            body={"value": bytes("bytes", encoding="utf-8")},
        )

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy_async
    async def test_property_base64_url(self, bytes_endpoint):
        client = self.create_async_client(endpoint=bytes_endpoint)
        response = await client.property.base64_url(
            body={"value": bytes("bytes", encoding="utf-8")},
        )

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy_async
    async def test_property_base64_url_array(self, bytes_endpoint):
        client = self.create_async_client(endpoint=bytes_endpoint)
        response = await client.property.base64_url_array(
            body={"value": [bytes("bytes", encoding="utf-8")]},
        )

        # please add some check logic here by yourself
        # ...
