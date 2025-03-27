# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import DatetimePreparer
from testpreparer_async import DatetimeClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDatetimeResponseHeaderOperationsAsync(DatetimeClientTestBaseAsync):
    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_response_header_default(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.response_header.default()

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_response_header_rfc3339(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.response_header.rfc3339()

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_response_header_rfc7231(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.response_header.rfc7231()

        # please add some check logic here by yourself
        # ...

    @DatetimePreparer()
    @recorded_by_proxy_async
    async def test_response_header_unix_timestamp(self, datetime_endpoint):
        client = self.create_async_client(endpoint=datetime_endpoint)
        response = await client.response_header.unix_timestamp()

        # please add some check logic here by yourself
        # ...
