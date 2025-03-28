# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import DatetimeClientTestBase, DatetimePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDatetimeQueryOperations(DatetimeClientTestBase):
    @DatetimePreparer()
    @recorded_by_proxy
    def test_query_default(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.query.default(
            value="2020-02-20 00:00:00",
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy
    def test_query_rfc3339(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.query.rfc3339(
            value="2020-02-20 00:00:00",
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy
    def test_query_rfc7231(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.query.rfc7231(
            value="2020-02-20 00:00:00",
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy
    def test_query_unix_timestamp(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.query.unix_timestamp(
            value="2020-02-20 00:00:00",
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy
    def test_query_unix_timestamp_array(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.query.unix_timestamp_array(
            value=["2020-02-20 00:00:00"],
        )

        # please add some check logic here by yourself
        # ...
