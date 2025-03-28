# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import PagePreparer
from testpreparer_async import PageClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestPageTwoModelsAsPageItemOperationsAsync(PageClientTestBaseAsync):
    @PagePreparer()
    @recorded_by_proxy_async
    async def test_two_models_as_page_item_list_first_item(self, page_endpoint):
        client = self.create_async_client(endpoint=page_endpoint)
        response = client.two_models_as_page_item.list_first_item()
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @PagePreparer()
    @recorded_by_proxy_async
    async def test_two_models_as_page_item_list_second_item(self, page_endpoint):
        client = self.create_async_client(endpoint=page_endpoint)
        response = client.two_models_as_page_item.list_second_item()
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
