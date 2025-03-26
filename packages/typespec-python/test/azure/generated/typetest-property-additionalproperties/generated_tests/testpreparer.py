# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from typetest.property.additionalproperties import AdditionalPropertiesClient


class AdditionalPropertiesClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(AdditionalPropertiesClient)
        return self.create_client_from_credential(
            AdditionalPropertiesClient,
            credential=credential,
            endpoint=endpoint,
        )


AdditionalPropertiesPreparer = functools.partial(
    PowerShellPreparer,
    "additionalproperties",
    additionalproperties_endpoint="https://fake_additionalproperties_endpoint.com",
)
