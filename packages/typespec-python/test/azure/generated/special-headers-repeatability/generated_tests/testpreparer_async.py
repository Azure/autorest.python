# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from specialheaders.repeatability.aio import RepeatabilityClient


class RepeatabilityClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(RepeatabilityClient, is_async=True)
        return self.create_client_from_credential(
            RepeatabilityClient,
            credential=credential,
            endpoint=endpoint,
        )
