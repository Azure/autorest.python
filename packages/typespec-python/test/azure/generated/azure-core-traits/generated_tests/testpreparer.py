# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from specs.azure.core.traits import TraitsClient


class TraitsClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(TraitsClient)
        return self.create_client_from_credential(
            TraitsClient,
            credential=credential,
            endpoint=endpoint,
        )


TraitsPreparer = functools.partial(PowerShellPreparer, "traits", traits_endpoint="https://fake_traits_endpoint.com")
