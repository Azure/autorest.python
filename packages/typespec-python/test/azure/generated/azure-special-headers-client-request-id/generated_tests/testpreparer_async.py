# coding=utf-8
None
from azure.specialheaders.xmsclientrequestid.aio import XmsClientRequestIdClient
from devtools_testutils import AzureRecordedTestCase


class XmsClientRequestIdClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(XmsClientRequestIdClient, is_async=True)
        return self.create_client_from_credential(
            XmsClientRequestIdClient,
            credential=credential,
            endpoint=endpoint,
        )
