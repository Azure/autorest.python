# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import DatetimePreparer
from testpreparer_async import DatetimeClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDatetimeQueryOperationsAsync(DatetimeClientTestBaseAsync):
    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_query_default(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.query.default(
            value="2020-02-20 00:00:00",
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_query_rfc3339(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.query.rfc3339(
            value="2020-02-20 00:00:00",
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_query_rfc7231(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.query.rfc7231(
            value="2020-02-20 00:00:00",
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_query_unix_timestamp(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.query.unix_timestamp(
            value="2020-02-20 00:00:00",
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_query_unix_timestamp_array(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.query.unix_timestamp_array(
            value=["2020-02-20 00:00:00"],
        )

        # please add some check logic here by yourself
        # ...
