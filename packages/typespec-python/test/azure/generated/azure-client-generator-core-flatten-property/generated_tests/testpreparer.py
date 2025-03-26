# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from specs.azure.clientgenerator.core.flattenproperty import FlattenPropertyClient


class FlattenPropertyClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(FlattenPropertyClient)
        return self.create_client_from_credential(
            FlattenPropertyClient,
            credential=credential,
            endpoint=endpoint,
        )


FlattenPropertyPreparer = functools.partial(
    PowerShellPreparer, "flattenproperty", flattenproperty_endpoint="https://fake_flattenproperty_endpoint.com"
)
