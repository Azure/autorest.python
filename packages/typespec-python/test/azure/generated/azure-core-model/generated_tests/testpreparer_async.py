# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from specs.azure.core.model.aio import ModelClient


class ModelClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(ModelClient, is_async=True)
        return self.create_client_from_credential(
            ModelClient,
            credential=credential,
            endpoint=endpoint,
        )
