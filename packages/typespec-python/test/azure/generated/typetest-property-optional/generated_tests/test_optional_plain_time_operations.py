# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import OptionalClientTestBase, OptionalPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestOptionalPlainTimeOperations(OptionalClientTestBase):
    @OptionalPreparer()
    @recorded_by_proxy
    def test_plain_time_get_all(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.plain_time.get_all()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_plain_time_get_default(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.plain_time.get_default()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_plain_time_put_all(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.plain_time.put_all(
            body={"property": "12:30:00"},
        )

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_plain_time_put_default(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.plain_time.put_default(
            body={"property": "12:30:00"},
        )

        # please add some check logic here by yourself
        # ...
