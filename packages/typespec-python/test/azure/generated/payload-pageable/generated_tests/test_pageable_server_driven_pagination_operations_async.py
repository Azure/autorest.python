# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import PageablePreparer
from testpreparer_async import PageableClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestPageableServerDrivenPaginationOperationsAsync(PageableClientTestBaseAsync):
    @PageablePreparer()
    @recorded_by_proxy_async
    async def test_server_driven_pagination_link(self, pageable_endpoint):
        client = self.create_async_client(endpoint=pageable_endpoint)
        response = client.server_driven_pagination.link()
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @PageablePreparer()
    @recorded_by_proxy_async
    async def test_server_driven_pagination_continuation_token_request_query_response_body(self, pageable_endpoint):
        client = self.create_async_client(endpoint=pageable_endpoint)
        response = client.server_driven_pagination.continuation_token.request_query_response_body()
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @PageablePreparer()
    @recorded_by_proxy_async
    async def test_server_driven_pagination_continuation_token_request_header_response_body(self, pageable_endpoint):
        client = self.create_async_client(endpoint=pageable_endpoint)
        response = client.server_driven_pagination.continuation_token.request_header_response_body()
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @PageablePreparer()
    @recorded_by_proxy_async
    async def test_server_driven_pagination_continuation_token_request_query_response_header(self, pageable_endpoint):
        client = self.create_async_client(endpoint=pageable_endpoint)
        response = client.server_driven_pagination.continuation_token.request_query_response_header()
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @PageablePreparer()
    @recorded_by_proxy_async
    async def test_server_driven_pagination_continuation_token_request_header_response_header(self, pageable_endpoint):
        client = self.create_async_client(endpoint=pageable_endpoint)
        response = client.server_driven_pagination.continuation_token.request_header_response_header()
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
