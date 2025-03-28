# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import NumericClientTestBase, NumericPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNumericPropertyOperations(NumericClientTestBase):
    @NumericPreparer()
    @recorded_by_proxy
    def test_property_safeint_as_string(self, numeric_endpoint):
        client = self.create_client(endpoint=numeric_endpoint)
        response = client.property.safeint_as_string(
            value={"value": 0},
        )

        # please add some check logic here by yourself
        # ...

    @NumericPreparer()
    @recorded_by_proxy
    def test_property_uint32_as_string_optional(self, numeric_endpoint):
        client = self.create_client(endpoint=numeric_endpoint)
        response = client.property.uint32_as_string_optional(
            value={"value": 0},
        )

        # please add some check logic here by yourself
        # ...

    @NumericPreparer()
    @recorded_by_proxy
    def test_property_uint8_as_string(self, numeric_endpoint):
        client = self.create_client(endpoint=numeric_endpoint)
        response = client.property.uint8_as_string(
            value={"value": 0},
        )

        # please add some check logic here by yourself
        # ...
