# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import RoutesClientTestBase, RoutesPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRoutes(RoutesClientTestBase):
    @RoutesPreparer()
    @recorded_by_proxy
    def test_fixed(self, routes_endpoint):
        client = self.create_client(endpoint=routes_endpoint)
        response = client.fixed()

        # please add some check logic here by yourself
        # ...
