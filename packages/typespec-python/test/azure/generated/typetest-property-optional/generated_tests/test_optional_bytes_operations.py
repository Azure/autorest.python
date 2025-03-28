# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import OptionalClientTestBase, OptionalPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestOptionalBytesOperations(OptionalClientTestBase):
    @OptionalPreparer()
    @recorded_by_proxy
    def test_bytes_get_all(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.bytes.get_all()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_bytes_get_default(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.bytes.get_default()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_bytes_put_all(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.bytes.put_all(
            body={"property": bytes("bytes", encoding="utf-8")},
        )

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_bytes_put_default(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.bytes.put_default(
            body={"property": bytes("bytes", encoding="utf-8")},
        )

        # please add some check logic here by yourself
        # ...
