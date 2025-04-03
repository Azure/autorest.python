# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import UsageClientTestBase, UsagePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestUsageModelInOperationOperations(UsageClientTestBase):
    @UsagePreparer()
    @recorded_by_proxy
    def test_model_in_operation_input_to_input_output(self, usage_endpoint):
        client = self.create_client(endpoint=usage_endpoint)
        response = client.model_in_operation.input_to_input_output(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @UsagePreparer()
    @recorded_by_proxy
    def test_model_in_operation_output_to_input_output(self, usage_endpoint):
        client = self.create_client(endpoint=usage_endpoint)
        response = client.model_in_operation.output_to_input_output()

        # please add some check logic here by yourself
        # ...

    @UsagePreparer()
    @recorded_by_proxy
    def test_model_in_operation_model_in_read_only_property(self, usage_endpoint):
        client = self.create_client(endpoint=usage_endpoint)
        response = client.model_in_operation.model_in_read_only_property(
            body={"result": {"name": "str"}},
        )

        # please add some check logic here by yourself
        # ...

    @UsagePreparer()
    @recorded_by_proxy
    def test_model_in_operation_orphan_model_serializable(self, usage_endpoint):
        client = self.create_client(endpoint=usage_endpoint)
        response = client.model_in_operation.orphan_model_serializable(
            body={},
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...
