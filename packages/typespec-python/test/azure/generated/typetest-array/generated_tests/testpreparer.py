# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from typetest.array import ArrayClient


class ArrayClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(ArrayClient)
        return self.create_client_from_credential(
            ArrayClient,
            credential=credential,
            endpoint=endpoint,
        )


ArrayPreparer = functools.partial(PowerShellPreparer, "array", array_endpoint="https://fake_array_endpoint.com")
