# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ServiceClientTestBase, ServicePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestService(ServiceClientTestBase):
    @ServicePreparer()
    @recorded_by_proxy
    def test_one(self, service_endpoint):
        client = self.create_client(endpoint=service_endpoint)
        response = client.one()

        # please add some check logic here by yourself
        # ...

    @ServicePreparer()
    @recorded_by_proxy
    def test_two(self, service_endpoint):
        client = self.create_client(endpoint=service_endpoint)
        response = client.two()

        # please add some check logic here by yourself
        # ...
