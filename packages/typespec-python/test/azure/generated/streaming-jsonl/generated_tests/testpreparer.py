# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from streaming.jsonl import JsonlClient


class JsonlClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(JsonlClient)
        return self.create_client_from_credential(
            JsonlClient,
            credential=credential,
            endpoint=endpoint,
        )


JsonlPreparer = functools.partial(PowerShellPreparer, "jsonl", jsonl_endpoint="https://fake_jsonl_endpoint.com")
