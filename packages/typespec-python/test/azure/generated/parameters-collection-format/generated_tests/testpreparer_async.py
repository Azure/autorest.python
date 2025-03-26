# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from parameters.collectionformat.aio import CollectionFormatClient


class CollectionFormatClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(CollectionFormatClient, is_async=True)
        return self.create_client_from_credential(
            CollectionFormatClient,
            credential=credential,
            endpoint=endpoint,
        )
