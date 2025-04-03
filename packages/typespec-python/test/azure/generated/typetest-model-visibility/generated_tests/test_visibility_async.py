# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import VisibilityPreparer
from testpreparer_async import VisibilityClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestVisibilityAsync(VisibilityClientTestBaseAsync):
    @VisibilityPreparer()
    @recorded_by_proxy_async
    async def test_get_model(self, visibility_endpoint):
        client = self.create_async_client(endpoint=visibility_endpoint)
        response = await client.get_model(
            input={"createProp": ["str"], "deleteProp": bool, "readProp": "str", "updateProp": [0]},
            query_prop=0,
        )

        # please add some check logic here by yourself
        # ...

    @VisibilityPreparer()
    @recorded_by_proxy_async
    async def test_head_model(self, visibility_endpoint):
        client = self.create_async_client(endpoint=visibility_endpoint)
        response = await client.head_model(
            input={"createProp": ["str"], "deleteProp": bool, "readProp": "str", "updateProp": [0]},
            query_prop=0,
        )

        # please add some check logic here by yourself
        # ...

    @VisibilityPreparer()
    @recorded_by_proxy_async
    async def test_put_model(self, visibility_endpoint):
        client = self.create_async_client(endpoint=visibility_endpoint)
        response = await client.put_model(
            input={"createProp": ["str"], "deleteProp": bool, "readProp": "str", "updateProp": [0]},
        )

        # please add some check logic here by yourself
        # ...

    @VisibilityPreparer()
    @recorded_by_proxy_async
    async def test_patch_model(self, visibility_endpoint):
        client = self.create_async_client(endpoint=visibility_endpoint)
        response = await client.patch_model(
            input={"createProp": ["str"], "deleteProp": bool, "readProp": "str", "updateProp": [0]},
        )

        # please add some check logic here by yourself
        # ...

    @VisibilityPreparer()
    @recorded_by_proxy_async
    async def test_post_model(self, visibility_endpoint):
        client = self.create_async_client(endpoint=visibility_endpoint)
        response = await client.post_model(
            input={"createProp": ["str"], "deleteProp": bool, "readProp": "str", "updateProp": [0]},
        )

        # please add some check logic here by yourself
        # ...

    @VisibilityPreparer()
    @recorded_by_proxy_async
    async def test_delete_model(self, visibility_endpoint):
        client = self.create_async_client(endpoint=visibility_endpoint)
        response = await client.delete_model(
            input={"createProp": ["str"], "deleteProp": bool, "readProp": "str", "updateProp": [0]},
        )

        # please add some check logic here by yourself
        # ...

    @VisibilityPreparer()
    @recorded_by_proxy_async
    async def test_put_read_only_model(self, visibility_endpoint):
        client = self.create_async_client(endpoint=visibility_endpoint)
        response = await client.put_read_only_model(
            input={"optionalNullableIntList": [0], "optionalStringRecord": {"str": "str"}},
        )

        # please add some check logic here by yourself
        # ...
