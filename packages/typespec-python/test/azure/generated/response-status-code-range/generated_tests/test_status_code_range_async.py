# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import StatusCodeRangePreparer
from testpreparer_async import StatusCodeRangeClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestStatusCodeRangeAsync(StatusCodeRangeClientTestBaseAsync):
    @StatusCodeRangePreparer()
    @recorded_by_proxy_async
    async def test_error_response_status_code_in_range(self, statuscoderange_endpoint):
        client = self.create_async_client(endpoint=statuscoderange_endpoint)
        response = await client.error_response_status_code_in_range()

        # please add some check logic here by yourself
        # ...

    @StatusCodeRangePreparer()
    @recorded_by_proxy_async
    async def test_error_response_status_code404(self, statuscoderange_endpoint):
        client = self.create_async_client(endpoint=statuscoderange_endpoint)
        response = await client.error_response_status_code404()

        # please add some check logic here by yourself
        # ...
