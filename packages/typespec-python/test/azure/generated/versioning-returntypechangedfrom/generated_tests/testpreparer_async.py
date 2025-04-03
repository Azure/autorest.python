# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from versioning.returntypechangedfrom.aio import ReturnTypeChangedFromClient


class ReturnTypeChangedFromClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(ReturnTypeChangedFromClient, is_async=True)
        return self.create_client_from_credential(
            ReturnTypeChangedFromClient,
            credential=credential,
            endpoint=endpoint,
        )
