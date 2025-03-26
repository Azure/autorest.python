# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import CustomClientTestBase, CustomPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestCustom(CustomClientTestBase):
    @CustomPreparer()
    @recorded_by_proxy
    def test_valid(self, custom_endpoint):
        client = self.create_client(endpoint=custom_endpoint)
        response = client.valid()

        # please add some check logic here by yourself
        # ...

    @CustomPreparer()
    @recorded_by_proxy
    def test_invalid(self, custom_endpoint):
        client = self.create_client(endpoint=custom_endpoint)
        response = client.invalid()

        # please add some check logic here by yourself
        # ...
