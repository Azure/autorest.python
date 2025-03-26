# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from specs.azure.core.page import PageClient


class PageClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(PageClient)
        return self.create_client_from_credential(
            PageClient,
            credential=credential,
            endpoint=endpoint,
        )


PagePreparer = functools.partial(PowerShellPreparer, "page", page_endpoint="https://fake_page_endpoint.com")
