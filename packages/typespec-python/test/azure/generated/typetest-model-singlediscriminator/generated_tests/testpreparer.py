# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from typetest.model.singlediscriminator import SingleDiscriminatorClient


class SingleDiscriminatorClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(SingleDiscriminatorClient)
        return self.create_client_from_credential(
            SingleDiscriminatorClient,
            credential=credential,
            endpoint=endpoint,
        )


SingleDiscriminatorPreparer = functools.partial(
    PowerShellPreparer,
    "singlediscriminator",
    singlediscriminator_endpoint="https://fake_singlediscriminator_endpoint.com",
)
