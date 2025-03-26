# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from resiliency.srv.driven1.aio import ResiliencyServiceDrivenClient


class ResiliencyServiceDrivenClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(ResiliencyServiceDrivenClient, is_async=True)
        return self.create_client_from_credential(
            ResiliencyServiceDrivenClient,
            credential=credential,
            endpoint=endpoint,
        )
