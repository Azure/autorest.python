# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import PageableClientTestBase, PageablePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestPageableServerDrivenPaginationOperations(PageableClientTestBase):
    @PageablePreparer()
    @recorded_by_proxy
    def test_server_driven_pagination_link(self, pageable_endpoint):
        client = self.create_client(endpoint=pageable_endpoint)
        response = client.server_driven_pagination.link()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @PageablePreparer()
    @recorded_by_proxy
    def test_server_driven_pagination_continuation_token_request_query_response_body(self, pageable_endpoint):
        client = self.create_client(endpoint=pageable_endpoint)
        response = client.server_driven_pagination.continuation_token.request_query_response_body()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @PageablePreparer()
    @recorded_by_proxy
    def test_server_driven_pagination_continuation_token_request_header_response_body(self, pageable_endpoint):
        client = self.create_client(endpoint=pageable_endpoint)
        response = client.server_driven_pagination.continuation_token.request_header_response_body()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @PageablePreparer()
    @recorded_by_proxy
    def test_server_driven_pagination_continuation_token_request_query_response_header(self, pageable_endpoint):
        client = self.create_client(endpoint=pageable_endpoint)
        response = client.server_driven_pagination.continuation_token.request_query_response_header()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @PageablePreparer()
    @recorded_by_proxy
    def test_server_driven_pagination_continuation_token_request_header_response_header(self, pageable_endpoint):
        client = self.create_client(endpoint=pageable_endpoint)
        response = client.server_driven_pagination.continuation_token.request_header_response_header()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
