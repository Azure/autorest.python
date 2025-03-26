# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from specs.azure.core.traits.aio import TraitsClient


class TraitsClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(TraitsClient, is_async=True)
        return self.create_client_from_credential(
            TraitsClient,
            credential=credential,
            endpoint=endpoint,
        )
