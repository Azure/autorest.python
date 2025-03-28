# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import ModelPreparer
from testpreparer_async import ModelClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestModelAzureCoreEmbeddingVectorOperationsAsync(ModelClientTestBaseAsync):
    @ModelPreparer()
    @recorded_by_proxy_async
    async def test_azure_core_embedding_vector_get(self, model_endpoint):
        client = self.create_async_client(endpoint=model_endpoint)
        response = await client.azure_core_embedding_vector.get()

        # please add some check logic here by yourself
        # ...

    @ModelPreparer()
    @recorded_by_proxy_async
    async def test_azure_core_embedding_vector_put(self, model_endpoint):
        client = self.create_async_client(endpoint=model_endpoint)
        response = await client.azure_core_embedding_vector.put(
            body=[0],
        )

        # please add some check logic here by yourself
        # ...

    @ModelPreparer()
    @recorded_by_proxy_async
    async def test_azure_core_embedding_vector_post(self, model_endpoint):
        client = self.create_async_client(endpoint=model_endpoint)
        response = await client.azure_core_embedding_vector.post(
            body={"embedding": [0]},
        )

        # please add some check logic here by yourself
        # ...
