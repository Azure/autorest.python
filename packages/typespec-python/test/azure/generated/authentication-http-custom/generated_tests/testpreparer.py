# coding=utf-8
None
from authentication.http.custom import CustomClient
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools


class CustomClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(CustomClient)
        return self.create_client_from_credential(
            CustomClient,
            credential=credential,
            endpoint=endpoint,
        )


CustomPreparer = functools.partial(PowerShellPreparer, "custom", custom_endpoint="https://fake_custom_endpoint.com")
