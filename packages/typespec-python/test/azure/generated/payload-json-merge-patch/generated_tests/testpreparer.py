# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from payload.jsonmergepatch import JsonMergePatchClient


class JsonMergePatchClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(JsonMergePatchClient)
        return self.create_client_from_credential(
            JsonMergePatchClient,
            credential=credential,
            endpoint=endpoint,
        )


JsonMergePatchPreparer = functools.partial(
    PowerShellPreparer, "jsonmergepatch", jsonmergepatch_endpoint="https://fake_jsonmergepatch_endpoint.com"
)
