# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from versioning.removed.aio import RemovedClient


class RemovedClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(RemovedClient, is_async=True)
        return self.create_client_from_credential(
            RemovedClient,
            credential=credential,
            endpoint=endpoint,
        )
