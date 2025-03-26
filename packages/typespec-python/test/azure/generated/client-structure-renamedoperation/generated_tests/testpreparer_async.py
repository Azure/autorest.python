# coding=utf-8
None
from client.structure.renamedoperation.aio import RenamedOperationClient
from devtools_testutils import AzureRecordedTestCase


class RenamedOperationClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(RenamedOperationClient, is_async=True)
        return self.create_client_from_credential(
            RenamedOperationClient,
            credential=credential,
            endpoint=endpoint,
        )
