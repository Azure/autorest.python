# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from specialheaders.conditionalrequest import ConditionalRequestClient


class ConditionalRequestClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(ConditionalRequestClient)
        return self.create_client_from_credential(
            ConditionalRequestClient,
            credential=credential,
            endpoint=endpoint,
        )


ConditionalRequestPreparer = functools.partial(
    PowerShellPreparer, "conditionalrequest", conditionalrequest_endpoint="https://fake_conditionalrequest_endpoint.com"
)
