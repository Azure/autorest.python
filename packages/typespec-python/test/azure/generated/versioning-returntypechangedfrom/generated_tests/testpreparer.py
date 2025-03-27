# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from versioning.returntypechangedfrom import ReturnTypeChangedFromClient


class ReturnTypeChangedFromClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(ReturnTypeChangedFromClient)
        return self.create_client_from_credential(
            ReturnTypeChangedFromClient,
            credential=credential,
            endpoint=endpoint,
        )


ReturnTypeChangedFromPreparer = functools.partial(
    PowerShellPreparer,
    "returntypechangedfrom",
    returntypechangedfrom_endpoint="https://fake_returntypechangedfrom_endpoint.com",
)
