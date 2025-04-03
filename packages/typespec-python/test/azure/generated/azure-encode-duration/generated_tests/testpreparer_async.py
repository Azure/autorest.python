# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from specs.azure.encode.duration.aio import DurationClient


class DurationClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(DurationClient, is_async=True)
        return self.create_client_from_credential(
            DurationClient,
            credential=credential,
            endpoint=endpoint,
        )
