# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from parameters.basic.aio import BasicClient


class BasicClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(BasicClient, is_async=True)
        return self.create_client_from_credential(
            BasicClient,
            credential=credential,
            endpoint=endpoint,
        )
