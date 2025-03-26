# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from serialization.encodedname.json import JsonClient


class JsonClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(JsonClient)
        return self.create_client_from_credential(
            JsonClient,
            credential=credential,
            endpoint=endpoint,
        )


JsonPreparer = functools.partial(PowerShellPreparer, "json", json_endpoint="https://fake_json_endpoint.com")
