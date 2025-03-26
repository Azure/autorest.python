# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import JsonlClientTestBase, JsonlPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestJsonlBasicOperations(JsonlClientTestBase):
    @JsonlPreparer()
    @recorded_by_proxy
    def test_basic_send(self, jsonl_endpoint):
        client = self.create_client(endpoint=jsonl_endpoint)
        response = client.basic.send(
            body=bytes("bytes", encoding="utf-8"),
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...

    @JsonlPreparer()
    @recorded_by_proxy
    def test_basic_receive(self, jsonl_endpoint):
        client = self.create_client(endpoint=jsonl_endpoint)
        response = client.basic.receive()

        # please add some check logic here by yourself
        # ...
