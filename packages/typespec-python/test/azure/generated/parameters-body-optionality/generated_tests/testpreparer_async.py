# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from parameters.bodyoptionality.aio import BodyOptionalityClient


class BodyOptionalityClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(BodyOptionalityClient, is_async=True)
        return self.create_client_from_credential(
            BodyOptionalityClient,
            credential=credential,
            endpoint=endpoint,
        )
