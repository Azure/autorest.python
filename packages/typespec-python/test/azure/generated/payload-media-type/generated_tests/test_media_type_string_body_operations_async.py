# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import MediaTypePreparer
from testpreparer_async import MediaTypeClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestMediaTypeStringBodyOperationsAsync(MediaTypeClientTestBaseAsync):
    @MediaTypePreparer()
    @recorded_by_proxy_async
    async def test_string_body_send_as_text(self, mediatype_endpoint):
        client = self.create_async_client(endpoint=mediatype_endpoint)
        response = await client.string_body.send_as_text(
            text="str",
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...

    @MediaTypePreparer()
    @recorded_by_proxy_async
    async def test_string_body_get_as_text(self, mediatype_endpoint):
        client = self.create_async_client(endpoint=mediatype_endpoint)
        response = await client.string_body.get_as_text()

        # please add some check logic here by yourself
        # ...

    @MediaTypePreparer()
    @recorded_by_proxy_async
    async def test_string_body_send_as_json(self, mediatype_endpoint):
        client = self.create_async_client(endpoint=mediatype_endpoint)
        response = await client.string_body.send_as_json(
            text="str",
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...

    @MediaTypePreparer()
    @recorded_by_proxy_async
    async def test_string_body_get_as_json(self, mediatype_endpoint):
        client = self.create_async_client(endpoint=mediatype_endpoint)
        response = await client.string_body.get_as_json()

        # please add some check logic here by yourself
        # ...
