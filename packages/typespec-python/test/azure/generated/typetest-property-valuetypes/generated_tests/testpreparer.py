# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from typetest.property.valuetypes import ValueTypesClient


class ValueTypesClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(ValueTypesClient)
        return self.create_client_from_credential(
            ValueTypesClient,
            credential=credential,
            endpoint=endpoint,
        )


ValueTypesPreparer = functools.partial(
    PowerShellPreparer, "valuetypes", valuetypes_endpoint="https://fake_valuetypes_endpoint.com"
)
