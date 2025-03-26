# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
from encode.numeric import NumericClient
import functools


class NumericClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(NumericClient)
        return self.create_client_from_credential(
            NumericClient,
            credential=credential,
            endpoint=endpoint,
        )


NumericPreparer = functools.partial(PowerShellPreparer, "numeric", numeric_endpoint="https://fake_numeric_endpoint.com")
