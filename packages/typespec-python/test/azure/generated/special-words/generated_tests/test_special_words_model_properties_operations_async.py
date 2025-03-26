# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import SpecialWordsPreparer
from testpreparer_async import SpecialWordsClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSpecialWordsModelPropertiesOperationsAsync(SpecialWordsClientTestBaseAsync):
    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_model_properties_same_as_model(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.model_properties.same_as_model(
            body={"SameAsModel": "str"},
        )

        # please add some check logic here by yourself
        # ...
