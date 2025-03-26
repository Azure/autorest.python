# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from payload.mediatype import MediaTypeClient


class MediaTypeClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(MediaTypeClient)
        return self.create_client_from_credential(
            MediaTypeClient,
            credential=credential,
            endpoint=endpoint,
        )


MediaTypePreparer = functools.partial(
    PowerShellPreparer, "mediatype", mediatype_endpoint="https://fake_mediatype_endpoint.com"
)
