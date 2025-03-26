# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from payload.mediatype.aio import MediaTypeClient


class MediaTypeClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(MediaTypeClient, is_async=True)
        return self.create_client_from_credential(
            MediaTypeClient,
            credential=credential,
            endpoint=endpoint,
        )
