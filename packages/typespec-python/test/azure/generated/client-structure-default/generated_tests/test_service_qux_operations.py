# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ServiceClientTestBase, ServicePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestServiceQuxOperations(ServiceClientTestBase):
    @ServicePreparer()
    @recorded_by_proxy
    def test_qux_eight(self, service_endpoint):
        client = self.create_client(endpoint=service_endpoint)
        response = client.qux.eight()

        # please add some check logic here by yourself
        # ...

    @ServicePreparer()
    @recorded_by_proxy
    def test_qux_bar_nine(self, service_endpoint):
        client = self.create_client(endpoint=service_endpoint)
        response = client.qux.bar.nine()

        # please add some check logic here by yourself
        # ...
