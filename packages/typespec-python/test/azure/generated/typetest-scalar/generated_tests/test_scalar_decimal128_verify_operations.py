# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ScalarClientTestBase, ScalarPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestScalarDecimal128VerifyOperations(ScalarClientTestBase):
    @ScalarPreparer()
    @recorded_by_proxy
    def test_decimal128_verify_prepare_verify(self, scalar_endpoint):
        client = self.create_client(endpoint=scalar_endpoint)
        response = client.decimal128_verify.prepare_verify()

        # please add some check logic here by yourself
        # ...

    @ScalarPreparer()
    @recorded_by_proxy
    def test_decimal128_verify_verify(self, scalar_endpoint):
        client = self.create_client(endpoint=scalar_endpoint)
        response = client.decimal128_verify.verify(
            body=0.0,
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...
