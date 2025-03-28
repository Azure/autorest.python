# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ScalarClientTestBase, ScalarPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestScalarAzureLocationScalarOperations(ScalarClientTestBase):
    @ScalarPreparer()
    @recorded_by_proxy
    def test_azure_location_scalar_get(self, scalar_endpoint):
        client = self.create_client(endpoint=scalar_endpoint)
        response = client.azure_location_scalar.get()

        # please add some check logic here by yourself
        # ...

    @ScalarPreparer()
    @recorded_by_proxy
    def test_azure_location_scalar_put(self, scalar_endpoint):
        client = self.create_client(endpoint=scalar_endpoint)
        response = client.azure_location_scalar.put(
            body="str",
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...

    @ScalarPreparer()
    @recorded_by_proxy
    def test_azure_location_scalar_post(self, scalar_endpoint):
        client = self.create_client(endpoint=scalar_endpoint)
        response = client.azure_location_scalar.post(
            body={"location": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @ScalarPreparer()
    @recorded_by_proxy
    def test_azure_location_scalar_header(self, scalar_endpoint):
        client = self.create_client(endpoint=scalar_endpoint)
        response = client.azure_location_scalar.header(
            region="str",
        )

        # please add some check logic here by yourself
        # ...

    @ScalarPreparer()
    @recorded_by_proxy
    def test_azure_location_scalar_query(self, scalar_endpoint):
        client = self.create_client(endpoint=scalar_endpoint)
        response = client.azure_location_scalar.query(
            region="str",
        )

        # please add some check logic here by yourself
        # ...
