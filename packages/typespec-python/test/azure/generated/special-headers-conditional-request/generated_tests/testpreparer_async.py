# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase
from specialheaders.conditionalrequest.aio import ConditionalRequestClient


class ConditionalRequestClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(ConditionalRequestClient, is_async=True)
        return self.create_client_from_credential(
            ConditionalRequestClient,
            credential=credential,
            endpoint=endpoint,
        )
