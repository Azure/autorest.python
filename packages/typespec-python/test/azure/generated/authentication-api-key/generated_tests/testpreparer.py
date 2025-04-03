# coding=utf-8
from authentication.apikey import ApiKeyClient
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools


class ApiKeyClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(ApiKeyClient)
        return self.create_client_from_credential(
            ApiKeyClient,
            credential=credential,
            endpoint=endpoint,
        )


ApiKeyPreparer = functools.partial(PowerShellPreparer, "apikey", apikey_endpoint="https://fake_apikey_endpoint.com")
