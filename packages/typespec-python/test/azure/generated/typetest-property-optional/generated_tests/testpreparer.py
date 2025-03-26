# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from typetest.property.optional import OptionalClient


class OptionalClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(OptionalClient)
        return self.create_client_from_credential(
            OptionalClient,
            credential=credential,
            endpoint=endpoint,
        )


OptionalPreparer = functools.partial(
    PowerShellPreparer, "optional", optional_endpoint="https://fake_optional_endpoint.com"
)
