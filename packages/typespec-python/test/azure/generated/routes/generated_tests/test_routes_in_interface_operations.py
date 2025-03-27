# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import RoutesClientTestBase, RoutesPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRoutesInInterfaceOperations(RoutesClientTestBase):
    @RoutesPreparer()
    @recorded_by_proxy
    def test_in_interface_fixed(self, routes_endpoint):
        client = self.create_client(endpoint=routes_endpoint)
        response = client.in_interface.fixed()

        # please add some check logic here by yourself
        # ...
