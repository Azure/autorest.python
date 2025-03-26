# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
from encode.bytes import BytesClient
import functools


class BytesClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(BytesClient)
        return self.create_client_from_credential(
            BytesClient,
            credential=credential,
            endpoint=endpoint,
        )


BytesPreparer = functools.partial(PowerShellPreparer, "bytes", bytes_endpoint="https://fake_bytes_endpoint.com")
