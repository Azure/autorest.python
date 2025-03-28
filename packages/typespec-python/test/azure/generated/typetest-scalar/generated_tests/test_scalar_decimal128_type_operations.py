# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ScalarClientTestBase, ScalarPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestScalarDecimal128TypeOperations(ScalarClientTestBase):
    @ScalarPreparer()
    @recorded_by_proxy
    def test_decimal128_type_response_body(self, scalar_endpoint):
        client = self.create_client(endpoint=scalar_endpoint)
        response = client.decimal128_type.response_body()

        # please add some check logic here by yourself
        # ...

    @ScalarPreparer()
    @recorded_by_proxy
    def test_decimal128_type_request_body(self, scalar_endpoint):
        client = self.create_client(endpoint=scalar_endpoint)
        response = client.decimal128_type.request_body(
            body=0.0,
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...

    @ScalarPreparer()
    @recorded_by_proxy
    def test_decimal128_type_request_parameter(self, scalar_endpoint):
        client = self.create_client(endpoint=scalar_endpoint)
        response = client.decimal128_type.request_parameter(
            value=0.0,
        )

        # please add some check logic here by yourself
        # ...
