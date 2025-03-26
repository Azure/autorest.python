# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from resiliency.srv.driven2 import ResiliencyServiceDrivenClient


class ResiliencyServiceDrivenClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(ResiliencyServiceDrivenClient)
        return self.create_client_from_credential(
            ResiliencyServiceDrivenClient,
            credential=credential,
            endpoint=endpoint,
        )


ResiliencyServiceDrivenPreparer = functools.partial(
    PowerShellPreparer,
    "resiliencyservicedriven",
    resiliencyservicedriven_endpoint="https://fake_resiliencyservicedriven_endpoint.com",
)
