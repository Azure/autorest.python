# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from routes.aio import RoutesClient


class RoutesClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(RoutesClient, is_async=True)
        return self.create_client_from_credential(
            RoutesClient,
            credential=credential,
            endpoint=endpoint,
        )
