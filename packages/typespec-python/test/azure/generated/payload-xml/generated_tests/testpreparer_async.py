# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from payload.xml.aio import XmlClient


class XmlClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(XmlClient, is_async=True)
        return self.create_client_from_credential(
            XmlClient,
            credential=credential,
            endpoint=endpoint,
        )
