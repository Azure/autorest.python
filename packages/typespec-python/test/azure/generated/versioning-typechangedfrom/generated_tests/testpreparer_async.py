# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from versioning.typechangedfrom.aio import TypeChangedFromClient


class TypeChangedFromClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(TypeChangedFromClient, is_async=True)
        return self.create_client_from_credential(
            TypeChangedFromClient,
            credential=credential,
            endpoint=endpoint,
        )
