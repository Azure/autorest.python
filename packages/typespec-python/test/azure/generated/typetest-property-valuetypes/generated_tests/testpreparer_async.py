# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from typetest.property.valuetypes.aio import ValueTypesClient


class ValueTypesClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(ValueTypesClient, is_async=True)
        return self.create_client_from_credential(
            ValueTypesClient,
            credential=credential,
            endpoint=endpoint,
        )
