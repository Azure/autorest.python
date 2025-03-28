# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import NestedDiscriminatorPreparer
from testpreparer_async import NestedDiscriminatorClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNestedDiscriminatorAsync(NestedDiscriminatorClientTestBaseAsync):
    @NestedDiscriminatorPreparer()
    @recorded_by_proxy_async
    async def test_get_model(self, nesteddiscriminator_endpoint):
        client = self.create_async_client(endpoint=nesteddiscriminator_endpoint)
        response = await client.get_model()

        # please add some check logic here by yourself
        # ...

    @NestedDiscriminatorPreparer()
    @recorded_by_proxy_async
    async def test_put_model(self, nesteddiscriminator_endpoint):
        client = self.create_async_client(endpoint=nesteddiscriminator_endpoint)
        response = await client.put_model(
            input={"age": 0, "kind": "salmon", "friends": ["fish"], "hate": {"str": "fish"}, "partner": "fish"},
        )

        # please add some check logic here by yourself
        # ...

    @NestedDiscriminatorPreparer()
    @recorded_by_proxy_async
    async def test_get_recursive_model(self, nesteddiscriminator_endpoint):
        client = self.create_async_client(endpoint=nesteddiscriminator_endpoint)
        response = await client.get_recursive_model()

        # please add some check logic here by yourself
        # ...

    @NestedDiscriminatorPreparer()
    @recorded_by_proxy_async
    async def test_put_recursive_model(self, nesteddiscriminator_endpoint):
        client = self.create_async_client(endpoint=nesteddiscriminator_endpoint)
        response = await client.put_recursive_model(
            input={"age": 0, "kind": "salmon", "friends": ["fish"], "hate": {"str": "fish"}, "partner": "fish"},
        )

        # please add some check logic here by yourself
        # ...

    @NestedDiscriminatorPreparer()
    @recorded_by_proxy_async
    async def test_get_missing_discriminator(self, nesteddiscriminator_endpoint):
        client = self.create_async_client(endpoint=nesteddiscriminator_endpoint)
        response = await client.get_missing_discriminator()

        # please add some check logic here by yourself
        # ...

    @NestedDiscriminatorPreparer()
    @recorded_by_proxy_async
    async def test_get_wrong_discriminator(self, nesteddiscriminator_endpoint):
        client = self.create_async_client(endpoint=nesteddiscriminator_endpoint)
        response = await client.get_wrong_discriminator()

        # please add some check logic here by yourself
        # ...
