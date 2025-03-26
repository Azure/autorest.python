# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import DatetimeClientTestBase, DatetimePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDatetimePropertyOperations(DatetimeClientTestBase):
    @DatetimePreparer()
    @recorded_by_proxy
    def test_property_default(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.property.default(
            body={"value": "2020-02-20 00:00:00"},
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy
    def test_property_rfc3339(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.property.rfc3339(
            body={"value": "2020-02-20 00:00:00"},
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy
    def test_property_rfc7231(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.property.rfc7231(
            body={"value": "2020-02-20 00:00:00"},
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy
    def test_property_unix_timestamp(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.property.unix_timestamp(
            body={"value": "2020-02-20 00:00:00"},
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy
    def test_property_unix_timestamp_array(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.property.unix_timestamp_array(
            body={"value": ["2020-02-20 00:00:00"]},
        )

        # please add some check logic here by yourself
        # ...
