# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from typetest.model.empty import EmptyClient


class EmptyClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(EmptyClient)
        return self.create_client_from_credential(
            EmptyClient,
            credential=credential,
            endpoint=endpoint,
        )


EmptyPreparer = functools.partial(PowerShellPreparer, "empty", empty_endpoint="https://fake_empty_endpoint.com")
