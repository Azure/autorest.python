# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import BodyOptionalityPreparer
from testpreparer_async import BodyOptionalityClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestBodyOptionalityOptionalExplicitOperationsAsync(BodyOptionalityClientTestBaseAsync):
    @BodyOptionalityPreparer()
    @recorded_by_proxy_async
    async def test_optional_explicit_set(self, bodyoptionality_endpoint):
        client = self.create_async_client(endpoint=bodyoptionality_endpoint)
        response = await client.optional_explicit.set()

        # please add some check logic here by yourself
        # ...

    @BodyOptionalityPreparer()
    @recorded_by_proxy_async
    async def test_optional_explicit_omit(self, bodyoptionality_endpoint):
        client = self.create_async_client(endpoint=bodyoptionality_endpoint)
        response = await client.optional_explicit.omit()

        # please add some check logic here by yourself
        # ...
