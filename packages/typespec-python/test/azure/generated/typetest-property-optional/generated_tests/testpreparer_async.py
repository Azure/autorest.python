# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from typetest.property.optional.aio import OptionalClient


class OptionalClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(OptionalClient, is_async=True)
        return self.create_client_from_credential(
            OptionalClient,
            credential=credential,
            endpoint=endpoint,
        )
