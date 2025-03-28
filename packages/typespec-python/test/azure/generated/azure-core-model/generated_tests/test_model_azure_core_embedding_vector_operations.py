# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ModelClientTestBase, ModelPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestModelAzureCoreEmbeddingVectorOperations(ModelClientTestBase):
    @ModelPreparer()
    @recorded_by_proxy
    def test_azure_core_embedding_vector_get(self, model_endpoint):
        client = self.create_client(endpoint=model_endpoint)
        response = client.azure_core_embedding_vector.get()

        # please add some check logic here by yourself
        # ...

    @ModelPreparer()
    @recorded_by_proxy
    def test_azure_core_embedding_vector_put(self, model_endpoint):
        client = self.create_client(endpoint=model_endpoint)
        response = client.azure_core_embedding_vector.put(
            body=[0],
        )

        # please add some check logic here by yourself
        # ...

    @ModelPreparer()
    @recorded_by_proxy
    def test_azure_core_embedding_vector_post(self, model_endpoint):
        client = self.create_client(endpoint=model_endpoint)
        response = client.azure_core_embedding_vector.post(
            body={"embedding": [0]},
        )

        # please add some check logic here by yourself
        # ...
