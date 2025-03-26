# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import BytesClientTestBase, BytesPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestBytesHeaderOperations(BytesClientTestBase):
    @BytesPreparer()
    @recorded_by_proxy
    def test_header_default(self, bytes_endpoint):
        client = self.create_client(endpoint=bytes_endpoint)
        response = client.header.default(
            value=bytes("bytes", encoding="utf-8"),
        )

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy
    def test_header_base64(self, bytes_endpoint):
        client = self.create_client(endpoint=bytes_endpoint)
        response = client.header.base64(
            value=bytes("bytes", encoding="utf-8"),
        )

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy
    def test_header_base64_url(self, bytes_endpoint):
        client = self.create_client(endpoint=bytes_endpoint)
        response = client.header.base64_url(
            value=bytes("bytes", encoding="utf-8"),
        )

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy
    def test_header_base64_url_array(self, bytes_endpoint):
        client = self.create_client(endpoint=bytes_endpoint)
        response = client.header.base64_url_array(
            value=[bytes("bytes", encoding="utf-8")],
        )

        # please add some check logic here by yourself
        # ...
