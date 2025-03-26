# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import CollectionFormatPreparer
from testpreparer_async import CollectionFormatClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestCollectionFormatHeaderOperationsAsync(CollectionFormatClientTestBaseAsync):
    @CollectionFormatPreparer()
    @recorded_by_proxy_async
    async def test_header_csv(self, collectionformat_endpoint):
        client = self.create_async_client(endpoint=collectionformat_endpoint)
        response = await client.header.csv(
            colors=["str"],
        )

        # please add some check logic here by yourself
        # ...
