# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from versioning.madeoptional.aio import MadeOptionalClient


class MadeOptionalClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(MadeOptionalClient, is_async=True)
        return self.create_client_from_credential(
            MadeOptionalClient,
            credential=credential,
            endpoint=endpoint,
        )
