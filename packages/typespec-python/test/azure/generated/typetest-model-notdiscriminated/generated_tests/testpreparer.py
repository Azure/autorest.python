# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from typetest.model.notdiscriminated import NotDiscriminatedClient


class NotDiscriminatedClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(NotDiscriminatedClient)
        return self.create_client_from_credential(
            NotDiscriminatedClient,
            credential=credential,
            endpoint=endpoint,
        )


NotDiscriminatedPreparer = functools.partial(
    PowerShellPreparer, "notdiscriminated", notdiscriminated_endpoint="https://fake_notdiscriminated_endpoint.com"
)
