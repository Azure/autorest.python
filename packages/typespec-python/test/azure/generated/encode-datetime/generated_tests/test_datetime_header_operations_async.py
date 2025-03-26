# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import DatetimePreparer
from testpreparer_async import DatetimeClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDatetimeHeaderOperationsAsync(DatetimeClientTestBaseAsync):
    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_header_default(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.header.default(
            value="2020-02-20 00:00:00",
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_header_rfc3339(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.header.rfc3339(
            value="2020-02-20 00:00:00",
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_header_rfc7231(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.header.rfc7231(
            value="2020-02-20 00:00:00",
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_header_unix_timestamp(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.header.unix_timestamp(
            value="2020-02-20 00:00:00",
        )

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_header_unix_timestamp_array(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.header.unix_timestamp_array(
            value=["2020-02-20 00:00:00"],
        )

        # please add some check logic here by yourself
        # ...
