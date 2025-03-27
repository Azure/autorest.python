# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import UsageClientTestBase, UsagePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestUsage(UsageClientTestBase):
    @UsagePreparer()
    @recorded_by_proxy
    def test_input(self, usage_endpoint):
        client = self.create_client(endpoint=usage_endpoint)
        response = client.input(
            input={"requiredProp": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @UsagePreparer()
    @recorded_by_proxy
    def test_output(self, usage_endpoint):
        client = self.create_client(endpoint=usage_endpoint)
        response = client.output()

        # please add some check logic here by yourself
        # ...

    @UsagePreparer()
    @recorded_by_proxy
    def test_input_and_output(self, usage_endpoint):
        client = self.create_client(endpoint=usage_endpoint)
        response = client.input_and_output(
            body={"requiredProp": "str"},
        )

        # please add some check logic here by yourself
        # ...
