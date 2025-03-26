# coding=utf-8
from client.structure.renamedoperation import RenamedOperationClient
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools


class RenamedOperationClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(RenamedOperationClient)
        return self.create_client_from_credential(
            RenamedOperationClient,
            credential=credential,
            endpoint=endpoint,
        )


RenamedOperationPreparer = functools.partial(
    PowerShellPreparer, "renamedoperation", renamedoperation_endpoint="https://fake_renamedoperation_endpoint.com"
)
