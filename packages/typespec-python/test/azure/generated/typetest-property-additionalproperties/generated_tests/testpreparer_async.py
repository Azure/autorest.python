# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from typetest.property.additionalproperties.aio import AdditionalPropertiesClient


class AdditionalPropertiesClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(AdditionalPropertiesClient, is_async=True)
        return self.create_client_from_credential(
            AdditionalPropertiesClient,
            credential=credential,
            endpoint=endpoint,
        )
