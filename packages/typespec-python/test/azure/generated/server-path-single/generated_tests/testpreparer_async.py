# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from server.path.single.aio import SingleClient


class SingleClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(SingleClient, is_async=True)
        return self.create_client_from_credential(
            SingleClient,
            credential=credential,
            endpoint=endpoint,
        )
