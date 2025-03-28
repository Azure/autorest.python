# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import PagePreparer
from testpreparer_async import PageClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestPageAsync(PageClientTestBaseAsync):
    @PagePreparer()
    @recorded_by_proxy_async
    async def test_list_with_page(self, page_endpoint):
        client = self.create_async_client(endpoint=page_endpoint)
        response = client.list_with_page()
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @PagePreparer()
    @recorded_by_proxy_async
    async def test_list_with_parameters(self, page_endpoint):
        client = self.create_async_client(endpoint=page_endpoint)
        response = client.list_with_parameters(
            body_input={"inputName": "str"},
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @PagePreparer()
    @recorded_by_proxy_async
    async def test_list_with_custom_page_model(self, page_endpoint):
        client = self.create_async_client(endpoint=page_endpoint)
        response = client.list_with_custom_page_model()
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
