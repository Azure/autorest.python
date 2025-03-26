# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from payload.multipart import MultiPartClient


class MultiPartClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(MultiPartClient)
        return self.create_client_from_credential(
            MultiPartClient,
            credential=credential,
            endpoint=endpoint,
        )


MultiPartPreparer = functools.partial(
    PowerShellPreparer, "multipart", multipart_endpoint="https://fake_multipart_endpoint.com"
)
