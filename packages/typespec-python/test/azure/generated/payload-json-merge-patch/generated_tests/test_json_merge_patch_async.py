# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import JsonMergePatchPreparer
from testpreparer_async import JsonMergePatchClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestJsonMergePatchAsync(JsonMergePatchClientTestBaseAsync):
    @JsonMergePatchPreparer()
    @recorded_by_proxy_async
    async def test_create_resource(self, jsonmergepatch_endpoint):
        client = self.create_async_client(endpoint=jsonmergepatch_endpoint)
        response = await client.create_resource(
            body={
                "name": "str",
                "array": [{"description": "str", "name": "str"}],
                "description": "str",
                "floatValue": 0.0,
                "innerModel": {"description": "str", "name": "str"},
                "intArray": [0],
                "intValue": 0,
                "map": {"str": {"description": "str", "name": "str"}},
            },
        )

        # please add some check logic here by yourself
        # ...

    @JsonMergePatchPreparer()
    @recorded_by_proxy_async
    async def test_update_resource(self, jsonmergepatch_endpoint):
        client = self.create_async_client(endpoint=jsonmergepatch_endpoint)
        response = await client.update_resource(
            body={
                "array": [{"description": "str", "name": "str"}],
                "description": "str",
                "floatValue": 0.0,
                "innerModel": {"description": "str", "name": "str"},
                "intArray": [0],
                "intValue": 0,
                "map": {"str": {"description": "str", "name": "str"}},
            },
        )

        # please add some check logic here by yourself
        # ...

    @JsonMergePatchPreparer()
    @recorded_by_proxy_async
    async def test_update_optional_resource(self, jsonmergepatch_endpoint):
        client = self.create_async_client(endpoint=jsonmergepatch_endpoint)
        response = await client.update_optional_resource()

        # please add some check logic here by yourself
        # ...
