# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from typetest.model.visibility.aio import VisibilityClient


class VisibilityClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(VisibilityClient, is_async=True)
        return self.create_client_from_credential(
            VisibilityClient,
            credential=credential,
            endpoint=endpoint,
        )
