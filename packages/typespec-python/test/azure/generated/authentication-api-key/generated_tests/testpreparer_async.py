# coding=utf-8
None
from authentication.apikey.aio import ApiKeyClient
from devtools_testutils import AzureRecordedTestCase


class ApiKeyClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(ApiKeyClient, is_async=True)
        return self.create_client_from_credential(
            ApiKeyClient,
            credential=credential,
            endpoint=endpoint,
        )
