# coding=utf-8
from authentication.oauth2 import OAuth2Client
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools


class OAuth2ClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(OAuth2Client)
        return self.create_client_from_credential(
            OAuth2Client,
            credential=credential,
            endpoint=endpoint,
        )


OAuth2Preparer = functools.partial(PowerShellPreparer, "oauth2", oauth2_endpoint="https://fake_oauth2_endpoint.com")
