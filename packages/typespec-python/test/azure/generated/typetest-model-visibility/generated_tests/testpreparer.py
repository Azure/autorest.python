# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from typetest.model.visibility import VisibilityClient


class VisibilityClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(VisibilityClient)
        return self.create_client_from_credential(
            VisibilityClient,
            credential=credential,
            endpoint=endpoint,
        )


VisibilityPreparer = functools.partial(
    PowerShellPreparer, "visibility", visibility_endpoint="https://fake_visibility_endpoint.com"
)
