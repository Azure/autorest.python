# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import DatetimeClientTestBase, DatetimePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDatetimeResponseHeaderOperations(DatetimeClientTestBase):
    @DatetimePreparer()
    @recorded_by_proxy
    def test_response_header_default(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.response_header.default()

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy
    def test_response_header_rfc3339(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.response_header.rfc3339()

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy
    def test_response_header_rfc7231(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.response_header.rfc7231()

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy
    def test_response_header_unix_timestamp(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.response_header.unix_timestamp()

        # please add some check logic here by yourself
        # ...
