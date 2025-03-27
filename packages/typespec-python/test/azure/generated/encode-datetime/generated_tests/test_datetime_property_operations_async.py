# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import DatetimePreparer
from testpreparer_async import DatetimeClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDatetimePropertyOperationsAsync(DatetimeClientTestBaseAsync):
    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_property_default(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.property.default(
            body={"value": "2020-02-20 00:00:00"},
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_property_rfc3339(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.property.rfc3339(
            body={"value": "2020-02-20 00:00:00"},
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_property_rfc7231(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.property.rfc7231(
            body={"value": "2020-02-20 00:00:00"},
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_property_unix_timestamp(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.property.unix_timestamp(
            body={"value": "2020-02-20 00:00:00"},
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_property_unix_timestamp_array(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.property.unix_timestamp_array(
            body={"value": ["2020-02-20 00:00:00"]},
        )

        # please add some check logic here by yourself
        # ...
