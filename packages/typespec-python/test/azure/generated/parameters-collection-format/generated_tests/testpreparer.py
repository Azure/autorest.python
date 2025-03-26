# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from parameters.collectionformat import CollectionFormatClient


class CollectionFormatClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(CollectionFormatClient)
        return self.create_client_from_credential(
            CollectionFormatClient,
            credential=credential,
            endpoint=endpoint,
        )


CollectionFormatPreparer = functools.partial(
    PowerShellPreparer, "collectionformat", collectionformat_endpoint="https://fake_collectionformat_endpoint.com"
)
