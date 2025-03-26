# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ResiliencyServiceDrivenClientTestBase, ResiliencyServiceDrivenPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestResiliencyServiceDriven(ResiliencyServiceDrivenClientTestBase):
    @ResiliencyServiceDrivenPreparer()
    @recorded_by_proxy
    def test_add_operation(self, resiliencyservicedriven_endpoint):
        client = self.create_client(endpoint=resiliencyservicedriven_endpoint)
        response = client.add_operation()

        # please add some check logic here by yourself
        # ...

    @ResiliencyServiceDrivenPreparer()
    @recorded_by_proxy
    def test_from_none(self, resiliencyservicedriven_endpoint):
        client = self.create_client(endpoint=resiliencyservicedriven_endpoint)
        response = client.from_none()

        # please add some check logic here by yourself
        # ...

    @ResiliencyServiceDrivenPreparer()
    @recorded_by_proxy
    def test_from_one_required(self, resiliencyservicedriven_endpoint):
        client = self.create_client(endpoint=resiliencyservicedriven_endpoint)
        response = client.from_one_required(
            parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @ResiliencyServiceDrivenPreparer()
    @recorded_by_proxy
    def test_from_one_optional(self, resiliencyservicedriven_endpoint):
        client = self.create_client(endpoint=resiliencyservicedriven_endpoint)
        response = client.from_one_optional()

        # please add some check logic here by yourself
        # ...
