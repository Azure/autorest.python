# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from encode.numeric.aio import NumericClient


class NumericClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(NumericClient, is_async=True)
        return self.create_client_from_credential(
            NumericClient,
            credential=credential,
            endpoint=endpoint,
        )
