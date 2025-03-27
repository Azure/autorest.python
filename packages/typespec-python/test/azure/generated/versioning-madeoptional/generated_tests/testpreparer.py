# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from versioning.madeoptional import MadeOptionalClient


class MadeOptionalClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(MadeOptionalClient)
        return self.create_client_from_credential(
            MadeOptionalClient,
            credential=credential,
            endpoint=endpoint,
        )


MadeOptionalPreparer = functools.partial(
    PowerShellPreparer, "madeoptional", madeoptional_endpoint="https://fake_madeoptional_endpoint.com"
)
