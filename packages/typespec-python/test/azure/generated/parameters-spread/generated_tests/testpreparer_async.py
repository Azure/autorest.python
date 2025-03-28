# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from parameters.spread.aio import SpreadClient


class SpreadClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(SpreadClient, is_async=True)
        return self.create_client_from_credential(
            SpreadClient,
            credential=credential,
            endpoint=endpoint,
        )
