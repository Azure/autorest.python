# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import BodyOptionalityPreparer
from testpreparer_async import BodyOptionalityClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestBodyOptionalityAsync(BodyOptionalityClientTestBaseAsync):
    @BodyOptionalityPreparer()
    @recorded_by_proxy_async
    async def test_required_explicit(self, bodyoptionality_endpoint):
        client = self.create_async_client(endpoint=bodyoptionality_endpoint)
        response = await client.required_explicit(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @BodyOptionalityPreparer()
    @recorded_by_proxy_async
    async def test_required_implicit(self, bodyoptionality_endpoint):
        client = self.create_async_client(endpoint=bodyoptionality_endpoint)
        response = await client.required_implicit(
            body={"name": "str"},
            name="str",
        )

        # please add some check logic here by yourself
        # ...
