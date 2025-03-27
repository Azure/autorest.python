# coding=utf-8
from azure.specialheaders.xmsclientrequestid import XmsClientRequestIdClient
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools


class XmsClientRequestIdClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(XmsClientRequestIdClient)
        return self.create_client_from_credential(
            XmsClientRequestIdClient,
            credential=credential,
            endpoint=endpoint,
        )


XmsRequestIdPreparer = functools.partial(
    PowerShellPreparer, "xmsrequestid", xmsrequestid_endpoint="https://fake_xmsrequestid_endpoint.com"
)
