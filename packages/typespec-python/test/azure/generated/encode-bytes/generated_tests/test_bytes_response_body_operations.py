# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import BytesClientTestBase, BytesPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestBytesResponseBodyOperations(BytesClientTestBase):
    @BytesPreparer()
    @recorded_by_proxy
    def test_response_body_default(self, bytes_endpoint):
        client = self.create_client(endpoint=bytes_endpoint)
        response = client.response_body.default()

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy
    def test_response_body_octet_stream(self, bytes_endpoint):
        client = self.create_client(endpoint=bytes_endpoint)
        response = client.response_body.octet_stream()

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy
    def test_response_body_custom_content_type(self, bytes_endpoint):
        client = self.create_client(endpoint=bytes_endpoint)
        response = client.response_body.custom_content_type()

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy
    def test_response_body_base64(self, bytes_endpoint):
        client = self.create_client(endpoint=bytes_endpoint)
        response = client.response_body.base64()

        # please add some check logic here by yourself
        # ...

    @BytesPreparer()
    @recorded_by_proxy
    def test_response_body_base64_url(self, bytes_endpoint):
        client = self.create_client(endpoint=bytes_endpoint)
        response = client.response_body.base64_url()

        # please add some check logic here by yourself
        # ...
