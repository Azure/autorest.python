# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from typetest.model.enumdiscriminator import EnumDiscriminatorClient


class EnumDiscriminatorClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(EnumDiscriminatorClient)
        return self.create_client_from_credential(
            EnumDiscriminatorClient,
            credential=credential,
            endpoint=endpoint,
        )


EnumDiscriminatorPreparer = functools.partial(
    PowerShellPreparer, "enumdiscriminator", enumdiscriminator_endpoint="https://fake_enumdiscriminator_endpoint.com"
)
