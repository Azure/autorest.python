# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from payload.contentnegotiation import ContentNegotiationClient


class ContentNegotiationClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(ContentNegotiationClient)
        return self.create_client_from_credential(
            ContentNegotiationClient,
            credential=credential,
            endpoint=endpoint,
        )


ContentNegotiationPreparer = functools.partial(
    PowerShellPreparer, "contentnegotiation", contentnegotiation_endpoint="https://fake_contentnegotiation_endpoint.com"
)
