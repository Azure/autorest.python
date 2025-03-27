# coding=utf-8
from devtools_testutils import AzureRecordedTestCase
from encode.datetime.aio import DatetimeClient


class DatetimeClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(DatetimeClient, is_async=True)
        return self.create_client_from_credential(
            DatetimeClient,
            credential=credential,
            endpoint=endpoint,
        )
