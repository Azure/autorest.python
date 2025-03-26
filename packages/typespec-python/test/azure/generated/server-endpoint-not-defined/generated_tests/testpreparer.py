# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from server.endpoint.notdefined import NotDefinedClient


class NotDefinedClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(NotDefinedClient)
        return self.create_client_from_credential(
            NotDefinedClient,
            credential=credential,
            endpoint=endpoint,
        )


NotDefinedPreparer = functools.partial(
    PowerShellPreparer, "notdefined", notdefined_endpoint="https://fake_notdefined_endpoint.com"
)
