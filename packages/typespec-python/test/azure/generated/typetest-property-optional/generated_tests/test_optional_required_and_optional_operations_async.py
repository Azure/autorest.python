# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import OptionalPreparer
from testpreparer_async import OptionalClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestOptionalRequiredAndOptionalOperationsAsync(OptionalClientTestBaseAsync):
    @OptionalPreparer()
    @recorded_by_proxy_async
    async def test_required_and_optional_get_all(self, optional_endpoint):
        client = self.create_async_client(endpoint=optional_endpoint)
        response = await client.required_and_optional.get_all()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy_async
    async def test_required_and_optional_get_required_only(self, optional_endpoint):
        client = self.create_async_client(endpoint=optional_endpoint)
        response = await client.required_and_optional.get_required_only()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy_async
    async def test_required_and_optional_put_all(self, optional_endpoint):
        client = self.create_async_client(endpoint=optional_endpoint)
        response = await client.required_and_optional.put_all(
            body={"requiredProperty": 0, "optionalProperty": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy_async
    async def test_required_and_optional_put_required_only(self, optional_endpoint):
        client = self.create_async_client(endpoint=optional_endpoint)
        response = await client.required_and_optional.put_required_only(
            body={"requiredProperty": 0, "optionalProperty": "str"},
        )

        # please add some check logic here by yourself
        # ...
