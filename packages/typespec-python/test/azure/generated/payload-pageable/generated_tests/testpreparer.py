# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from payload.pageable import PageableClient


class PageableClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(PageableClient)
        return self.create_client_from_credential(
            PageableClient,
            credential=credential,
            endpoint=endpoint,
        )


PageablePreparer = functools.partial(
    PowerShellPreparer, "pageable", pageable_endpoint="https://fake_pageable_endpoint.com"
)
