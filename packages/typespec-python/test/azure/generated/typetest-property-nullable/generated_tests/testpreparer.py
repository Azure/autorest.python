# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from typetest.property.nullable import NullableClient


class NullableClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(NullableClient)
        return self.create_client_from_credential(
            NullableClient,
            credential=credential,
            endpoint=endpoint,
        )


NullablePreparer = functools.partial(
    PowerShellPreparer, "nullable", nullable_endpoint="https://fake_nullable_endpoint.com"
)
