# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from typetest.model.nesteddiscriminator import NestedDiscriminatorClient


class NestedDiscriminatorClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(NestedDiscriminatorClient)
        return self.create_client_from_credential(
            NestedDiscriminatorClient,
            credential=credential,
            endpoint=endpoint,
        )


NestedDiscriminatorPreparer = functools.partial(
    PowerShellPreparer,
    "nesteddiscriminator",
    nesteddiscriminator_endpoint="https://fake_nesteddiscriminator_endpoint.com",
)
