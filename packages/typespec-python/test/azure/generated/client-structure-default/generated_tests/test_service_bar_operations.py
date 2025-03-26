# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ServiceClientTestBase, ServicePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestServiceBarOperations(ServiceClientTestBase):
    @ServicePreparer()
    @recorded_by_proxy
    def test_bar_five(self, service_endpoint):
        client = self.create_client(endpoint=service_endpoint)
        response = client.bar.five()

        # please add some check logic here by yourself
        # ...

    @ServicePreparer()
    @recorded_by_proxy
    def test_bar_six(self, service_endpoint):
        client = self.create_client(endpoint=service_endpoint)
        response = client.bar.six()

        # please add some check logic here by yourself
        # ...
