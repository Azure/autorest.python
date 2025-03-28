# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import TraitsPreparer
from testpreparer_async import TraitsClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestTraitsAsync(TraitsClientTestBaseAsync):
    @TraitsPreparer()
    @recorded_by_proxy_async
    async def test_smoke_test(self, traits_endpoint):
        client = self.create_async_client(endpoint=traits_endpoint)
        response = await client.smoke_test(
            id=0,
            foo="str",
        )

        # please add some check logic here by yourself
        # ...

    @TraitsPreparer()
    @recorded_by_proxy_async
    async def test_repeatable_action(self, traits_endpoint):
        client = self.create_async_client(endpoint=traits_endpoint)
        response = await client.repeatable_action(
            id=0,
            body={"userActionValue": "str"},
        )

        # please add some check logic here by yourself
        # ...
