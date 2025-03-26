# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from payload.xml import XmlClient


class XmlClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(XmlClient)
        return self.create_client_from_credential(
            XmlClient,
            credential=credential,
            endpoint=endpoint,
        )


XmlPreparer = functools.partial(PowerShellPreparer, "xml", xml_endpoint="https://fake_xml_endpoint.com")
