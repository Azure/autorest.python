# coding=utf-8
from authentication.oauth2.aio import OAuth2Client
from devtools_testutils import AzureRecordedTestCase


class OAuth2ClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(OAuth2Client, is_async=True)
        return self.create_client_from_credential(
            OAuth2Client,
            credential=credential,
            endpoint=endpoint,
        )
