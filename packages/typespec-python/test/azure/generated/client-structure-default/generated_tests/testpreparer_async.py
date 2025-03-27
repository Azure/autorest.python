# coding=utf-8
from client.structure.service.aio import ServiceClient
from devtools_testutils import AzureRecordedTestCase


class ServiceClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(ServiceClient, is_async=True)
        return self.create_client_from_credential(
            ServiceClient,
            credential=credential,
            endpoint=endpoint,
        )
