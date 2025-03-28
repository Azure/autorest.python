# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import ConditionalRequestPreparer
from testpreparer_async import ConditionalRequestClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestConditionalRequestAsync(ConditionalRequestClientTestBaseAsync):
    @ConditionalRequestPreparer()
    @recorded_by_proxy_async
    async def test_post_if_match(self, conditionalrequest_endpoint):
        client = self.create_async_client(endpoint=conditionalrequest_endpoint)
        response = await client.post_if_match()

        # please add some check logic here by yourself
        # ...

    @ConditionalRequestPreparer()
    @recorded_by_proxy_async
    async def test_post_if_none_match(self, conditionalrequest_endpoint):
        client = self.create_async_client(endpoint=conditionalrequest_endpoint)
        response = await client.post_if_none_match()

        # please add some check logic here by yourself
        # ...

    @ConditionalRequestPreparer()
    @recorded_by_proxy_async
    async def test_head_if_modified_since(self, conditionalrequest_endpoint):
        client = self.create_async_client(endpoint=conditionalrequest_endpoint)
        response = await client.head_if_modified_since()

        # please add some check logic here by yourself
        # ...

    @ConditionalRequestPreparer()
    @recorded_by_proxy_async
    async def test_post_if_unmodified_since(self, conditionalrequest_endpoint):
        client = self.create_async_client(endpoint=conditionalrequest_endpoint)
        response = await client.post_if_unmodified_since()

        # please add some check logic here by yourself
        # ...
