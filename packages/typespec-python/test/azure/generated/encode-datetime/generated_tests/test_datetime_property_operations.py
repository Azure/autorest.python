# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import DatetimeClientTestBase, DatetimePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDatetimePropertyOperations(DatetimeClientTestBase):
    @DatetimePreparer()
    @recorded_by_proxy
    def test_default(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.property.default(
            body={"value": "2020-02-20 00:00:00"},
        )

        # please add some check logic here by yourself

    @DatetimePreparer()
    @recorded_by_proxy
    def test_rfc3339(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.property.rfc3339(
            body={"value": "2020-02-20 00:00:00"},
        )

        # please add some check logic here by yourself

    @DatetimePreparer()
    @recorded_by_proxy
    def test_rfc7231(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.property.rfc7231(
            body={"value": "2020-02-20 00:00:00"},
        )

        # please add some check logic here by yourself

    @DatetimePreparer()
    @recorded_by_proxy
    def test_unix_timestamp(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.property.unix_timestamp(
            body={"value": "2020-02-20 00:00:00"},
        )

        # please add some check logic here by yourself

    @DatetimePreparer()
    @recorded_by_proxy
    def test_unix_timestamp_array(self, datetime_endpoint):
        client = self.create_client(endpoint=datetime_endpoint)
        response = client.property.unix_timestamp_array(
            body={"value": ["2020-02-20 00:00:00"]},
        )

        # please add some check logic here by yourself
