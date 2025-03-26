# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
from encode.datetime import DatetimeClient
import functools


class DatetimeClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(DatetimeClient)
        return self.create_client_from_credential(
            DatetimeClient,
            credential=credential,
            endpoint=endpoint,
        )


DatetimePreparer = functools.partial(
    PowerShellPreparer, "datetime", datetime_endpoint="https://fake_datetime_endpoint.com"
)
