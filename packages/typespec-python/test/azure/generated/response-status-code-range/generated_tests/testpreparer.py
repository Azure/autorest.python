# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from response.statuscoderange import StatusCodeRangeClient


class StatusCodeRangeClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(StatusCodeRangeClient)
        return self.create_client_from_credential(
            StatusCodeRangeClient,
            credential=credential,
            endpoint=endpoint,
        )


StatusCodeRangePreparer = functools.partial(
    PowerShellPreparer, "statuscoderange", statuscoderange_endpoint="https://fake_statuscoderange_endpoint.com"
)
