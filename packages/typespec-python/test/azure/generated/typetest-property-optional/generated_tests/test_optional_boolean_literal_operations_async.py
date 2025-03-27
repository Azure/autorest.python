# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import OptionalPreparer
from testpreparer_async import OptionalClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestOptionalBooleanLiteralOperationsAsync(OptionalClientTestBaseAsync):
    @OptionalPreparer()
    @recorded_by_proxy_async
    async def test_boolean_literal_get_all(self, optional_endpoint):
        client = self.create_async_client(endpoint=optional_endpoint)
        response = await client.boolean_literal.get_all()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy_async
    async def test_boolean_literal_get_default(self, optional_endpoint):
        client = self.create_async_client(endpoint=optional_endpoint)
        response = await client.boolean_literal.get_default()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy_async
    async def test_boolean_literal_put_all(self, optional_endpoint):
        client = self.create_async_client(endpoint=optional_endpoint)
        response = await client.boolean_literal.put_all(
            body={"property": True},
        )

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy_async
    async def test_boolean_literal_put_default(self, optional_endpoint):
        client = self.create_async_client(endpoint=optional_endpoint)
        response = await client.boolean_literal.put_default(
            body={"property": True},
        )

        # please add some check logic here by yourself
        # ...
