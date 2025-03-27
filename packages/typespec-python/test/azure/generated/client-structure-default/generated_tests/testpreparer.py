# coding=utf-8
from client.structure.service import ServiceClient
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools


class ServiceClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(ServiceClient)
        return self.create_client_from_credential(
            ServiceClient,
            credential=credential,
            endpoint=endpoint,
        )


ServicePreparer = functools.partial(PowerShellPreparer, "service", service_endpoint="https://fake_service_endpoint.com")
