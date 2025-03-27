# coding=utf-8
from authentication.http.custom.aio import CustomClient
from devtools_testutils import AzureRecordedTestCase


class CustomClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(CustomClient, is_async=True)
        return self.create_client_from_credential(
            CustomClient,
            credential=credential,
            endpoint=endpoint,
        )
