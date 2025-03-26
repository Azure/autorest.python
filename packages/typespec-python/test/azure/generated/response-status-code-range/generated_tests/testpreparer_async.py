# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from response.statuscoderange.aio import StatusCodeRangeClient


class StatusCodeRangeClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(StatusCodeRangeClient, is_async=True)
        return self.create_client_from_credential(
            StatusCodeRangeClient,
            credential=credential,
            endpoint=endpoint,
        )
