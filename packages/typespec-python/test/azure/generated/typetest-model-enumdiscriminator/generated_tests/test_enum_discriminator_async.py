# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import EnumDiscriminatorPreparer
from testpreparer_async import EnumDiscriminatorClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestEnumDiscriminatorAsync(EnumDiscriminatorClientTestBaseAsync):
    @EnumDiscriminatorPreparer()
    @recorded_by_proxy_async
    async def test_get_extensible_model(self, enumdiscriminator_endpoint):
        client = self.create_async_client(endpoint=enumdiscriminator_endpoint)
        response = await client.get_extensible_model()

        # please add some check logic here by yourself
        # ...

    @EnumDiscriminatorPreparer()
    @recorded_by_proxy_async
    async def test_put_extensible_model(self, enumdiscriminator_endpoint):
        client = self.create_async_client(endpoint=enumdiscriminator_endpoint)
        response = await client.put_extensible_model(
            input={"kind": "golden", "weight": 0},
        )

        # please add some check logic here by yourself
        # ...

    @EnumDiscriminatorPreparer()
    @recorded_by_proxy_async
    async def test_get_extensible_model_missing_discriminator(self, enumdiscriminator_endpoint):
        client = self.create_async_client(endpoint=enumdiscriminator_endpoint)
        response = await client.get_extensible_model_missing_discriminator()

        # please add some check logic here by yourself
        # ...

    @EnumDiscriminatorPreparer()
    @recorded_by_proxy_async
    async def test_get_extensible_model_wrong_discriminator(self, enumdiscriminator_endpoint):
        client = self.create_async_client(endpoint=enumdiscriminator_endpoint)
        response = await client.get_extensible_model_wrong_discriminator()

        # please add some check logic here by yourself
        # ...

    @EnumDiscriminatorPreparer()
    @recorded_by_proxy_async
    async def test_get_fixed_model(self, enumdiscriminator_endpoint):
        client = self.create_async_client(endpoint=enumdiscriminator_endpoint)
        response = await client.get_fixed_model()

        # please add some check logic here by yourself
        # ...

    @EnumDiscriminatorPreparer()
    @recorded_by_proxy_async
    async def test_put_fixed_model(self, enumdiscriminator_endpoint):
        client = self.create_async_client(endpoint=enumdiscriminator_endpoint)
        response = await client.put_fixed_model(
            input={"kind": "cobra", "length": 0},
        )

        # please add some check logic here by yourself
        # ...

    @EnumDiscriminatorPreparer()
    @recorded_by_proxy_async
    async def test_get_fixed_model_missing_discriminator(self, enumdiscriminator_endpoint):
        client = self.create_async_client(endpoint=enumdiscriminator_endpoint)
        response = await client.get_fixed_model_missing_discriminator()

        # please add some check logic here by yourself
        # ...

    @EnumDiscriminatorPreparer()
    @recorded_by_proxy_async
    async def test_get_fixed_model_wrong_discriminator(self, enumdiscriminator_endpoint):
        client = self.create_async_client(endpoint=enumdiscriminator_endpoint)
        response = await client.get_fixed_model_wrong_discriminator()

        # please add some check logic here by yourself
        # ...
