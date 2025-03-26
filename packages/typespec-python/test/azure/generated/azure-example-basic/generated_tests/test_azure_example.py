# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import AzureExampleClientTestBase, AzureExamplePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAzureExample(AzureExampleClientTestBase):
    @AzureExamplePreparer()
    @recorded_by_proxy
    def test_basic_action(self, azureexample_endpoint):
        client = self.create_client(endpoint=azureexample_endpoint)
        response = client.basic_action(
            body={
                "stringProperty": "str",
                "arrayProperty": ["str"],
                "modelProperty": {"enumProperty": "str", "float32Property": 0.0, "int32Property": 0},
                "recordProperty": {"str": "str"},
            },
            query_param="str",
            header_param="str",
        )

        # please add some check logic here by yourself
        # ...
