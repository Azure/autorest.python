# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import AzureExamplePreparer
from testpreparer_async import AzureExampleClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAzureExampleAsync(AzureExampleClientTestBaseAsync):
    @AzureExamplePreparer()
    @recorded_by_proxy_async
    async def test_basic_action(self, azureexample_endpoint):
        client = self.create_async_client(endpoint=azureexample_endpoint)
        response = await client.basic_action(
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
