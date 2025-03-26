# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ServiceClientTestBase, ServicePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestServiceBazOperations(ServiceClientTestBase):
    @ServicePreparer()
    @recorded_by_proxy
    def test_baz_foo_seven(self, service_endpoint):
        client = self.create_client(endpoint=service_endpoint)
        response = client.baz.foo.seven()

        # please add some check logic here by yourself
        # ...
